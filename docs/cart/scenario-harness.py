import re, json, html as H
from liquid import Environment
R='/home/user/shopify/'
src=open(R+'snippets/nr-cart-next-step.liquid').read()
src_clean=re.sub(r'\{%-?\s*(doc|stylesheet)\s*-?%\}.*?\{%-?\s*end\1\s*-?%\}','',src,flags=re.S)
src_clean=re.sub(r'(?m)^\s*#.*$','',src_clean)
css=re.search(r'\{% stylesheet %\}(.*?)\{% endstylesheet %\}',src,re.S).group(1)
env=Environment()
def money(c):
    c=float(c); kr=int(c)//100; ore=int(round(c))%100
    return f"{kr:,}".replace(',',' ')+(f",{ore:02d}" if ore else '')+' kr'
env.filters['money']=money
env.filters['asset_url']=lambda s:'/'+s
def ph(n): 
    n=n.replace('&','och')
    return {'src':f"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='160' height='160'><rect width='100%' height='100%' fill='%23eee'/><text x='50%' y='55%' font-size='14' text-anchor='middle' fill='%23555'>{n[:10]}</text></svg>"}
env.filters['image_url']=lambda i,**k: i['src'] if isinstance(i,dict) else ''
env.filters['image_tag']=lambda u,**k: f'<img src="{u}" alt="">'
P={}
def prod(h,t,price,variants=1,available=True,comps=None):
    v=[{'id':abs(hash(h))%10**8+i,'price':price,'available':available} for i in range(variants)]
    p={'handle':h,'title':t,'price':price,'available':available,'url':'/products/'+h,'featured_image':ph(t),'variants':v,'selected_or_first_available_variant':v[0],
       'metafields':{'custom':{'kit_components':{'value':[]}}}}
    P[h]=p; return p
for h,t,pr in [('revolt-flygrostborttagare','Revolt – Flygrostborttagare',18900),('mikrofiber-falgborste','Mikrofiber Fälgborste',18900),
 ('pristine-dack-plastfornyare','Pristine - Däck- & Plastförnyare',18900),('dackapplikator','Däckapplikator',4000),('clarity-glasrengoring','Clarity – Glasrengöring',14900),
 ('glass-towel-glasduk','Glass Towel – Glasduk',6900),('core-apc-allrengoring','Core APC – Allrengöring (APC)',15900),('scrub-pad-interior','Scrub Pad',3900),
 ('pure-shampoo-ph-neutralt-bilschampo','Pure Shampoo – Bilschampo',17900),('wash-pad-mikrofiber','Washpad',14900),('foamtastic-hogkoncentrerat-snow-foam','Foamtastic – Snow Foam för effektiv förtvätt',16900),
 ('foam-lance-skumlans','Foam Cannon',39900),('deepdegrease-kallavfettning','DeepDegrease – Kallavfettning',16900),('alkastrike-alkalisk-avfettning','Alkastrike – Alkalisk Avfettning',14900),
 ('glosscoat-hydrofobisk-sprayforsegling','GlossCoat – Sprayförsegling',18900),('detail-brush','Detail Brush Duo – 2-pack',13900),('deepreach-wheel-brush','DeepReach Wheel Brush',16900)]:
    prod(h,t,pr)
prod('mikrofiberduk','Mikrofiberduk',4900,variants=3)
def kit(h,t,price,comps):
    p=prod(h,t,price); p['metafields']['custom']['kit_components']['value']=[{'variant':{'value':{'product':P[c]}}} for c in comps]
