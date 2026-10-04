"""Local render harness for the NR collection pages (sections/nr-shop, nr-kit-hub).
Real section/snippet code + real product copy (docs/collections/content-source.py);
Shopify's filter objects are mocked faithfully enough to click through states."""
import re, json, os, sys, importlib.util, urllib.parse
from liquid import Environment, DictLoader
R='/home/user/shopify/'
spec=importlib.util.spec_from_file_location('cs', R+'docs/collections/content-source.py'); cs=importlib.util.module_from_spec(spec); spec.loader.exec_module(cs)

def clean(s):
    for t in ('doc','schema','stylesheet','javascript','comment'):
        s=re.sub(r'\{%%-?\s*%s\s*-?%%\}.*?\{%%-?\s*end%s\s*-?%%\}'%(t,t),'',s,flags=re.S)
    s=re.sub(r'\{%-?\s*#[^%]*%\}','',s); s=re.sub(r'(?m)^\s*#.*$','',s)
    s=re.sub(r'\{%-?\s*paginate[^%]*%\}','',s); s=re.sub(r'\{%-?\s*endpaginate\s*-?%\}','',s)
    return s

COL={'2a2a2a':0}
def ph(name,bg='f1f0ec',col='3a3a3a',w=600,h=600):
    n=name.replace('&','och')
    return {'src':f"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='{w}' height='{h}' viewBox='0 0 {w} {h}'><rect width='100%' height='100%' fill='%23{bg}'/><rect x='40%' y='16%' width='20%' height='62%' rx='10' fill='%23{col}'/><text x='50%' y='90%' font-size='{int(w/22)}' text-anchor='middle' font-family='sans-serif' fill='%23888'>{n[:24]}</text></svg>"}

# id -> handle, title, price (öre), variants
META={
 '15963399553358':('revolt-flygrostborttagare','Revolt – Flygrostborttagare',18900,1,'5a3a5a'),
 '15959788814670':('alkastrike-alkalisk-avfettning','Alkastrike – Alkalisk Avfettning',14900,1,'3a5a3a'),
 '15963418362190':('deepdegrease-kallavfettning','DeepDegrease – Kallavfettning',16900,1,'2b2b2b'),
 '15963388379470':('foamtastic-hogkoncentrerat-snow-foam','Foamtastic – Snow Foam för effektiv förtvätt',16900,1,'9fb3bd'),
 '15963382055246':('pure-shampoo-ph-neutralt-bilschampo','Pure Shampoo – Bilschampo',17900,1,'c9c2b0'),
 '15963394867534':('glosscoat-hydrofobisk-sprayforsegling','GlossCoat – Sprayförsegling',18900,1,'303030'),
 '15963424031054':('clarity-glasrengoring','Clarity – Glasrengöring',14900,1,'a9c4d0'),
 '15963415740750':('pristine-dack-plastfornyare','Pristine - Däck- & Plastförnyare',18900,1,'c9a3b3'),
 '15963421442382':('core-apc-allrengoring','Core APC – Allrengöring (APC)',15900,1,'7a7a7a'),
 '15963468333390':('scrub-pad-interior','Scrub Pad',3900,1,'b0a080'),
 '16015861219662':('detail-brush','Detail Brush Duo – 2-pack',13900,1,'806040'),
 '15963505688910':('mikrofiberduk','Mikrofiberduk',4900,3,'6080a0'),
 '16015909454158':('glass-towel-glasduk','Glass Towel – Glasduk',6900,1,'4080a0'),
 '15996560376142':('interiorpaket-grundlaggande-interiorvard','Litet interiör Startkit',25900,1,'555'),
 '16015851487566':('mellan-interior-startkit','Mellan interiör Startkit',36900,1,'555'),
 '16015857221966':('stort-interior-startkit','Stort interiör Startkit',54900,1,'555'),
 '15963462795598':('foam-lance-skumlans','Foam Cannon',39900,1,'777'),
 '15963460075854':('tryckspruta-2l-kemikalieresistent','Tryckspruta',29900,1,'444'),
 '15963482751310':('wash-pad-mikrofiber','Washpad',14900,1,'5070a0'),
 '15963454832974':('tvatthink-20l-grit-guard','Tvätthink',29900,1,'222'),
 '15963479048526':('mikrofiber-falgborste','Mikrofiber Fälgborste',18900,1,'888'),
 '16015891235150':('deepreach-wheel-brush','DeepReach Wheel Brush',16900,1,'333'),
 '15963484750158':('dackapplikator','Däckapplikator',4000,1,'999'),
 '15963493466446':('torkduk-70x90-1400gsm','Torkduk 70x90 - 1400 GSM',32900,1,'4a6a8a'),
 '15963500609870':('torkduk-50x80-1400gsm','Torkduk 50x80 - 1400 GSM',22900,1,'4a6a8a'),
 '15963501134158':('torkduk-40x40-1400gsm','Torkduk 40x40 - 1400 GSM',14900,1,'4a6a8a'),
}
FV={k:{'label':{'value':lab},'key':{'value':k}} for k,lab in []}
LABELS=dict(traffic_film='Trafikfilm',tar='Asfalt & tjära',iron='Flygrost & bromsdamm',foam='Foam',contact_wash='Handtvätt',protection='Skydd & glans',glass='Glas',tyres_trim='Däck & plast',
 int_surfaces='Ytor',int_stubborn='Ingrodd smuts',int_details='Detaljer & springor',int_wipe='Torka av',kits='Färdiga paket',
 acc_prewash='Förtvätt & applicering',acc_wheels='Fälgar & däck',acc_drying='Torkning',acc_interior='Interiör',acc_detailing='Detaljering',
 kind_chem='Kemikalier',kind_sprayer='Sprutor & skumkanon',kind_brush='Borstar',kind_pad='Pads',kind_towel='Dukar',kind_bucket='Hinkar',kind_applicator='Applikatorer',kind_kit='Paket')
