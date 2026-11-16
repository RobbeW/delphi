"""Private manifest intake and revisioned teacher review."""
import ast
import csv
import fcntl
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import tempfile
import zipfile
from .rubric import EXERCISES, DIMENSIONS, NORMAL, MOBIT, DESCRIPTORS
from .evaluator import run, parse_source
from .proposals import enrich, VERSION as PROPOSAL_VERSION

FORMAT = 'delphi-grading-v1'
def digest(data): return hashlib.sha256(data).hexdigest()
def encoded(value): return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',',':')).encode()
def engine_hash():
    return digest(encoded({name:digest(Path(__file__).with_name(name).read_bytes()) for name in ('core.py','evaluator.py','rubric.py','proposals.py')}))
def atomic(path, value):
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix='.grading-')
    try:
        with os.fdopen(fd,'wb') as f:
            f.write(encoded(value)); f.flush(); os.fsync(f.fileno())
        os.replace(tmp,path)
    finally:
        if os.path.exists(tmp): os.unlink(tmp)
def rows(data):
    reader=csv.DictReader(io.StringIO(data.decode('utf-8-sig'), newline=''))
    if not reader.fieldnames or len(reader.fieldnames)!=len(set(reader.fieldnames)): raise ValueError('Ongeldige CSV-kolommen')
    result=list(reader)
    if any(None in row for row in result): raise ValueError('Ongeldige CSV-rij')
    return result

def tests_for(content_root, folder):
    text=(Path(content_root)/folder/'evaluation/tests.yaml').read_text(encoding='utf-8')
    tests=[]; inp=None
    lines=iter(text.splitlines())
    for line in lines:
        m=re.match(r'^\s*-?\s*(stdin|stdout):\s*(.+)$',line)
        if not m: continue
        raw=m.group(2)
        while raw.startswith(('"',"'")) and not raw.endswith(raw[0]):
            try: raw += ' ' + next(lines).strip()
            except StopIteration: raise ValueError('Onvolledige publieke test') from None
        try: v=ast.literal_eval(raw)
        except (ValueError,SyntaxError): raise ValueError('Niet-ondersteunde publieke testnotatie')
        if not isinstance(v,str): raise ValueError('Niet-ondersteunde publieke testwaarde')
        if m.group(1)=='stdin': inp=v
        elif inp is not None: tests.append((inp,v)); inp=None
    if not tests or inp is not None: raise ValueError('Ongeldige publieke tests')
    return tests, text

def proposal(code,status,title,topic,maxima,tests,confirmed):
    source_lines=code.splitlines()
    try:
        tree=parse_source(code); nodes=list(ast.walk(tree)); syntax=None
    except SyntaxError as exc: nodes=[]; syntax=exc.lineno
    lines=lambda typ: sorted({n.lineno for n in nodes if isinstance(n,typ) and hasattr(n,'lineno')})[:12]
    checks=[]
    if nodes:
        for input_,expected in tests:
            result=run(code,input_)
            checks.append({'state':result['state'], 'passed':result.get('output')==expected if result['state']=='ok' else None})
    diagnostics={'syntax_error_line':syntax,'if_lines':lines(ast.If),'calculation_lines':lines(ast.BinOp),'assignment_lines':lines((ast.Assign,ast.AugAssign,ast.AnnAssign)), 'local_tests':{'provenance':'bevestigde historische taille-heuptests' if confirmed else 'lokale diagnostiek; bronversie niet bevestigd','total':len(tests),'passed':sum(c['passed'] is True for c in checks),'failed':sum(c['passed'] is False for c in checks),'unresolved':sum(c['passed'] is None for c in checks) if checks else len(tests)}}
    def criterion(maximum,points,rationale): return {'max':maximum,'points':points,'rationale':rationale,'checked':False}
    fp = maxima[0] if status=='correct' else 0 if status in ('wrong','runtime error','compilation error','unstarted') else None
    functional_reasons={'correct':'Je programma geeft de juiste uitvoer.',
                        'wrong':'Je programma geeft nog niet altijd de juiste uitvoer.',
                        'runtime error':'Je programma stopt met een foutmelding.',
                        'compilation error':'Je programma start niet door een fout in de schrijfwijze of inspringing.',
                        'unstarted':'Je hebt deze oefening niet ingediend.'}
    f=criterion(maxima[0],fp,functional_reasons.get(status,'De werking van je programma moet nog beoordeeld worden.'))
    l=criterion(maxima[1],None,'De namen en inspringing moeten nog worden nagekeken.')
    p=criterion(maxima[2],None,'De invoer en voorwaarden moeten nog worden nagekeken.')
    m=criterion(maxima[3],None,'De berekeningen moeten nog worden nagekeken.')
    if not code.strip():
        strength='Er is geen uitgewerkte oplossing beschikbaar om te bespreken.'
    elif syntax: strength='Je hebt een aanzet ingediend. Controleer de schrijfwijze rond regel '+str(syntax)+'.'
    else: strength='Je hebt een oplossing uitgewerkt.'
    criteria=dict(zip(DIMENSIONS,(f,l,p,m)))
    feedback={'strength':strength,'improve':'Controleer je oplossing voor '+title+'.'}
    diagnostics.update(enrich(code,title,maxima,tests,criteria,feedback))
    return diagnostics,criteria,feedback