kit('interiorpaket-grundlaggande-interiorvard','Litet interiör Startkit',25900,['core-apc-allrengoring','scrub-pad-interior','mikrofiberduk'])
kit('mellan-interior-startkit','Mellan interiör Startkit',36900,['core-apc-allrengoring','scrub-pad-interior','mikrofiberduk','detail-brush'])
kit('stort-interior-startkit','Stort interiör Startkit',54900,['core-apc-allrengoring','scrub-pad-interior','mikrofiberduk','detail-brush','clarity-glasrengoring','glass-towel-glasduk'])
kit('falg-startkit','Fälg startkit',30900,['revolt-flygrostborttagare','mikrofiber-falgborste'])
kit('falg-och-dack-komplett-kit','Fälg Och Däck Komplett Kit',49900,['revolt-flygrostborttagare','mikrofiber-falgborste','pristine-dack-plastfornyare','dackapplikator'])
kit('litet-exterior-startkit','Exteriör Startkit',42900,['deepdegrease-kallavfettning','alkastrike-alkalisk-avfettning','pure-shampoo-ph-neutralt-bilschampo'])
kit('foam-wash-kit','Foam Wash Kit',46900,['foamtastic-hogkoncentrerat-snow-foam','foam-lance-skumlans'])
kit('exterior-komplett-kit','Exteriör Komplett Kit',119900,['deepdegrease-kallavfettning','alkastrike-alkalisk-avfettning','foamtastic-hogkoncentrerat-snow-foam','pure-shampoo-ph-neutralt-bilschampo','revolt-flygrostborttagare','clarity-glasrengoring','pristine-dack-plastfornyare','glosscoat-hydrofobisk-sprayforsegling'])
BXGY={'mikrofiber-falgborste':0.7}
def cart(*lines):
    handles=[h for h,q in lines]; items=[]
    for h,q in lines:
        p=P[h]; fp=p['price']
        if h in BXGY and 'revolt-flygrostborttagare' in handles: fp=int(round(fp*BXGY[h]))
        items.append({'product':p,'quantity':q,'final_price':fp,'variant':p['variants'][0]})
    return {'items':items,'item_count':sum(q for h,q in lines)}
def render(c, overrides=None, ctx='drawer'):
    ap=dict(P); 
    for k,v in (overrides or {}).items(): ap[k]=v
    return env.from_string(src_clean).render(cart=c, all_products=ap, context=ctx)
def summary(out):
    items=re.findall(r'<li class="nr-cart-next__item[^"]*">(.*?)</li>',out,re.S)
    res=[]
    for it in items:
        t=H.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',it))).strip()
        btn='add' if 'data-nr-cart-rec-add' in it else 'link'
        vid=re.search(r'data-variant-id="(\d+)"',it)
        res.append(f'[{btn}] {t}')
    return res
if __name__=='__main__':
    import copy
    soldout=copy.deepcopy(P['glass-towel-glasduk']); soldout['available']=False
    S=[('Tom korg',cart(),None),
       ('Revolt ensam',cart(('revolt-flygrostborttagare',1)),None),
       ('Revolt + fälgborste',cart(('revolt-flygrostborttagare',1),('mikrofiber-falgborste',1)),None),
       ('Revolt ×2',cart(('revolt-flygrostborttagare',2)),None),
       ('Fälg startkit',cart(('falg-startkit',1)),None),
       ('Fälg & Däck Komplett',cart(('falg-och-dack-komplett-kit',1)),None),
       ('Clarity ensam',cart(('clarity-glasrengoring',1)),None),
       ('Clarity + Glass Towel',cart(('clarity-glasrengoring',1),('glass-towel-glasduk',1)),None),
       ('Core APC ensam',cart(('core-apc-allrengoring',1)),None),
       ('Litet interiörkit',cart(('interiorpaket-grundlaggande-interiorvard',1)),None),
       ('Stort interiörkit',cart(('stort-interior-startkit',1)),None),
       ('Pure Shampoo ensam',cart(('pure-shampoo-ph-neutralt-bilschampo',1)),None),
       ('Exteriör startkit',cart(('litet-exterior-startkit',1)),None),
       ('Exteriör komplett',cart(('exterior-komplett-kit',1)),None),
       ('Foam Wash Kit',cart(('foam-wash-kit',1)),None),
       ('Foamtastic ensam',cart(('foamtastic-hogkoncentrerat-snow-foam',1)),None),
       ('Blandad: Clarity, Revolt, Pure, Core APC',cart(('clarity-glasrengoring',1),('revolt-flygrostborttagare',1),('pure-shampoo-ph-neutralt-bilschampo',1),('core-apc-allrengoring',1)),None),
       ('Revolt + DeepReach',cart(('revolt-flygrostborttagare',1),('deepreach-wheel-brush',1)),None),
       ('Clarity, Glass Towel slutsåld',cart(('clarity-glasrengoring',1)),{'glass-towel-glasduk':soldout}),
       ('Fälg startkit + Revolt',cart(('falg-startkit',1),('revolt-flygrostborttagare',1)),None),
       ('Pristine ensam',cart(('pristine-dack-plastfornyare',1)),None),
    ]
    for name,c,o in S:
        out=render(c,o); r=summary(out)
        print(f'## {name}: {len(r)}'); [print('   ',x) for x in r]
