import json, http.server, socketserver, os, sys, re
os.chdir(os.path.dirname(os.path.abspath(__file__))+'/out')
CART={'items':[]}
VAR2PROD={}  # variant id -> product id ("9"+pid)
class H(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*a): pass
    def _json(self,o,code=200):
        b=json.dumps(o).encode(); self.send_response(code); self.send_header('Content-Type','application/json'); self.send_header('Content-Length',str(len(b))); self.end_headers(); self.wfile.write(b)
    def do_GET(self):
        if self.path.startswith('/cart.js'): return self._json({'items':CART['items'],'item_count':sum(i['quantity'] for i in CART['items'])})
        return super().do_GET()
    def do_POST(self):
        n=int(self.headers.get('Content-Length',0)); body=json.loads(self.rfile.read(n) or b'{}')
        if self.path.startswith('/__set'):
            CART['items']=[{'product_id':int(p),'variant_id':int('9'+str(p)),'quantity':1} for p in body.get('products',[])]; return self._json(CART)
        if self.path.startswith('/cart/add.js'):
            if os.environ.get('FAIL'): return self._json({'status':422,'message':'Fel','description':'Slut'},422)
            for it in body['items']:
                vid=str(it['id']); pid=int(vid[1:])
                CART['items'].append({'product_id':pid,'variant_id':int(vid),'quantity':it['quantity']})
            return self._json({'items':body['items']})
        self._json({},404)
socketserver.TCPServer.allow_reuse_address=True
with socketserver.TCPServer(('127.0.0.1',int(sys.argv[1]) if len(sys.argv)>1 else 8765),H) as s: s.serve_forever()
