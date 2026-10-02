import re, json, os, sys
from liquid import Environment, DictLoader
R='/home/user/shopify/'
def clean(s):
    for t in ('doc','schema','stylesheet','javascript'):
        s=re.sub(r'\{%%-?\s*%s\s*-?%%\}.*?\{%%-?\s*end%s\s*-?%%\}'%(t,t),'',s,flags=re.S)
    s=re.sub(r'\{%-?\s*#[^%]*%\}','',s); s=re.sub(r'(?m)^\s*#.*$','',s)
    return s
def ph(name,w=600,h=600,c='f1efe9'):
    name=name.replace('&','och')
    return {'src':f"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='{w}' height='{h}' viewBox='0 0 {w} {h}'><rect width='100%' height='100%' fill='%23{c}'/><rect x='38%' y='14%' width='24%' height='64%' rx='10' fill='%23cfcbc1'/><text x='50%' y='90%' font-size='{int(w/18)}' text-anchor='middle' font-family='sans-serif' fill='%23555'>{name}</text></svg>"}
vid={'media_type':'video'}
PRODUCTS=[ # pid, title, handle, price(öre), type_label, has_video, variants
 (1,'Core APC – Allrengöring (APC)','core-apc-allrengoring',15900,'Allrengöring (APC)',1,1),
 (2,'Scrub Pad','scrub-pad-interior',3900,'Rengöringspad för interiör',0,1),
 (3,'Mikrofiberduk','mikrofiberduk',4900,'Mikrofiberduk',0,3),
 (4,'Detail Brush Duo – 2-pack','detail-brush',13900,'Detaljborstar, 2-pack',0,1),
 (5,'Clarity – Glasrengöring','clarity-glasrengoring',14900,'Glasrengöring',0,1),
 (6,'Glass Towel – Glasduk','glass-towel-glasduk',6900,'Glasduk',0,1),
 (7,'Revolt – Flygrostborttagare','revolt-flygrostborttagare',18900,'Flygrostborttagare',1,1),
 (8,'Mikrofiber Fälgborste','mikrofiber-falgborste',18900,'Fälgborste i mikrofiber',1,1),
 (9,'Pristine - Däck- & Plastförnyare','pristine-dack-plastfornyare',18900,'Däck- och plastförnyare',1,1),
 (10,'Däckapplikator','dackapplikator',4000,'Applikator för däckglans',0,1),
 (11,'DeepDegrease – Kallavfettning','deepdegrease-kallavfettning',16900,'Kallavfettning',0,1),
 (12,'Alkastrike – Alkalisk Avfettning','alkastrike-alkalisk-avfettning',14900,'Alkalisk förtvätt',1,1),
 (13,'Pure Shampoo – Bilschampo','pure-shampoo-ph-neutralt-bilschampo',17900,'Bilschampo för kontaktvätt',1,1),
 (14,'Foamtastic – Snow Foam för effektiv förtvätt','foamtastic-hogkoncentrerat-snow-foam',16900,'Snow foam / förtvätt',1,1),
 (15,'Foam Cannon','foam-lance-skumlans',39900,'Foam cannon / skumkanon',0,1),
 (16,'GlossCoat – Sprayförsegling','glosscoat-hydrofobisk-sprayforsegling',18900,'Sprayförsegling',1,1),
]
P={}
for pid,t,h,pr,tl,v,nv in PRODUCTS:
    P[h]={'id':pid,'title':t,'handle':h,'url':'/products/'+h,'price':pr,'featured_image':ph(t.split(' –')[0].split(' -')[0]),'variants':list(range(nv)),
          'metafields':{'pdp':{'type_label':{'value':tl},'demo_media':{'value':[vid] if v else []}},'custom':{}}}
def comp(h,size,price=None):
    p=P[h]; v={'id':1000+p['id'],'price':price or p['price'],'product':p,'image':None,'url':p['url']+'?variant=5'}
    return {'variant':{'value':v},'quantity':{'value':1},'size':{'value':size or None},'purpose':{'value':'generic purpose'},'role':{'value':''}}