def intake(archive,scoresheet,workspace,content_root,include_unlabelled=False):
    workspace=Path(workspace); a=Path(archive).read_bytes(); s=Path(scoresheet).read_bytes()
    public={}; public_hash={}
    for slug,title,folder,topic in EXERCISES:
        public[slug],txt=tests_for(content_root,folder); public_hash[slug]=digest(txt.encode())
    binding={'archive_sha256':digest(a),'scoresheet_sha256':digest(s),'rubric_sha256':digest(encoded([EXERCISES,NORMAL,MOBIT,DESCRIPTORS,PROPOSAL_VERSION])),'engine_sha256':engine_hash(),'public_tests_sha256':public_hash,'include_unlabelled':bool(include_unlabelled),'content_root':str(Path(content_root).resolve()),'archive_path':str(Path(archive).resolve()),'scoresheet_path':str(Path(scoresheet).resolve())}
    workspace.mkdir(parents=True,exist_ok=True,mode=0o700)
    with open(workspace/'.lock','a+b') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX)
        if (workspace/'baseline.json').exists() and not (workspace/'state.json').exists(): raise ValueError('Onvolledige bestaande beoordeling')
        if (workspace/'state.json').exists():
            state=load(workspace)
            if state['binding']!=binding: raise ValueError('Bestaande beoordeling heeft andere bronbindingen')
            return state
        roster=rows(s); roster=[r for r in roster if r.get('id','').lower() not in ('maximum','max','maxima')]
        byid={r['id']:r for r in roster}
        if len(byid)!=len(roster) or not all(byid): raise ValueError('Dubbele of ontbrekende account-ID')
        with zipfile.ZipFile(io.BytesIO(a)) as z:
            infos=z.infolist(); paths=[i.filename for i in infos]
            if len(paths)!=len({p.casefold() for p in paths}) or len(infos)>10000 or sum(i.file_size for i in infos)>100_000_000: raise ValueError('Ongeldig archief')
            for i in infos:
                p=PurePosixPath(i.filename)
                if p.is_absolute() or '..' in p.parts or '\\' in i.filename or re.match(r'^[A-Za-z]:',i.filename) or i.flag_bits&1 or ((i.external_attr>>16)&0o170000)==0o120000 or i.file_size>1_000_000: raise ValueError('Onveilig archiefpad of bestand')
            manifests=[p for p in paths if p.lower().endswith('.csv')]
            if len(manifests)!=1: raise ValueError('Eén manifest vereist')
            manifest=rows(z.read(manifests[0])); mapping={}; usedpaths=set(); submissions=set(); exids={}
            titles={x[1]:x for x in EXERCISES}
            for r in manifest:
                if not all(r.get(k) for k in ('filename','id','status','submission_id','exercise_id','created_at','name_nl')): raise ValueError('Onvolledig manifest')
                if r['id'] not in byid or r['name_nl'] not in titles: raise ValueError('Onbekend account of oefening')
                k=(r['id'],r['name_nl']); path=r['filename']
                if k in mapping or path in usedpaths or r['submission_id'] in submissions or path not in paths or not path.endswith('.py'): raise ValueError('Dubbele of ontbrekende inzending')
                if r['exercise_id'] in exids and exids[r['exercise_id']]!=r['name_nl']: raise ValueError('Dubbele oefening-ID')
                exids[r['exercise_id']]=r['name_nl']
                account=byid[r['id']]
                if any(r.get(k)!=account.get(k) for k in ('username','first_name','last_name','email')) or account.get('Status '+r['name_nl'])!=r['status']: raise ValueError('Manifest en scoresheet verschillen')
                mapping[k]=r; usedpaths.add(path); submissions.add(r['submission_id'])
            if usedpaths!={p for p in paths if p.endswith('.py')}: raise ValueError('Bronnen en manifest verschillen')
            students=[]
            for account in roster:
                if not include_unlabelled and not account.get('labels'): continue
                exercises=[]
                for slug,title,folder,topic in EXERCISES:
                    record=mapping.get((account['id'],title)); status=account.get('Status '+title,'')
                    if record is None and status!='unstarted': raise ValueError('Status zonder inzending')
                    if record and status=='unstarted': raise ValueError('Inzending met status niet gestart')
                    if account.get(title) not in ('0','1') or (account[title]=='1') != (status=='correct'): raise ValueError('Ongeldige platformscore')
                    code=z.read(record['filename']).decode('utf-8-sig') if record else ''
                    maximum=MOBIT if slug=='mobit' else NORMAL
                    diag,criteria,feedback=proposal(code,status,title,topic,maximum,public[slug],slug=='taille-heup')
                    exercises.append({'id':slug,'title':title,'source':{'state':'submitted' if record else 'not_submitted','code':code,'sha256':digest(code.encode()),'status':status,'submission_id':record['submission_id'] if record else None},'diagnostics':diag,'criteria':criteria,'feedback':feedback})
                students.append({'id':digest((binding['archive_sha256']+':'+account['id']).encode())[:24],'name':(account.get('first_name','')+' '+account.get('last_name','')).strip(),'class_name':account.get('labels',''),'revision':0,'attested':False,'approved_revision':None,'history':[],'exercises':exercises})
        state={'format':FORMAT,'binding':binding,'students':students,'intake':{'accounts':len(roster),'unlabelled':sum(not r.get('labels') for r in roster),'included':len(students)}}
        atomic(workspace/'baseline.json',state); atomic(workspace/'state.json',state)
        return state