mo=lambda k:{'label':{'value':LABELS[k]},'key':{'value':k}}
P={}
for pid,name,line,ext,inte,acc,kind,label in cs.P:
    h,t,price,nv,col=META[pid]
    p={'id':pid,'handle':h,'title':t,'url':'/products/'+h,'price':price,'price_varies':nv>1,'available':True,'has_only_default_variant':nv==1,
       'selected_or_first_available_variant':{'id':'9'+pid,'price':price,'available':True,'title':'Default Title' if nv==1 else '1'},
       'featured_image':ph(name,col=col),
       'metafields':{'nrc':{'card_name':{'value':name},'card_line':{'value':line},'card_label':{'value':label or ''},
            'intent_exterior':{'value':[mo(x) for x in ext] or None},'intent_interior':{'value':[mo(x) for x in inte] or None},
            'intent_accessories':{'value':[mo(x) for x in acc] or None},'product_kind':{'value':mo(kind)},'pairs_with':{'value':None}},
            'custom':{}},'_intents':{'exterior':ext,'interior':inte,'accessories':acc},'_kind':kind}
    P[pid]=p
for a,b in cs.PAIRS.items(): P[a]['metafields']['nrc']['pairs_with']['value']=P[b]
H={p['handle']:p for p in P.values()}
# kits not in cs.P
class PList(list):
    @property
    def count(self): return len(self)
def comp(h,q=1,size=None): return {'variant':{'value':{'id':'9'+H[h]['id'],'price':H[h]['price'],'product':H[h]}},'quantity':{'value':q},'size':{'value':size},'label':{'value':H[h]['metafields']['nrc']['card_name']['value']}}
def kit(h,t,price,tier,summary,who,comps,adjust=None,name=None):
    k={'id':'k'+h,'handle':h,'title':t,'url':'/products/'+h,'price':price,'available':True,'has_only_default_variant':True,
       'selected_or_first_available_variant':{'id':'9k'+h,'price':price,'available':True},'featured_image':ph(t,'f1f0ec','555',600,600),
       'metafields':{'custom':{'kit_components':{'value':comps},'kit_name':{'value':name or t},'kit_tier':{'value':tier},'kit_tier_summary':{'value':summary},
          'kit_card_line':{'value':who},'kit_separate_adjust':{'value':adjust}},'nrc':H.get(h,{}).get('metafields',{}).get('nrc',{})}}
    if h in H: H[h]['metafields']['custom']=k['metafields']['custom']; return H[h]
    H[h]=k; return k
