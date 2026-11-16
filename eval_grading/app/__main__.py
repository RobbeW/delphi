import argparse
from pathlib import Path
import webbrowser
from . import core, reports

ROOT=Path(__file__).resolve().parents[2]; YEAR=ROOT/'eval_grading'/'2026-2027'; WORK=ROOT/'eval_grading'/'private'/'selection-2026'
def discover(pattern):
    files=list(YEAR.rglob(pattern))
    if len(files)!=1: raise ValueError('Verwacht precies één '+pattern+' in '+str(YEAR))
    return files[0]
def main():
    parser=argparse.ArgumentParser(description='Lokale beoordeling selectie'); parser.add_argument('--workspace',type=Path,default=WORK)
    sub=parser.add_subparsers(dest='command',required=True)
    prep=sub.add_parser('prepare'); prep.add_argument('--archive',type=Path); prep.add_argument('--scoresheet',type=Path); prep.add_argument('--content-root',type=Path,default=ROOT/'content'/'02-Hoofdstuk 2 - Selectie'/'7-Evaluatie'); prep.add_argument('--include-unlabelled',action='store_true')
    serve=sub.add_parser('serve'); serve.add_argument('--port',type=int,default=0); serve.add_argument('--open',action='store_true')
    sub.add_parser('drafts'); release=sub.add_parser('release'); release.add_argument('--class-name',required=True); release.add_argument('--output',type=Path,required=True)
    csv=sub.add_parser('teacher-csv'); csv.add_argument('--output',type=Path,required=True)
    a=parser.parse_args()
    if a.command=='prepare':
        state=core.intake(a.archive or discover('*.zip'),a.scoresheet or discover('*.csv'),a.workspace,a.content_root,a.include_unlabelled); print('Voorbereid:',state['intake'])
    elif a.command=='drafts': print('Voorlopige rapporten:',reports.drafts(a.workspace))
    elif a.command=='serve':
        from .server import make_server
        core.load(a.workspace); server=make_server(a.workspace,a.port); url=f'http://127.0.0.1:{server.server_port}/'; print(url,flush=True)
        if a.open: webbrowser.open(url)
        try: server.serve_forever()
        except KeyboardInterrupt: pass
        finally: server.server_close()
    else:
        data=reports.class_zip(a.workspace,a.class_name) if a.command=='release' else reports.teacher_csv(a.workspace)
        a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_bytes(data); print('Geschreven:',a.output)
if __name__=='__main__': main()
