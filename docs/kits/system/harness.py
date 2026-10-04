import re, json, os, sys
from liquid import Environment, DictLoader
R='/home/user/shopify/'
def clean(s):
    for t in ('doc','schema','stylesheet','javascript'):
        s=re.sub(r'\{%%-?\s*%s\s*-?%%\}.*?\{%%-?\s*end%s\s*-?%%\}'%(t,t),'',s,flags=re.S)
    s=re.sub(r'\{%-?\s*#[^%]*%\}','',s); s=re.sub(r'(?m)^\s*#.*$','',s)
    return s
COLORS={'deepdegrease':'2b2b2b','alkastrike':'3a5a3a','pure':'d9d4c7','foamtastic':'c7d3d9','revolt':'5a3a5a','clarity':'cfe0e8','pristine':'e8cfd9','glosscoat':'303030','foam cannon':'777777'}
def ph(name,w=600,h=600,bg='f5f5f2',kit=False):
    n=name.replace('&','och')
    col=next((v for k,v in COLORS.items() if k in n.lower()),'bdb8ad')
    if kit:
        body=f"<rect x='22%' y='26%' width='14%' height='52%' rx='8' fill='%23{COLORS['deepdegrease']}'/><rect x='43%' y='30%' width='14%' height='48%' rx='8' fill='%23{COLORS['alkastrike']}'/><rect x='64%' y='30%' width='14%' height='48%' rx='8' fill='%23{COLORS['pure']}'/>"
    else:
        body=f"<rect x='38%' y='14%' width='24%' height='66%' rx='10' fill='%23{col}'/>"
    return {'src':f"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='{w}' height='{h}' viewBox='0 0 {w} {h}'><rect width='100%' height='100%' fill='%23{bg}'/>{body}<text x='50%' y='92%' font-size='{int(w/22)}' text-anchor='middle' font-family='sans-serif' fill='%23777'>{n[:28]}</text></svg>"}
vid={'media_type':'video'}
P={}
def prod(pid,title,handle,price,tl,video=False,variants=1,safety=None,mf=None):
    p={'id':pid,'title':title,'handle':handle,'url':'/products/'+handle,'price':price,'available':True,'featured_image':ph(title.split(' –')[0]),
       'variants':list(range(variants)),'selected_or_first_available_variant':{'id':pid*10,'price':price,'available':True},
       'metafields':{'pdp':{'type_label':{'value':tl},'demo_media':{'value':[vid] if video else []},'safety_note':{'value':safety}},'custom':mf or {}}}
    P[handle]=p; return p
prod(11,'DeepDegrease – Kallavfettning','deepdegrease-kallavfettning',16900,'Kallavfettning',safety='Brandfarlig (H226). Använd aldrig nära öppen låga, gnistor eller värmekällor och arbeta i ett väl ventilerat utrymme.')
prod(12,'Alkastrike – Alkalisk Avfettning','alkastrike-alkalisk-avfettning',14900,'Alkalisk förtvätt',True,safety='Använd inte på varma ytor eller i direkt solljus, och låt aldrig produkten torka in.')
prod(13,'Pure Shampoo – Bilschampo','pure-shampoo-ph-neutralt-bilschampo',17900,'Bilschampo för kontaktvätt',True,safety='Låt inte produkten torka på ytan. Skölj av grundligt och arbeta gärna i skugga.')
prod(14,'Foamtastic – Snow Foam för effektiv förtvätt','foamtastic-hogkoncentrerat-snow-foam',16900,'Snow foam / förtvätt',True)
prod(15,'Foam Cannon','foam-lance-skumlans',39900,'Foam cannon / skumkanon')
prod(16,'Revolt – Flygrostborttagare','revolt-flygrostborttagare',18900,'Flygrostborttagare',True)
prod(17,'Clarity – Glasrengöring','clarity-glasrengoring',14900,'Glasrengöring')
prod(18,'Pristine - Däck- & Plastförnyare','pristine-dack-plastfornyare',18900,'Däck- och plastförnyare',True)
prod(19,'GlossCoat – Sprayförsegling','glosscoat-hydrofobisk-sprayforsegling',18900,'Sprayförsegling',True)
def comp(h,size,group,purpose='',role=''):
    p=P[h]; v={'id':1000+p['id'],'price':p['price'],'product':p,'image':None,'url':p['url']}
    return {'variant':{'value':v},'quantity':{'value':1},'size':{'value':size},'group':{'value':group},'purpose':{'value':purpose},'role':{'value':role}}