# mikrofiberduk 5-pack variant price 119
def mf5(): return {'variant':{'value':{'id':'9mf5','price':11900,'product':H['mikrofiberduk']}},'quantity':{'value':1},'size':{'value':'5-pack'}}
kit('interiorpaket-grundlaggande-interiorvard','Litet interiör Startkit',25900,'Bas','Ytorna i kupén','Det viktigaste: allrengöring, skrubb och dukar.',[comp('core-apc-allrengoring'),comp('scrub-pad-interior'),mf5()],name='Litet Interiör Startkit')
kit('mellan-interior-startkit','Mellan interiör Startkit',36900,'Detalj','Ytor och detaljer','Som Litet, plus borstar för ventiler och detaljer.',[comp('core-apc-allrengoring'),comp('scrub-pad-interior'),mf5(),comp('detail-brush')],name='Mellan Interiör Startkit')
kit('stort-interior-startkit','Stort interiör Startkit',54900,'Komplett','Ytor, detaljer och glas','Som Mellan, plus Clarity och glasduk för rutorna.',[comp('core-apc-allrengoring'),comp('scrub-pad-interior'),mf5(),comp('detail-brush'),comp('clarity-glasrengoring'),comp('glass-towel-glasduk')],name='Stort Interiör Startkit')
kit('litet-exterior-startkit','Exteriör Startkit',42900,'Start','Grunden: avfettning och handtvätt','Grunden, avfettning och handtvätt.',[comp('deepdegrease-kallavfettning'),comp('alkastrike-alkalisk-avfettning'),comp('pure-shampoo-ph-neutralt-bilschampo')])
kit('foam-wash-kit','Foam Wash Kit',46900,'Foam','Skumförtvätt med Foam Cannon','För dig som vill bygga tvätten runt Foam Cannon.',[comp('foamtastic-hogkoncentrerat-snow-foam'),comp('foam-lance-skumlans')])
kit('exterior-komplett-kit','Exteriör Komplett Kit',119900,'Komplett','Hela utsidan, från förtvätt till finish','För dig som vill ha hela rutinen.',[comp(x) for x in ['deepdegrease-kallavfettning','alkastrike-alkalisk-avfettning','foamtastic-hogkoncentrerat-snow-foam','pure-shampoo-ph-neutralt-bilschampo','revolt-flygrostborttagare','clarity-glasrengoring','pristine-dack-plastfornyare','glosscoat-hydrofobisk-sprayforsegling']])
kit('falg-startkit','Fälg startkit',30900,'Fälg','Rena fälgar','För dig som vill ha rena fälgar.',[comp('revolt-flygrostborttagare'),comp('mikrofiber-falgborste')],adjust=56.7,name='Fälg Startkit')
kit('falg-och-dack-komplett-kit','Fälg Och Däck Komplett Kit',49900,'Fälg + däck','Rena fälgar och färdig däckfinish','För dig som vill ha hela hjulet klart.',[comp('revolt-flygrostborttagare'),comp('mikrofiber-falgborste'),comp('pristine-dack-plastfornyare'),comp('dackapplikator')],adjust=56.7,name='Fälg & Däck Komplett Kit')
for k in ['interiorpaket-grundlaggande-interiorvard','mellan-interior-startkit','stort-interior-startkit']:
    H[k]['metafields']['nrc']['product_kind']={'value':mo('kind_kit')}

COLLS={
 'exterior':('Exteriör',[cs_id for cs_id in cs.ORDER['exterior']],'intent_exterior','exterior'),
 'interior':('Interiör',cs.ORDER['interior'],'intent_interior','interior'),
 'accessories':('Tillbehör',cs.ORDER['accessories'],'intent_accessories','accessories'),
 'all':('Products',list(P.keys()),None,None),
}