C={'apc':comp('core-apc-allrengoring','500 ml'),'scrub':comp('scrub-pad-interior',''),'duk':comp('mikrofiberduk','5-pack',11900),
   'brush':comp('detail-brush','2-pack'),'cla':comp('clarity-glasrengoring','500 ml'),'towel':comp('glass-towel-glasduk',''),
   'rev':comp('revolt-flygrostborttagare','500 ml'),'wb':comp('mikrofiber-falgborste',''),'pri':comp('pristine-dack-plastfornyare','500 ml'),
   'app':comp('dackapplikator',''),'dd':comp('deepdegrease-kallavfettning','1000 ml'),'alk':comp('alkastrike-alkalisk-avfettning','500 ml'),
   'pure':comp('pure-shampoo-ph-neutralt-bilschampo','500 ml'),'foam':comp('foamtastic-hogkoncentrerat-snow-foam','1000 ml'),
   'fc':comp('foam-lance-skumlans',''),'gc':comp('glosscoat-hydrofobisk-sprayforsegling','500 ml')}
KITS=[ # suffix, pid, title, handle, price, comps, eyebrow, tagline, value_points
 ('interiorlitet',15996560376142,'Litet interiör Startkit','interiorpaket-grundlaggande-interiorvard',25900,'apc scrub duk','Interiör · Litet','Det viktigaste för en enkel och effektiv rengöring av bilens interiör.'),
 ('interiormellan',16015851487566,'Mellan interiör Startkit','mellan-interior-startkit',36900,'apc scrub duk brush','Interiör · Mellan','Rengör både större ytor och de minsta detaljerna i kupén.'),
 ('interiorstort',16015857221966,'Stort interiör Startkit','stort-interior-startkit',54900,'apc scrub duk brush cla towel','Interiör · Komplett','För dig som vill rengöra hela kupén själv – ytor, detaljer och glas.'),
 ('falgstart',16016364077390,'Fälg startkit','falg-startkit',30900,'rev wb','Fälgar · Start','En enkel kombination för att lösa bromsdamm och järnpartiklar på fälgarna.'),
 ('falgdack',16016378134862,'Fälg Och Däck Komplett Kit','falg-och-dack-komplett-kit',49900,'rev wb pri app','Fälgar & däck · Komplett','Rengör, detaljera och ge däcken finish med en komplett rutin för hjulen.'),
 ('exteriorstart',16018450940238,'Exteriör Startkit','litet-exterior-startkit',42900,'dd alk pure','Exteriör · Start','För dig som vill få grunden rätt – från avfettning till handtvätt.'),
 ('foamwash',16016437608782,'Foam Wash Kit','foam-wash-kit',46900,'foam fc','Exteriör · Foam','Foam Cannon och Foamtastic i en färdig setup för skumförtvätten.'),
 ('exteriorkomplett',16018547671374,'Exteriör Komplett Kit','exterior-komplett-kit',119900,'dd alk foam pure rev cla pri gc','Exteriör · Komplett','Allt du behöver för en komplett utvändig tvätt – från grovsmuts till färdig finish.'),
]
MF=json.load(open(R+'docs/kits/rollout/metafields.json'))
STORT_MF={'kit_display_title':'Stort interiörkit','kit_descriptor':'6 produktgrupper, inklusive 5 mikrofiberdukar och 2 detaljborstar',
 'kit_value_points':['Core APC 500 ml – koncentrat som späds efter behov','Verktyg för både större ytor och trånga detaljer','Clarity 500 ml och Glass Towel för rutor och speglar'],
 'kit_component_notes':['För plast, vinyl, textil och gummi. Späds efter smutsgrad enligt etiketten.','Bearbetar ingrodd smuts på plast, vinyl, gummi och textil.','För avtorkning efter rengöringen.','Mjuka borstar för luftventiler, knappar och trånga detaljer.','För in- och utvändigt glas. Invändigt sprayar du på duken, inte på rutan.','Eftertorkar glaset för en klar finish.'],
 'kit_faq':'Vad behöver jag ha hemma? | En tom sprayflaska och vatten för att späda Core APC efter smutsgrad enligt etiketten. Clarity levereras i sprayflaska.\nHur späder jag Core APC? | Efter smutsgrad och yta enligt produktetiketten – svagare för underhåll, starkare för kraftig smuts.\nVilka ytor kan jag rengöra? | Core APC är avsedd för plast, vinyl, textil och gummi. Testa alltid på en liten, mindre synlig yta först och följ produktetiketten.\nHur rengör jag rutorna invändigt? | Spraya Clarity på en ren duk istället för direkt på glaset, torka med en ren mikrofiberduk och eftertorka med Glass Towel.\nVad skiljer Stort från Mellan interiörkit? | Stort innehåller även Clarity glasrengöring och Glass Towel. Övrigt innehåll är detsamma.'}