C={'dd':comp('deepdegrease-kallavfettning','1000 ml','Förtvätt'),'alk':comp('alkastrike-alkalisk-avfettning','500 ml','Förtvätt'),
   'foam':comp('foamtastic-hogkoncentrerat-snow-foam','1000 ml','Förtvätt'),'pure':comp('pure-shampoo-ph-neutralt-bilschampo','500 ml','Handtvätt'),
   'rev':comp('revolt-flygrostborttagare','500 ml','Järn & bromsdamm'),'cla':comp('clarity-glasrengoring','500 ml','Glas'),
   'pri':comp('pristine-dack-plastfornyare','500 ml','Finish & skydd'),'gc':comp('glosscoat-hydrofobisk-sprayforsegling','500 ml','Finish & skydd'),
   'fc':comp('foam-lance-skumlans',None,'Applicering')}
def kit(pid,title,handle,price,comps,md):
    md=dict(md); md['kit_components']={'value':[C[c] for c in comps]}
    p={'id':pid,'title':title,'handle':handle,'url':'/products/'+handle,'price':price,'available':True,'featured_image':ph(title,1254,1254,'ece9e2',True),
       'selected_or_first_available_variant':{'id':pid*10,'price':price,'available':True},'variants':[0],'metafields':{'custom':md,'pdp':{}}}
    P[handle]=p; return p
start=kit(201,'Exteriör Startkit','litet-exterior-startkit',42900,['dd','alk','pure'],{
  'kit_eyebrow':{'value':'Exteriör · Start'},'kit_name':{'value':'Exteriör Startkit'},'kit_display_title':{'value':'Exteriör startkit'},'kit_tier':{'value':'Start'},'kit_tier_summary':{'value':'Grunden: avfettning och handtvätt'},
  'kit_component_notes':{'value':['För asfalt, tjära och oljebaserad smuts. Används outspädd.','För trafikfilm, insekter och vägsmuts. Koncentrat som späds efter smutsgrad.','För själva handtvätten – skonsamt mot vax och keramiska lackskydd.']},
  'kit_card_line':{'value':'Grunden – avfettning och handtvätt.'}})
foam=kit(202,'Foam Wash Kit','foam-wash-kit',46900,['foam','fc'],{'kit_eyebrow':{'value':'Exteriör · Foam'},'kit_name':{'value':'Foam Wash Kit'},'kit_display_title':{'value':'Foam Wash Kit'},'kit_tier':{'value':'Foam'},'kit_tier_summary':{'value':'Skumförtvätt med Foam Cannon'}})
komp=kit(203,'Exteriör Komplett Kit','exterior-komplett-kit',119900,['dd','alk','foam','pure','rev','cla','pri','gc'],{'kit_eyebrow':{'value':'Exteriör · Komplett'},'kit_name':{'value':'Exteriör Komplett Kit'},'kit_display_title':{'value':'Exteriör komplett kit'},'kit_tier':{'value':'Komplett'},'kit_tier_summary':{'value':'Hela utsidan, från förtvätt till finish'}})
for k in (start,foam,komp): k['metafields']['custom']['kit_family']={'value':[start,foam,komp]}
H=dict(P)
REVIEWS=[{'author':{'value':'Hyseni'},'rating':{'value':5},'title':{'value':'Produkterna var riktigt bra och lätta…'},'body':{'value':'Produkterna var riktigt bra och lätta att använda, kall- och alkaliska avfettningarna var riktigt bra för att få bort 150mils smuts från bilen, schampot gjorde bilen riktigt fin o blank med som dessutom skummade på bra och luktade riktigt gott! Rekommenderar starkt dessa produkter!'},'date':{'value':'9 september 2026'},'mentions':{'value':[P['alkastrike-alkalisk-avfettning'],P['deepdegrease-kallavfettning'],P['pure-shampoo-ph-neutralt-bilschampo']]}},
 {'author':{'value':'streamnight'},'rating':{'value':4},'title':{'value':'Fantastisk'},'body':{'value':'Snabb leverans till Gotland, en riktigt bra flygrostborttagare som gav ett fantastiskt resultat. Även en riktigt bra alkalisk avfättning.'},'date':{'value':'11 september 2026'},'mentions':{'value':[P['revolt-flygrostborttagare'],P['alkastrike-alkalisk-avfettning']]}},
 {'author':{'value':'Filip Am'},'rating':{'value':5},'title':{'value':'Produkterna gav ett resultat över min…'},'body':{'value':'Produkterna gav ett resultat över min förväntan. Fungerade utmärkt och simpelt att använda, samt sköna att hålla i när dem används.'},'date':{'value':'7 september 2026'},'mentions':{'value':[]}}]
