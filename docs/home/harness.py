import re, json, os, sys, html as H
from liquid import Environment, DictLoader
R='/home/user/shopify/'
mode=sys.argv[1]  # before|after
SRC = 'before/' if mode=='before' else R
L='/tmp/claude-0/-home-user-shopify/1a32fd48-c4be-54e0-9836-3c7f4bb6dcec/scratchpad/home/live/'
def clean(s):
    for t in ('doc','schema','stylesheet','javascript','comment'):
        s=re.sub(r'\{%%-?\s*%s\s*-?%%\}.*?\{%%-?\s*end%s\s*-?%%\}'%(t,t),'',s,flags=re.S)
    s=re.sub(r'\{%-?\s*#[^%]*%\}','',s); s=re.sub(r'(?m)^\s*#.*$','',s)
    return s
def styles(s): return '\n'.join(re.findall(r'\{% stylesheet %\}(.*?)\{% endstylesheet %\}',s,re.S))
def ph(name,w=600,h=600,bg='f5f5f2',col='3a3a3a',bottle=True):
    n=name.replace('&','och')
    body=f"<rect x='40%' y='14%' width='20%' height='66%' rx='10' fill='%23{col}'/>" if bottle else ""
    return {'src':f"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='{w}' height='{h}' viewBox='0 0 {w} {h}'><rect width='100%' height='100%' fill='%23{bg}'/>{body}<text x='50%' y='92%' font-size='{int(w/24)}' text-anchor='middle' font-family='sans-serif' fill='%23888'>{n[:30]}</text></svg>",'width':w,'height':h,'alt':'','presentation':{'focal_point':'center'}}
P={}
def prod(h,t,price,col='3a3a3a',comps=None,kit_name=None):
    p={'title':t,'handle':h,'url':'/products/'+h,'price':price,'compare_at_price':None,'featured_image':ph(t.split(' –')[0],600,600,'f5f5f2',col),'available':True,
       'metafields':{'custom':{'kit_components':{'value':comps or []},'kit_name':{'value':kit_name}, 'kit_separate_adjust':{'value':None}}}}
    P[h]=p; return p
for h,t,pr,c in [('revolt-flygrostborttagare','Revolt – Flygrostborttagare',18900,'5a3a5a'),('alkastrike-alkalisk-avfettning','Alkastrike – Alkalisk Avfettning',14900,'3a5a3a'),
 ('deepdegrease-kallavfettning','DeepDegrease – Kallavfettning',16900,'2b2b2b'),('foamtastic-hogkoncentrerat-snow-foam','Foamtastic – Snow Foam för effektiv förtvätt',16900,'9fb3bd'),
 ('pure-shampoo-ph-neutralt-bilschampo','Pure Shampoo – Bilschampo',17900,'d9d4c7'),('glosscoat-hydrofobisk-sprayforsegling','GlossCoat – Sprayförsegling',18900,'303030'),
 ('clarity-glasrengoring','Clarity – Glasrengöring',14900,'a9c4d0'),('pristine-dack-plastfornyare','Pristine - Däck- & Plastförnyare',18900,'c9a3b3'),
 ('core-apc-allrengoring','Core APC – Allrengöring (APC)',15900,'7a7a7a'),('foam-lance-skumlans','Foam Cannon',39900,'777777')]:
    prod(h,t,pr,c)