K={}
for suf,pid,title,h,price,comps,eb,tag in KITS:
    md={'kit_components':{'value':[C[c] for c in comps.split()]},'kit_eyebrow':{'value':eb},'kit_tagline':{'value':tag},'kit_value_points':{'value':['legacy point']}}
    for m in MF:
        if m['ownerId'].endswith(str(pid)):
            v=m['value']; md[m['key']]={'value':json.loads(v) if m['type'].startswith('list') else v}
    if suf=='interiorstort':
        for k,v in STORT_MF.items(): md[k]={'value':v}
    K[suf]={'id':pid,'title':title,'handle':h,'url':'/products/'+h,'price':price,'available':True,'featured_image':ph(title,1254,1254,'ece9e2'),
            'selected_or_first_available_variant':{'price':price},'metafields':{'custom':md},'suffix':suf}
H={**P, **{k['handle']:k for k in K.values()}}
env=Environment(loader=DictLoader({n:clean(open(R+'snippets/'+n+'.liquid').read()) for n in ['nr-kit-separate-total','nr-kit-check']}))
def money(c):
    c=float(c); kr=int(c)//100; ore=int(round(c))%100
    s=f"{kr:,}".replace(',',' ')
    return s+(f",{ore:02d}" if ore else '')+' kr'
env.filters['money']=money
env.filters['asset_url']=lambda s:'/'+s
env.filters['stylesheet_tag']=lambda s:''
env.filters['image_url']=lambda i,**k: (i or {}).get('src','') if isinstance(i,dict) else str(i)
env.filters['image_tag']=lambda u,**k: f'<img src="{u}" alt="" loading="lazy">'
settings={'nr_trustpilot_rating':'4.7','nr_trustpilot_url':'https://se.trustpilot.com/review/nordicreflection.se','free_shipping_threshold':799,'delivery_time_text':'Leverans inom 1–3 arbetsdagar'}
base=open('orig/assets/base.css').read()
sec_css=base[base.index('/* Set up page widths & margins */'):base.index('/* For full-width sections with margin')]
css=open(R+'assets/nr-kitpage.css').read()
def resolve(v):
    if isinstance(v,str) and v in H: return H[v]
    if isinstance(v,list): return [H.get(x,x) for x in v]
    return v
