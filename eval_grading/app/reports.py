"""Private, revision-bound learner PDFs and teacher exports."""
import csv
import fcntl
import io
import os
from pathlib import Path
import re
import tempfile
import unicodedata
import zipfile
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
import reportlab
from . import core

LAYOUT='selection-feedback-v4'
LABELS={'functioneel':'Functioneel','leesbaarheid':'Leesbaarheid','programmeerconcepten':'Programmeerconcepten','wiskundeconcepten':'Wiskundeconcepten'}
FONT=Path(reportlab.__file__).parent/'fonts'
pdfmetrics.registerFont(TTFont('Vera',str(FONT/'Vera.ttf')))
pdfmetrics.registerFont(TTFont('VeraBold',str(FONT/'VeraBd.ttf')))
pdfmetrics.registerFontFamily('Vera',normal='Vera',bold='VeraBold',italic='Vera',boldItalic='VeraBold')
PURPLE=colors.HexColor('#5200FF'); INK=colors.HexColor('#160033'); PALE=colors.HexColor('#F3F0FA'); MUTED=colors.HexColor('#625B70'); RULE=colors.HexColor('#E2DDEA')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='BodyV',fontName='Vera',fontSize=9.5,leading=13.5,textColor=INK,spaceAfter=6))
styles.add(ParagraphStyle(name='TitleV',parent=styles['BodyV'],fontName='VeraBold',fontSize=22,leading=28,spaceAfter=12))
styles.add(ParagraphStyle(name='HeadV',parent=styles['BodyV'],fontName='VeraBold',fontSize=13,leading=18,textColor=PURPLE,spaceBefore=12,spaceAfter=8,keepWithNext=True))
styles.add(ParagraphStyle(name='SmallV',parent=styles['BodyV'],fontSize=9,leading=12.5))
styles.add(ParagraphStyle(name='ScoreV',parent=styles['BodyV'],fontName='VeraBold',fontSize=26,leading=34,textColor=PURPLE))
styles.add(ParagraphStyle(name='MutedV',parent=styles['BodyV'],fontSize=8.5,leading=12,textColor=MUTED))

def fmt(value): return f'{value:g}'.replace('.',',')
def p(text,style='BodyV'): return Paragraph(escape(str(text)).replace('\n','<br/>'),styles[style])
def labelled(label,text): return Paragraph('<b>'+escape(label)+'</b> '+escape(str(text)).replace('\n','<br/>'),styles['BodyV'])
def score(criteria):
    earned=sum(c['points'] for c in criteria.values() if c['points'] is not None)
    pending=sum(c['max'] for c in criteria.values() if c['points'] is None)
    maximum=sum(c['max'] for c in criteria.values())
    return (fmt(earned)+' - '+fmt(earned+pending) if pending else fmt(earned))+' / '+fmt(maximum)

def table(rows,widths):
    t=Table(rows,colWidths=widths,repeatRows=1,hAlign='LEFT',splitByRow=1,splitInRow=1)
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),PALE),('LINEBELOW',(0,0),(-1,0),.7,PURPLE),('LINEBELOW',(0,1),(-1,-1),.35,RULE),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]))
    return t