def comp(h): return {'variant':{'value':{'price':P[h]['price'],'product':P[h]}},'quantity':{'value':1}}
prod('litet-exterior-startkit','Exteriör Startkit',42900,'444',[comp(x) for x in ['deepdegrease-kallavfettning','alkastrike-alkalisk-avfettning','pure-shampoo-ph-neutralt-bilschampo']],'Exteriör Startkit')
prod('foam-wash-kit','Foam Wash Kit',46900,'444',[comp(x) for x in ['foamtastic-hogkoncentrerat-snow-foam','foam-lance-skumlans']],'Foam Wash Kit')
prod('exterior-komplett-kit','Exteriör Komplett Kit',119900,'444',[comp(x) for x in ['deepdegrease-kallavfettning','alkastrike-alkalisk-avfettning','foamtastic-hogkoncentrerat-snow-foam','pure-shampoo-ph-neutralt-bilschampo','revolt-flygrostborttagare','clarity-glasrengoring','pristine-dack-plastfornyare','glosscoat-hydrofobisk-sprayforsegling']],'Exteriör Komplett Kit')
REV=[('streamnight',4,'Fantastisk','Snabb leverans till Gotland, en riktigt bra flygrostborttagare som gav ett fantastiskt resultat. Även en riktigt bra alkalisk avfättning. Grymma dofter som ger en bra känsla när man lägger på medlet. Slutresultatet på bil som hoj blir otroligt bra!','11 september 2026'),
 ('Hyseni',5,'Produkterna var riktigt bra och lätta…','Produkterna var riktigt bra och lätta att använda, kall- och alkaliska avfettningarna var riktigt bra för att få bort 150mils smuts från bilen, schampot gjorde bilen riktigt fin o blank med som dessutom skummade på bra och luktade riktigt gott! Rekommenderar starkt dessa produkter!','9 september 2026'),
 ('My Segerstedt',5,'Riktigt nöjd med produkterna!','Fantastiska produkter! Fälg rengöringen är helt otrolig, fälgarna var extremt smutsiga, sprayade på och lät de bara sitta en stund, spolade av och allt var borta! Avfettning och Schampo var också underbart. Gör definitivt sitt jobb ordentligt. Glosscoat gjorde bilen otroligt glansig🥰 Kommer definitivt fortsätta med dessa produkter❤️','8 september 2026')]
reviews=[{'author':{'value':a},'rating':{'value':r},'title':{'value':t},'body':{'value':b},'date':{'value':d}} for a,r,t,b,d in REV]
vidobj={'sources':[{'format':'mp4','height':480,'url':'v480.mp4'},{'format':'mp4','height':1080,'url':'v1080.mp4'},{'format':'mp4','height':720,'url':'v720.mp4'},{'format':'m3u8','height':1080,'url':'v.m3u8'}],'preview_image':ph('video',1600,900,'2a2a2a','555',False)}
snips={'icon-or-image':'<svg viewBox="0 0 20 20" class="{{ class_name }}"><circle cx="10" cy="10" r="7" fill="none" stroke="currentColor" stroke-width="1.4"/></svg>'}
for n in ['nr-video-toggle','nr-video-sources','nr-ks-separate','nr-kit-separate-total']:
    if os.path.exists(R+'snippets/'+n+'.liquid'): snips[n]=clean(open(R+'snippets/'+n+'.liquid').read())
env=Environment(loader=DictLoader(snips))
def money(c):
    c=float(c); kr=int(c)//100; ore=int(round(c))%100
    return f"{kr:,}".replace(',',' ')+(f",{ore:02d}" if ore else '')+' kr'
env.filters['money']=money
env.filters['asset_url']=lambda s:'/'+s
env.filters['stylesheet_tag']=lambda s:''
env.filters['image_url']=lambda i,**k: (i or {}).get('src','') if isinstance(i,dict) else str(i)
env.filters['image_tag']=lambda u,**k: f'<img src="{u}" alt="{k.get("alt","")}" loading="lazy" style="{k.get("style","")}">'
settings={'nr_trustpilot_rating':'4.7','nr_trustpilot_count':34,'nr_trustpilot_url':'https://se.trustpilot.com/review/nordicreflection.se','free_shipping_threshold':799,'nr_production_mode':False}
def resolve(k,v):
    if isinstance(v,str) and v in P: return P[v]
    if isinstance(v,str) and v.startswith('shopify://files/videos'): return vidobj
    if isinstance(v,str) and v.startswith('shopify://shop_images'): return ph(k,1200,900,'cfcac0','',False)
    return v