os.makedirs('out',exist_ok=True)
for suf,kit in K.items():
    vh=None
    tpl=json.loads((lambda r:r[r.index('{'):])(open(R+f'templates/product.kit-{suf}.json').read()))
    pd=tpl['sections']['main']['blocks']['product-details']['blocks']
    def blk(name,bs):
        return env.from_string(clean(open(R+'blocks/'+name+'.liquid').read())).render(closest={'product':kit},product=kit,block={'settings':bs,'shopify_attributes':''},settings=settings)
    def sec(s):
        ss={k:resolve(v) for k,v in s.get('settings',{}).items()}
        bl=[{'settings':{k:resolve(v) for k,v in s['blocks'][b]['settings'].items()},'shopify_attributes':''} for b in s.get('block_order',[])]
        [ss.setdefault(k,'') for k in ('alternative','alternative_2','video_product')]
        vname=(ss.get('video_heading') or 'film')
        env.filters['video_tag']=lambda v,**k: f'<video controls poster="{ph(vname,1280,720,"2b2b2b")["src"]}"></video>'
        return env.from_string(clean(open(R+'sections/'+s['type']+'.liquid').read())).render(product=kit,section={'settings':ss,'blocks':bl,'id':'x'},settings=settings)
    col=blk('nr-kitpage-summary',pd['summary']['settings'])+'''<div class="product-form-buttons product-form-buttons--stacked">
<div class="qty"><button aria-label="Minska">−</button><span>1</span><button aria-label="Öka">+</button></div>
<button class="button add-to-cart-button">Lägg kitet i varukorgen</button>
<div class="shopify-payment-button"><button class="gpay">Köp med <b>Shop</b>Pay</button><a class="more" href="#">Fler betalningsalternativ</a></div></div>'''+blk('nr-kitpage-points',{})+blk('nr-kitpage-meta',{})
    secs=''.join(f'<div class="shopify-section">{sec(tpl["sections"][k])}</div>' for k in tpl['order'][1:])
    html=f'''<!doctype html><html lang="sv"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{suf}</title><style>
*{{box-sizing:border-box}} body{{margin:0;font-family:Inter,system-ui,sans-serif;color:#111;--font-heading--family:Inter,system-ui,sans-serif;--narrow-page-width:90rem;--normal-page-width:120rem;--normal-content-width:48rem}}
{sec_css}
.visually-hidden{{position:absolute;clip:rect(0 0 0 0);width:1px;height:1px;overflow:hidden}}
header.h{{position:sticky;top:0;z-index:5;height:64px;background:#fff;border-bottom:1px solid #eee;display:flex;align-items:center;justify-content:space-between;padding:0 16px;font-weight:700}}
.pi{{display:grid;gap:24px;padding-block:8px 8px}}
@media(min-width:750px){{.pi{{grid-template-columns:1fr 1fr;gap:48px;padding-block:24px}} .product-details{{position:sticky;top:88px;align-self:start}}}}
.gal img{{width:100%;display:block;aspect-ratio:1}}
.product-details{{display:flex;flex-direction:column;gap:20px}}
.product-form-buttons{{display:flex;flex-direction:column}}
.qty{{display:inline-flex;align-items:center;gap:18px;border:1px solid #ccc;border-radius:14px;height:48px;padding:0 14px;width:max-content}} .qty button{{border:0;background:none;font-size:18px;width:24px}}
.button{{background:#000;color:#fff;border:0;border-radius:14px;font-size:15px;min-height:48px}}
.product-form-buttons--stacked{{gap:10px}}
.gpay{{width:100%;height:48px;border-radius:14px;border:0;background:#5a31f4;color:#fff;font-size:15px}} .more{{display:block;text-align:center;font-size:13px;color:#111;margin-top:8px}}
.sticky{{position:fixed;left:8px;right:8px;bottom:8px;display:flex;align-items:center;gap:10px;background:#fff;border:1px solid #ddd;border-radius:14px;padding:8px;z-index:6}} .sticky b{{flex:1;font-size:13px}} .sticky button{{background:#000;color:#fff;border:0;border-radius:10px;height:40px;padding:0 14px}}
@media(min-width:750px){{.sticky{{display:none}}}}
{css}</style></head><body class="page-width-narrow"><header class="h">NordicReflection<span>☰ 🛒</span></header>
<div class="shopify-section"><div class="section section--page-width"><div class="pi"><div class="gal"><img src="{kit['featured_image']['src']}"></div><div class="product-details">{col}</div></div></div></div>
{secs}
<footer style="height:200px;background:#111;margin-top:40px"></footer>
<div class="sticky" id="sticky" hidden style="display:none"><b>{kit['title']}<br>{money(kit['price'])}</b><button>Lägg i varukorgen</button></div>
<script>const s=document.getElementById('sticky'),b=document.querySelector('.add-to-cart-button');new IntersectionObserver(([e])=>{{s.hidden=e.isIntersecting||e.boundingClientRect.top>0;s.style.display=s.hidden?'none':''}}).observe(b);</script>
</body></html>'''
    open(f'out/{suf}.html','w').write(html)
print('ok', len(K))