def build_pdf(student,destination,final=False):
    if final and not core.is_approved(student): raise ValueError('Deze revisie is niet goedgekeurd')
    destination=Path(destination);destination.parent.mkdir(parents=True,exist_ok=True,mode=0o700)
    fd,tmp=tempfile.mkstemp(dir=destination.parent,prefix='.report-',suffix='.pdf');os.close(fd)
    try:
        doc=SimpleDocTemplate(tmp,pagesize=(210*mm,297*mm),rightMargin=18*mm,leftMargin=18*mm,topMargin=30*mm,bottomMargin=20*mm,title='De Selectie - punten en feedback',author='Python in de Klas')
        total=core.totals(student)
        value=(fmt(total['range'][0])+' - '+fmt(total['range'][1])) if total['pending'] else fmt(total['earned'])
        status='Definitieve beoordeling' if final else 'Voorlopige beoordeling'
        story=[p('De Selectie','TitleV'),p(student['name']+' · '+student['class_name']),p(status,'MutedV'),Spacer(1,5*mm),p(value+' / 27','ScoreV')]
        if total['pending']: story.append(p('Dit scorebereik bevat nog open beoordelingen. Je leerkracht vult die aan voor de definitieve score.','MutedV'))
        story.append(p('Jouw punten per oefening','HeadV'))
        rows=[[p('Oefening','SmallV'),p('Score','SmallV')]]+[[p(e['title']),p(score(e['criteria']))] for e in student['exercises']]
        story.append(table(rows,[125*mm,49*mm]))
        story.append(p('De vier onderdelen','HeadV'))
        axes={k:{'max':sum(e['criteria'][k]['max'] for e in student['exercises']),
                 'points':None if any(e['criteria'][k]['points'] is None for e in student['exercises']) else sum(e['criteria'][k]['points'] for e in student['exercises'])} for k in LABELS}
        for key,c in axes.items():
            items={str(i):e['criteria'][key] for i,e in enumerate(student['exercises'])}
            story.append(labelled(LABELS[key]+':',score(items)))
        story.append(p('Op de volgende pagina’s zie je de punten en feedback per oefening.','MutedV'))
        story.append(PageBreak())
        for index,e in enumerate(student['exercises']):
            story.append(p(str(index+1)+'. '+e['title']+' · '+score(e['criteria']),'HeadV'))
            rows=[[p('Onderdeel','SmallV'),p('Punten','SmallV'),p('Feedback','SmallV')]]
            for key,c in e['criteria'].items():
                value='Open' if c['points'] is None else fmt(c['points'])+' / '+fmt(c['max'])
                rows.append([p(LABELS[key],'SmallV'),p(value,'SmallV'),p(c['rationale'],'SmallV')])
            story.append(table(rows,[50*mm,21*mm,103*mm]));story.append(Spacer(1,3*mm))
            feedback=[]
            for key,label in [('strength','Wat al lukt'),('improve','Volgende stap')]:
                feedback.append(labelled(label+':',e['feedback'][key]))
            story.append(KeepTogether(feedback))
            if index%2==1 and index<len(student['exercises'])-1:story.append(PageBreak())
        def decoration(canvas,doc):
            canvas.setFillColor(PURPLE);canvas.rect(0,294*mm,210*mm,3*mm,fill=1,stroke=0)
            canvas.setFont('VeraBold',9);canvas.setFillColor(INK);canvas.drawString(18*mm,282*mm,'PYTHON IN DE KLAS')
            canvas.setFont('Vera',8);canvas.setFillColor(MUTED);canvas.drawRightString(192*mm,282*mm,'Evaluatie - De Selectie')
            canvas.setStrokeColor(RULE);canvas.line(18*mm,15*mm,192*mm,15*mm)
            canvas.setFont('Vera',7.5);canvas.drawString(18*mm,10*mm,status+' · Robbe Wulgaert · AI in de Klas');canvas.drawRightString(192*mm,10*mm,str(doc.page))
        doc.build(story,onFirstPage=decoration,onLaterPages=decoration)
        os.replace(tmp,destination)
    finally:
        if os.path.exists(tmp):os.unlink(tmp)
    return destination

def slug(text):
    text=unicodedata.normalize('NFKD',text).encode('ascii','ignore').decode()
    return re.sub('[^a-zA-Z0-9_-]+','-',text).strip('-')[:80] or 'leerling'

def _render_locked(workspace,state,student,final):
    if final and not core.is_approved(student):raise ValueError('Deze revisie is niet goedgekeurd')
    dest=workspace/('final' if final else 'drafts')/slug(student['class_name'])/(slug(student['name'])+'-'+student['id'][:8])/'feedback.pdf'
    build_pdf(student,dest,final)
    core.atomic(dest.parent/'manifest.json',{'student_id':student['id'],'revision':student['revision'],'final':final,'layout':LAYOUT,
                                          'binding':state['binding'],'pdf_sha256':core.digest(dest.read_bytes())})
    return dest.read_bytes()

def render(workspace,student_id,final=False):
    workspace=Path(workspace)
    with open(workspace/'.lock','a+b') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX);state=core.load(workspace)
        student=next((s for s in state['students'] if s['id']==student_id),None)
        if not student:raise ValueError('Onbekende leerling')
        return _render_locked(workspace,state,student,final)

def drafts(workspace):
    workspace=Path(workspace)
    with open(workspace/'.lock','a+b') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX);state=core.load(workspace)
        for s in state['students']:_render_locked(workspace,state,s,False)
        return len(state['students'])

def safe_csv(value):return "'"+value if value.lstrip().startswith(('=','+','-','@','\t','\r')) else value

def teacher_csv(workspace):
    state=core.load(workspace);out=io.StringIO(newline='');writer=csv.writer(out)
    headers=['Naam','Klas','Score','Maximum','Revisie']+[e[1]+' - '+LABELS[k] for e in core.EXERCISES for k in LABELS]
    writer.writerow(headers)
    for s in state['students']:
        if core.is_approved(s):
            t=core.totals(s);writer.writerow([safe_csv(s['name']),safe_csv(s['class_name']),t['earned'],t['maximum'],s['revision']]+[s['exercises'][i]['criteria'][k]['points'] for i in range(6) for k in LABELS])
    return out.getvalue().encode('utf-8-sig')

def class_zip(workspace,class_name):
    workspace=Path(workspace);out=io.BytesIO()
    with open(workspace/'.lock','a+b') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX);state=core.load(workspace)
        chosen=[s for s in state['students'] if s['class_name']==class_name and core.is_approved(s)]
        if not chosen:raise ValueError('Er zijn nog geen goedgekeurde beoordelingen voor deze klas.')
        with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
            for s in chosen:z.writestr(slug(s['name'])+'-'+s['id'][:8]+'/feedback.pdf',_render_locked(workspace,state,s,True))
    return out.getvalue()