def immutable(student):
    return [(e['id'],e['title'],e['source'],e['diagnostics'],{k:v['max'] for k,v in e['criteria'].items()}) for e in student['exercises']]
def load(workspace,verify=True):
    workspace=Path(workspace); state=json.loads((workspace/'state.json').read_text()); base=json.loads((workspace/'baseline.json').read_text())
    if verify:
        if state['format']!=FORMAT or state['binding']!=base['binding'] or len(state['students'])!=len(base['students']): raise ValueError('Bronbinding ongeldig')
        if digest(Path(state['binding']['archive_path']).read_bytes())!=state['binding']['archive_sha256'] or digest(Path(state['binding']['scoresheet_path']).read_bytes())!=state['binding']['scoresheet_sha256']: raise ValueError('Invoerbestanden gewijzigd')
        if state['binding']['rubric_sha256']!=digest(encoded([EXERCISES,NORMAL,MOBIT,DESCRIPTORS,PROPOSAL_VERSION])): raise ValueError('Rubric gewijzigd')
        if state['binding'].get('engine_sha256')!=engine_hash(): raise ValueError('Beoordelingslogica gewijzigd; gebruik een nieuwe werkmap en behoud het vorige dossier')
        for slug,title,folder,topic in EXERCISES:
            _,txt=tests_for(state['binding']['content_root'],folder)
            if digest(txt.encode())!=state['binding']['public_tests_sha256'][slug]: raise ValueError('Publieke tests gewijzigd')
        for s,b in zip(state['students'],base['students']):
            if any(e['source']['sha256']!=digest(e['source']['code'].encode()) for e in b['exercises']): raise ValueError('Broncode gewijzigd')
            if any(s[k]!=b[k] for k in ('id','name','class_name')) or immutable(s)!=immutable(b): raise ValueError('Onveranderlijk bewijs gewijzigd')
    return state

