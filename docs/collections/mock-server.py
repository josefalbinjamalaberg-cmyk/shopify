import json, http.server, socketserver, os, sys, urllib.parse
os.chdir(os.path.dirname(os.path.abspath(__file__))+'/out')
CART={'items':[]}
class H(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*a): pass
    def _json(self,o,code=200):
        b=json.dumps(o).encode(); self.send_response(code); self.send_header('Content-Type','application/json'); self.send_header('Content-Length',str(len(b))); self.end_headers(); self.wfile.write(b)
    def _file(self,name):
        b=open(name,'rb').read(); self.send_response(200); self.send_header('Content-Type','text/html; charset=utf-8'); self.send_header('Content-Length',str(len(b))); self.end_headers(); self.wfile.write(b)
    def do_GET(self):
        u=urllib.parse.urlparse(self.path); q=urllib.parse.parse_qs(u.query)
        if u.path=='/cart.js': return self._json({'items':CART['items'],'item_count':len(CART['items'])})
        if u.path.startswith('/collections/'):
            h=u.path.split('/')[2]
            if h=='fardiga-paket': return self._file('fardiga-paket.html')
            intents=[v for k,vs in q.items() if 'intent_' in k for v in vs]
            kinds=[v for k,vs in q.items() if 'product_kind' in k for v in vs]
            if intents and kinds: return self._file('empty.html')
            if intents and os.path.exists(f'{h}--{intents[0]}.html'): return self._file(f'{h}--{intents[0]}.html')
            if kinds and os.path.exists(f'{h}--kind--{kinds[0]}.html'): return self._file(f'{h}--kind--{kinds[0]}.html')
            return self._file(f'{h}.html')
        return super().do_GET()
    def do_POST(self):
        n=int(self.headers.get('Content-Length',0)); body=json.loads(self.rfile.read(n) or b'{}')
        if self.path.startswith('/cart/add.js'):
            for it in body['items']: CART['items'].append({'variant_id':it['id'],'quantity':1})
            return self._json({'items':body['items']})
        self._json({},404)
socketserver.TCPServer.allow_reuse_address=True
with socketserver.TCPServer(('127.0.0.1',8790),H) as s: s.serve_forever()
