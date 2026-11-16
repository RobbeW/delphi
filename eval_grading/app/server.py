"""Loopback-only review server. No directory or private-file serving."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import secrets
from urllib.parse import urlsplit, parse_qs
from . import core, reports
from .rubric import DESCRIPTORS

WEB=Path(__file__).parent/'web'
def make_server(workspace,port=0):
    token=secrets.token_urlsafe(32)
    class Handler(BaseHTTPRequestHandler):
        def log_message(self,*args): pass
        def send(self,status,data,content='application/json; charset=utf-8',filename=None):
            self.send_response(status); self.send_header('Content-Type',content); self.send_header('Cache-Control','no-store'); self.send_header('X-Content-Type-Options','nosniff'); self.send_header('Content-Security-Policy',"default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self'; base-uri 'none'; frame-ancestors 'none'")
            if filename: self.send_header('Content-Disposition',f'attachment; filename="{filename}"')
            self.send_header('Content-Length',str(len(data))); self.end_headers(); self.wfile.write(data)
        def valid(self):
            host=self.headers.get('Host',''); expected=f'127.0.0.1:{self.server.server_port}'
            return host==expected and self.headers.get('Origin',f'http://{expected}')==f'http://{expected}' and secrets.compare_digest(self.headers.get('X-Review-Token',''),token)
        def do_GET(self):
            try:
                host=f'127.0.0.1:{self.server.server_port}'
                if self.headers.get('Host')!=host: return self.send(403,b'Forbidden','text/plain')
                path=urlsplit(self.path).path
                static={'/':('index.html','text/html; charset=utf-8'),'/app.js':('app.js','text/javascript; charset=utf-8'),'/style.css':('style.css','text/css; charset=utf-8'),'/favicon.png':('favicon.png','image/png')}
                if path in static:
                    file,ctype=static[path]; data=(WEB/file).read_bytes()
                    if path=='/': data=data.replace(b'__TOKEN__',token.encode())
                    return self.send(200,data,ctype)
                if not self.valid(): return self.send(403,b'Forbidden','text/plain')
                if path=='/api/state':
                    state=core.load(workspace); return self.send(200,json.dumps({'students':state['students'],'intake':state['intake'],'descriptors':DESCRIPTORS},ensure_ascii=False).encode())
                if path in ('/api/draft','/api/final'):
                    sid=parse_qs(urlsplit(self.path).query).get('id',[''])[0]; data=reports.render(workspace,sid,path.endswith('final')); return self.send(200,data,'application/pdf','feedback.pdf')
                if path=='/api/teacher-csv': return self.send(200,reports.teacher_csv(workspace),'text/csv; charset=utf-8','beoordelingen.csv')
                if path=='/api/class-zip': return self.send(200,reports.class_zip(workspace,parse_qs(urlsplit(self.path).query).get('class',[''])[0]),'application/zip','klas.zip')
                self.send(404,b'Not found','text/plain')
            except (ValueError,KeyError,OSError) as e: self.send(400,json.dumps({'error':str(e)}).encode())
        def do_POST(self):
            if not self.valid(): return self.send(403,b'Forbidden','text/plain')
            if self.path!='/api/review': return self.send(404,b'Not found','text/plain')
            try:
                length=int(self.headers.get('Content-Length','0'))
                if length<1 or length>2_000_000: raise ValueError('Ongeldige aanvraaggrootte')
                body=json.loads(self.rfile.read(length)); student=core.save_review(workspace,body['id'],body['revision'],body['actor'],body['exercises'],body.get('attested',False),body.get('approve',False)); self.send(200,json.dumps(student,ensure_ascii=False).encode())
            except (ValueError,KeyError,TypeError,OSError) as e: self.send(400,json.dumps({'error':str(e)}).encode())
    return ThreadingHTTPServer(('127.0.0.1',port),Handler)