tplsrc = L+'templates/index.json' if mode=='before' else R+'templates/index.json'
tpl=json.loads((lambda r:r[r.index('{'):])(open(tplsrc).read()))
css=open(SRC+('assets/' if mode=='before' else 'assets/')+'nr-homepage.css').read()
out=[]
def card(block):
    p=resolve('',block['settings']['product']); uc=block['blocks']['usecase']['settings']['text']
    return f'<product-card class="product-card"><div class="card-gallery" style="aspect-ratio:1"><img src="{p["featured_image"]["src"]}" style="width:100%;height:100%;object-fit:contain"></div><div class="product-card__content"><a href="{p["url"]}" class="title" role="heading">{H.escape(p["title"])}</a><div class="uc">{uc}</div><product-price>{money(p["price"])}</product-price><button class="qa">Lägg i varukorgen</button></div></product-card>'
for k in tpl['order']:
    s=tpl['sections'][k]
    if s.get('disabled'): continue
    typ=s['type']
    if typ=='_blocks':
        if mode=='before' and s.get('block_order'):
            src=open('before/ai_gen_block_f9f7e7d.liquid').read(); css+=styles(src)
            src=src.replace('{% style %}','<style>').replace('{% endstyle %}','</style>')
            b=s['blocks'][s['block_order'][0]]
            out.append(env.from_string(clean(src)).render(block={'settings':b['settings'],'id':'x','shopify_attributes':''},ai_gen_id='x',settings=settings,shop={'metaobjects':{}}))
        else:
            out.append('<div class="empty-blocks-section" style="min-height:0"></div>')
        continue
    path=(SRC if os.path.exists(SRC+'sections/'+typ+'.liquid') else R)+'sections/'+typ+'.liquid'
    src=open(path).read(); css+=styles(src)
    ss={kk:resolve(kk,v) for kk,v in s.get('settings',{}).items()}
    bl=[]
    for bk in s.get('block_order',[]):
        b=s['blocks'][bk]; bs={kk:resolve(kk,v) for kk,v in b.get('settings',{}).items()}
        bl.append({'settings':bs,'id':bk,'shopify_attributes':'','type':b['type']})
    body=clean(src).replace('alt: section.settings.image.alt | default: section.settings.heading,','alt: section.settings.heading,')
    if typ=='nr-home-featured-products':
        cards=''.join(card(s['blocks'][bk]) for bk in s['block_order'])
        body=body.replace("{% content_for 'blocks' %}",cards)
    out.append(env.from_string(body).render(section={'settings':ss,'blocks':bl,'id':k},settings=settings,shop={'metaobjects':{'nr_trustpilot_review':{'values':reviews}}},routes={'collections_url':'/collections'}))
html=f'''<!doctype html><html lang="sv"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>
*{{box-sizing:border-box}} body{{margin:0;font-family:Inter,"Helvetica Neue",Arial,sans-serif;color:#111;--font-heading--family:Inter,"Helvetica Neue",Arial,sans-serif}}
.visually-hidden{{position:absolute;clip:rect(0 0 0 0);width:1px;height:1px;overflow:hidden}}
header.h{{position:sticky;top:0;z-index:5;height:60px;background:#fff;border-bottom:1px solid #eee;display:flex;align-items:center;justify-content:space-between;padding:0 16px;font-weight:700}}
.nr-hero video{{background:#4a4f55}}
product-card{{display:flex;flex-direction:column;gap:8px}} .title{{font-weight:600;color:#111;text-decoration:none}} .uc{{font-size:13px;color:#555}} .uc p{{margin:0}} .qa{{margin-top:8px;height:40px;border:1px solid #111;background:#fff;border-radius:4px}}
.nr-grid{{display:grid;gap:24px}} .nr-grid--3{{grid-template-columns:repeat(3,1fr)}} .nr-grid--4{{grid-template-columns:repeat(4,1fr)}}
{css}
[data-nr-reveal],[data-nr-reveal] > *{{opacity:1!important;transform:none!important;visibility:visible!important}} header.h{{position:relative}}</style></head><body><header class="h">NordicReflection<span>☰</span></header>{''.join(out)}<footer style="height:200px;background:#111"></footer>
<script>document.querySelectorAll('video').forEach(v=>v.poster=v.poster)</script></body></html>'''
os.makedirs('out',exist_ok=True); open(f'out/{mode}.html','w').write(html); print('ok',mode)