snips={n:clean(open(R+'snippets/'+n+'.liquid').read()) for n in ['nr-kit-separate-total','nr-ks-separate','nr-ks-component','nr-pdp-stars','nr-kit-check']}
env=Environment(loader=DictLoader(snips))
def money(c):
    c=float(c); kr=int(c)//100; ore=int(round(c))%100
    return f"{kr:,}".replace(',',' ')+(f",{ore:02d}" if ore else '')+' kr'
env.filters['money']=money
env.filters['asset_url']=lambda s:'/'+s
env.filters['stylesheet_tag']=lambda s:''
env.filters['image_url']=lambda i,**k: (i or {}).get('src','') if isinstance(i,dict) else str(i)
env.filters['image_tag']=lambda u,**k: f'<img src="{u}" alt="{k.get("alt","")}" loading="lazy">'
env.filters['video_tag']=lambda v,**k: f'<video controls muted playsinline poster="{ph("Film",900,1125,"2b2b2b")["src"]}"></video>'
env.filters['payment_type_svg_tag']=lambda t,**k: f'<span class="pay">{t}</span>'
settings={'nr_trustpilot_rating':'4.7','nr_trustpilot_count':34,'nr_trustpilot_url':'https://se.trustpilot.com/review/nordicreflection.se','free_shipping_threshold':799,'delivery_time_text':'Leverans inom 1–3 arbetsdagar'}
def resolve(v):
    if isinstance(v,str) and v in H: return H[v]
    if isinstance(v,list): return [H.get(x,x) for x in v]
    return v
