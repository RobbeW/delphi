import http.client
import json
import threading
import unittest
from unittest.mock import patch
from eval_grading.app import server

class ServerTest(unittest.TestCase):
    def setUp(self):
        self.s=server.make_server('/tmp',0); self.thread=threading.Thread(target=self.s.serve_forever,daemon=True); self.thread.start(); self.host=f'127.0.0.1:{self.s.server_port}'
    def tearDown(self): self.s.shutdown(); self.s.server_close(); self.thread.join()
    def request(self,path,headers=None):
        c=http.client.HTTPConnection('127.0.0.1',self.s.server_port); c.request('GET',path,headers=headers or {}); r=c.getresponse(); body=r.read(); c.close(); return r.status,body
    def test_private_paths_and_host_are_rejected(self):
        self.assertEqual(self.request('/state.json')[0],403); self.assertEqual(self.request('/',{'Host':'evil.example'})[0],403); self.assertEqual(self.request('/api/state')[0],403)
    def test_token_and_origin_required(self):
        import re
        status,html=self.request('/'); token=re.search(rb'content="([^"]+)"',html.split(b'name="review-token"')[1]).group(1).decode()
        with patch.object(server.core,'load',return_value={'students':[],'intake':{}}):
            self.assertEqual(self.request('/api/state',{'X-Review-Token':token,'Origin':'http://evil.example'})[0],403)
            self.assertEqual(self.request('/api/state',{'X-Review-Token':token,'Origin':'http://'+self.host})[0],200)
if __name__=='__main__': unittest.main()