def money(c):
    c=float(c); kr=int(c)//100; ore=int(round(c))%100
    return f"{kr:,}".replace(',',' ')+(f",{ore:02d}" if ore else '')+' kr'
snips={}
for f in os.listdir(R+'snippets'):
    if f.startswith('nr-') and f.endswith('.liquid'): snips[f[:-7]]=clean(open(R+'snippets/'+f).read())
env=Environment(loader=DictLoader(snips))
env.filters['money']=money
env.filters['standard_event_data']=lambda c,*a:'{}'
env.filters['asset_url']=lambda s:'/'+s
env.filters['stylesheet_tag']=lambda s:''
env.filters['image_url']=lambda i,**k:(i or {}).get('src','') if isinstance(i,dict) else str(i)
env.filters['image_tag']=lambda u,**k:f'<img src="{u}" alt="{k.get("alt","")}" width="600" height="600" loading="lazy">'
env.filters['url_encode']=lambda s:urllib.parse.quote_plus(str(s))
env.filters['handleize']=lambda s:str(s).lower().replace(' ','-')
env.filters['default_pagination']=lambda *a,**k:''
settings={'nr_trustpilot_rating':'4.7','nr_trustpilot_url':'#','free_shipping_threshold':799}

def build_filter(base,param,label,keyfn,prods,active):
    vals=[]; seen={}
    for p in prods:
        for k in keyfn(p):
            seen.setdefault(k,0)
    for k in seen:
        is_active = k in active
        # count = products matching this value given the OTHER active values (approx: all prods)
        cnt=sum(1 for p in prods if k in keyfn(p))
        others=[a for a in active if a!=k]
        q='&'.join(f'{param}={a}' for a in (others if is_active else active+[k]))
        vals.append({'label':LABELS[k],'value':k,'param_name':param,'active':is_active,'count':cnt,
                     'url_to_remove':base+('?'+'&'.join(f'{param}={a}' for a in others) if others else ''),
                     'url_to_add':base+'?'+q})
    av=[v for v in vals if v['active']]
    return {'param_name':param,'label':label,'type':'list','values':vals,'active_values':av,'url_to_remove':base}

def render_collection(handle, active_intent=[], active_kind=[], sort='manual'):
    title,order,ikey,group=COLLS[handle]
    base='/collections/'+handle
    allp=[P[i] if i in P else H.get(i) for i in order]
    allp=[p for p in allp if p]
    # kits in interior order use H
    if handle=='interior':
        allp=[P[i] if i in P else None for i in order]
        allp=[p for p in allp if p] + [H['interiorpaket-grundlaggande-interiorvard'],H['mellan-interior-startkit'],H['stort-interior-startkit']]
        allp=[p for p in allp if p['handle'] not in ('interiorpaket-grundlaggande-interiorvard','mellan-interior-startkit','stort-interior-startkit')] + [H['interiorpaket-grundlaggande-interiorvard'],H['mellan-interior-startkit'],H['stort-interior-startkit']]
    def intents(p):
        if handle=='interior' and p['handle'] in ('interiorpaket-grundlaggande-interiorvard','mellan-interior-startkit','stort-interior-startkit'): return ['kits']
        return p.get('_intents',{}).get(group,[]) if group else []
    kinds=lambda p:[p.get('_kind','kind_kit')]
    filt=allp
    if active_intent: filt=[p for p in filt if set(intents(p))&set(active_intent)]
    if active_kind: filt=[p for p in filt if set(kinds(p))&set(active_kind)]
    filters=[]
    if ikey: filters.append(build_filter(base,'filter.p.m.nrc.'+ikey,'Vad?',intents,allp,list(active_intent)))
    filters.append(build_filter(base,'filter.p.m.nrc.product_kind','Produkttyp',kinds,allp,list(active_kind)))
    coll={'handle':handle,'title':title,'url':base,'description':'','products':filt,'products_count':len(filt),'all_products_count':len(allp),
          'filters':filters,'sort_by':sort if sort!='manual' else '','default_sort_by':'manual',
          'sort_options':[{'value':v,'name':v} for v in ['manual','best-selling','title-ascending','price-ascending','price-descending','created-descending']]}
    tpl=json.load(open(R+f'templates/collection.{handle}.json' if handle!='all' else R+'templates/collection.json'))
    return render_section(tpl,coll)