def save_review(workspace,student_id,expected_revision,actor,exercises,attested=False,approve=False,reason='Nakijken'):
    workspace=Path(workspace)
    with open(workspace/'.lock','a+b') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX); state=load(workspace)
        student=next((s for s in state['students'] if s['id']==student_id),None)
        if student is None: raise ValueError('Onbekende leerling')
        if type(expected_revision) is not int or student['revision']!=expected_revision: raise ValueError('Verouderde revisie')
        if not isinstance(actor,str) or not actor.strip() or not isinstance(reason,str) or not reason.strip(): raise ValueError('Naam en reden vereist')
        candidate=dict(student,exercises=exercises)
        try:
            if immutable(candidate)!=immutable(student): raise ValueError('Bewijs of maxima gewijzigd')
            for e in exercises:
                if set(e)!= {'id','title','source','diagnostics','criteria','feedback'} or set(e['criteria'])!=set(DIMENSIONS) or set(e['feedback'])!={'strength','improve'}: raise ValueError('Ongeldige beoordeling')
                if any(not isinstance(v,str) or len(v)>10000 for v in e['feedback'].values()): raise ValueError('Ongeldige feedback')
                for key,c in e['criteria'].items():
                    if set(c)!={'max','points','rationale','checked'} or type(c['checked']) is not bool or not isinstance(c['rationale'],str) or len(c['rationale'])>10000: raise ValueError('Ongeldig criterium')
                    allowed=([0,.5] if key=='functioneel' else [0,.25,.5]) if e['id']=='mobit' else ([0,1] if key=='functioneel' else [0,1,2] if key=='programmeerconcepten' else [0,.5,1])
                    if c['points'] is not None and (type(c['points']) not in (int,float) or c['points'] not in allowed): raise ValueError('Ongeldig puntniveau')
                    if approve and (not c['checked'] or c['points'] is None or len(c['rationale'].strip())<10): raise ValueError('Alle criteria moeten nagekeken en gemotiveerd zijn')
            if type(attested) is not bool or type(approve) is not bool or approve and not attested: raise ValueError('Bronbevestiging vereist')
        except (KeyError,TypeError,AttributeError): raise ValueError('Ongeldige beoordeling') from None
        student['exercises']=exercises; student['revision']+=1; student['attested']=attested; student['approved_revision']=student['revision'] if approve else None
        student['history'].append({'revision':student['revision'],'actor':actor,'reason':reason,'approved':approve})
        atomic(workspace/'state.json',state); return student

def totals(student):
    criteria=[c for e in student['exercises'] for c in e['criteria'].values()]; earned=sum(c['points'] for c in criteria if c['points'] is not None); pending=sum(c['max'] for c in criteria if c['points'] is None); maximum=sum(c['max'] for c in criteria)
    return {'earned':earned,'pending':pending,'maximum':maximum,'range':[earned,earned+pending]}
def is_approved(student):
    return bool(student['approved_revision'] is not None and student['approved_revision']==student['revision'] and student['attested']
                and all(c['checked'] and c['points'] is not None and len(c['rationale'].strip())>=10 for e in student['exercises'] for c in e['criteria'].values()))