def render_kit(suffix, kitp):
    tpl=json.loads((lambda r:r[r.index('{'):])(open(R+f'templates/product.{suffix}.json').read()))
    pd=tpl['sections']['main']['blocks']['product-details']['blocks']
    ctx=dict(product=kitp,settings=settings,routes={'cart_add_url':'/cart/add'},shop={'metaobjects':{'nr_trustpilot_review':{'values':REVIEWS}},'enabled_payment_types':['visa','mastercard','klarna','apple_pay','swish']},cart={'taxes_included':True},request={'visual_preview_mode':False})
    def blk(name,bs):
        bs={k:resolve(v) for k,v in bs.items()}
        return env.from_string(clean(open(R+'blocks/'+name+'.liquid').read())).render(**ctx,closest={'product':kitp},block={'settings':bs,'shopify_attributes':''})
    def sec(s,sid):
        ss={k:resolve(v) for k,v in s.get('settings',{}).items()}
        for k in ('alternative','products'): ss.setdefault(k,'')
        bl=[{'settings':{k:resolve(v) for k,v in s['blocks'][b]['settings'].items()},'shopify_attributes':''} for b in s.get('block_order',[])]
        return env.from_string(clean(open(R+'sections/'+s['type']+'.liquid').read())).render(**ctx,section={'settings':ss,'blocks':bl,'id':sid})
    intro=blk('nr-ks-intro',pd['intro']['settings'])
    delivery=blk('nr-pdp-delivery',pd['delivery']['settings'])
    buy='''<div class="buy"><div class="qty"><button aria-label="Minska">−</button><span>1</span><button aria-label="Öka">+</button></div>
<product-form-component><button ref="addToCartButton" class="button add-to-cart-button" onclick="window.__atc=(window.__atc||0)+1">Lägg paketet i varukorgen</button></product-form-component>
<div class="shopify-payment-button"><button class="gpay">Köp med <b>Shop</b>Pay</button><a class="more" href="#">Fler betalningsalternativ</a></div></div>'''
    secs=''.join(f'<div class="shopify-section {"nr-pdp-shell" if tpl["sections"][k]["type"]=="nr-pdp-trust" else "nr-ks-shell"}">{sec(tpl["sections"][k],k)}</div>' for k in tpl['order'][1:])
    css=open(R+'assets/nr-pdp.css').read()+open(R+'assets/nr-kitsys.css').read()
    for n in ('nr-pdp-trust',):
        m=re.search(r'\{% stylesheet %\}(.*?)\{% endstylesheet %\}',open(R+f'sections/{n}.liquid').read(),re.S)
        if m: css+=m.group(1)
    title=kitp['title']
    html=f'''<!doctype html><html lang="sv"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{suffix}</title><style>
*{{box-sizing:border-box}} body{{margin:0;font-family:Inter,"Helvetica Neue",Arial,sans-serif;font-size:14px;color:#111;background:#fff;--font-heading--family:Inter,"Helvetica Neue",Arial,sans-serif;--font-heading--weight:600}}
.visually-hidden{{position:absolute;clip:rect(0 0 0 0);width:1px;height:1px;overflow:hidden}}
header.h{{position:sticky;top:0;z-index:5;height:64px;background:#fff;border-bottom:1px solid #eee;display:flex;align-items:center;justify-content:space-between;padding:0 20px;font-weight:700}}
.hero{{background:#f5f4f0}} .pi{{display:grid;gap:20px;max-width:1440px;margin:0 auto;padding:0 0 24px}}
@media(min-width:990px){{.pi{{grid-template-columns:minmax(0,58fr) minmax(0,42fr);gap:48px;padding:24px 40px}} .product-details{{position:sticky;top:88px;align-self:start}}}}
.gal img{{width:100%;display:block;aspect-ratio:1}}
.product-details{{padding:0 20px;max-width:34rem}} @media(min-width:990px){{.product-details{{padding:0}}}}
.product-details>*+*{{margin-top:20px}}
.buy{{display:flex;flex-direction:column;gap:10px}}
.qty{{display:inline-flex;align-items:center;gap:18px;border:1px solid #111;height:48px;padding:0 14px;width:max-content}} .qty button{{border:0;background:none;font-size:18px;width:24px}}
.button{{width:100%;background:#111;color:#fff;border:0;border-radius:14px;font-size:15px;min-height:52px}}
.gpay{{width:100%;height:48px;border-radius:14px;border:0;background:#5a31f4;color:#fff;font-size:15px}} .more{{display:block;text-align:center;font-size:13px;color:#111;margin-top:8px}}
.pay{{font-size:9px;border:1px solid #ccc;padding:2px 4px}}
.sticky{{position:fixed;left:8px;right:8px;bottom:calc(8px + env(safe-area-inset-bottom));display:flex;align-items:center;gap:10px;background:#fff;border:1px solid #ddd;border-radius:14px;padding:8px 8px 8px 14px;z-index:6;font-size:13px}} .sticky b{{flex:1}} .sticky button{{background:#111;color:#fff;border:0;border-radius:10px;height:40px;padding:0 14px}}
@media(min-width:750px){{.sticky{{display:none!important}}}}
footer{{height:160px;background:#111;margin-top:0}}
{css}</style></head><body><header class="h">NordicReflection<span>☰</span></header>
<div class="hero"><div class="pi"><div class="gal"><img alt="" src="{kitp['featured_image']['src']}"></div><div class="product-details">{intro}{buy}{delivery}</div></div></div>
{secs}<footer></footer>
<div class="sticky" id="sticky" style="display:none"><b>{title}<br>{money(kitp['price'])}</b><button>Lägg i varukorgen</button></div>
<script>const s=document.getElementById('sticky'),b=document.querySelector('.add-to-cart-button');new IntersectionObserver(([e])=>{{s.style.display=(e.isIntersecting||e.boundingClientRect.top>0)?'none':'flex'}}).observe(b);
document.addEventListener('submit',e=>{{if(e.target.hasAttribute('data-nr-ks-final')){{e.preventDefault();b.click();}}}});</script>
</body></html>'''
    os.makedirs('out',exist_ok=True); open(f'out/{suffix}.html','w').write(html)
if __name__=='__main__':
    render_kit('kit-exteriorstart',start); print('ok')