def resolve(v):
    if isinstance(v,str) and v in H: return H[v]
    if isinstance(v,list) and v and all(isinstance(x,str) and x in H for x in v): return PList([H[x] for x in v])
    if isinstance(v,str) and v in ('exterior','interior','accessories','fardiga-paket'):
        return {'title':{'exterior':'Exteriör','interior':'Interiör','accessories':'Tillbehör','fardiga-paket':'Färdiga paket'}[v],'url':'/collections/'+v,'products_count':{'exterior':8,'interior':9,'accessories':14,'fardiga-paket':8}[v]}
    if isinstance(v,str) and v.startswith('shopify://collections/'): return '/collections/'+v.split('/')[-1]
    return v

def render_section(tpl,coll):
    s=tpl['sections']['main']; typ=s['type']
    src=open(R+f'sections/{typ}.liquid').read()
    ss={k:(resolve(v) if k.startswith('continue_') or k in ('product',) else v) for k,v in s['settings'].items()}
    bl=[]
    for bk in s['block_order']:
        b=s['blocks'][bk]; bs={k:(resolve(v) if k.startswith('product') or k=='kits' or k=='link_url' or k=='url' else v) for k,v in b['settings'].items()}
        for k in ['eyebrow','text','link_label','link_url','show_for_intent','product_3','text_3','hash','question']: bs.setdefault(k,'')
        bl.append({'type':b['type'],'id':bk,'settings':bs,'shopify_attributes':''})
    for k in ['eyebrow','heading','intro','intent_filter','chip_order','drawer_filters','continue_1','continue_2','continue_3','card_intent']: ss.setdefault(k,'')
    body=clean(src)
    html=env.from_string(body).render(section={'settings':ss,'blocks':bl,'id':'main'},collection=coll,settings=settings,request={'design_mode':False},paginate={'pages':1},shop={'metaobjects':{}},routes={})
    return html

def page(html, css_extra=''):
    css=open(R+'assets/nr-homepage.css').read()+open(R+'assets/nr-shop.css').read()
    js=open(R+'assets/nr-shop.js').read()
    return f'''<!doctype html><html lang="sv"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>*{{box-sizing:border-box}} body{{margin:0;font-family:Inter,Arial,sans-serif;color:#111;--font-heading--family:Inter,Arial,sans-serif}} .visually-hidden{{position:absolute;clip:rect(0 0 0 0);width:1px;height:1px;overflow:hidden}} header.h{{height:60px;background:#fff;border-bottom:1px solid #eee;display:flex;align-items:center;padding:0 16px;font-weight:700}}{css}</style></head><body><header class="h">NordicReflection</header><main>{html}</main><footer style="height:160px;background:#111"></footer><script type="module">{js}</script></body></html>'''

if __name__=='__main__':
    os.makedirs('out',exist_ok=True)
    for h,(title,order,ikey,group) in COLLS.items():
        open(f'out/{h}.html','w').write(page(render_collection(h)))
        if group:
            vals=set()
            for p in P.values():
                for k in p['_intents'].get(group,[]): vals.add(k)
            if h=='interior': vals.add('kits')
            for v in vals:
                open(f'out/{h}--{v}.html','w').write(page(render_collection(h,[v])))
        for kd in ['kind_towel','kind_brush']:
            open(f'out/{h}--kind--{kd}.html','w').write(page(render_collection(h,[],[kd])))
    open('out/empty.html','w').write(page(render_collection('accessories',['acc_drying'],['kind_brush'])))
    tpl=json.load(open(R+'templates/collection.kits.json'))
    open('out/fardiga-paket.html','w').write(page(render_section(tpl,{'handle':'fardiga-paket','title':'Färdiga paket','url':'/collections/fardiga-paket','description':''})))
    print('ok')
