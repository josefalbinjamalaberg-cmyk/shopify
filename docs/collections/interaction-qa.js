const { chromium } = require('playwright');
const U='http://127.0.0.1:8790';
(async()=>{const b=await chromium.launch(); const p=await b.newPage({viewport:{width:390,height:844}});
const errs=[];p.on('pageerror',e=>errs.push(e.message));
const ev=[]; await p.exposeFunction('logEv',(n,d)=>ev.push(n+':'+JSON.stringify(d)));
await p.addInitScript(()=>{window.Shopify={analytics:{publish:(n,d)=>window.logEv(n,d)}}});
const state=async()=>p.evaluate(()=>({url:location.pathname+location.search, sel:document.querySelector('.nr-shop-intents .nr-chip[aria-current="true"]')?.textContent.trim(), cards:[...document.querySelectorAll('.nr-card__name a')].map(a=>a.textContent.trim()).join(','), count:document.querySelector('[data-nr-count]')?.textContent.trim(), pills:[...document.querySelectorAll('.nr-shop-active__pill')].map(a=>a.textContent.trim().replace(/\s+/g,' ')).join('|')}));
await p.goto(U+'/collections/exterior'); await p.waitForTimeout(200);
await p.getByRole('link',{name:'Flygrost & bromsdamm'}).click(); await p.waitForTimeout(400);
console.log('chip      ',JSON.stringify(await state()));
await p.getByRole('link',{name:'Asfalt & tjära'}).click(); await p.waitForTimeout(400);
console.log('chip2     ',JSON.stringify(await state()));
await p.goBack(); await p.waitForTimeout(500); console.log('back      ',JSON.stringify(await state()));
await p.goBack(); await p.waitForTimeout(500); console.log('back2     ',JSON.stringify(await state()));
await p.goForward(); await p.waitForTimeout(500); console.log('forward   ',JSON.stringify(await state()));
await p.reload(); await p.waitForTimeout(300); console.log('reload    ',JSON.stringify(await state()));
// accessories drawer
await p.goto(U+'/collections/accessories'); await p.waitForTimeout(200);
await p.locator('[data-nr-drawer-open]').click(); await p.waitForTimeout(200);
const open=await p.evaluate(()=>document.querySelector('dialog[data-nr-drawer]').open);
await p.locator('label.nr-shop-check',{hasText:'Dukar'}).click(); await p.waitForTimeout(500);
const btn=await p.locator('[data-nr-drawer-apply]').textContent();
await p.locator('[data-nr-drawer-apply]').click(); await p.waitForTimeout(500);
console.log('drawer    ',open,btn.trim(),JSON.stringify(await state()));
// sort
await p.selectOption('.nr-shop-sort__select','price-ascending'); await p.waitForTimeout(400);
console.log('sort      ',await p.evaluate(()=>location.search));
// empty
await p.goto(U+'/collections/accessories?filter.p.m.nrc.intent_accessories=acc_drying&filter.p.m.nrc.product_kind=kind_brush'); 
console.log('empty     ',await p.locator('.nr-shop-empty__title').textContent(), await p.locator('.nr-shop-empty .nr-btn').getAttribute('href'));
// quick add
await p.goto(U+'/collections/exterior'); await p.locator('[data-nr-quick-add]').first().click(); await p.waitForTimeout(500);
console.log('quickadd  ',await p.locator('[data-nr-quick-add]').first().getAttribute('class'), await p.locator('[data-nr-quick-add-status]').first().textContent());
// variant product
await p.goto(U+'/collections/interior'); console.log('variant   ',await p.locator('.nr-card',{hasText:'Mikrofiberduk'}).locator('.nr-card__add').evaluate(e=>e.tagName+' '+e.getAttribute('href')+' '+e.textContent.trim()));
// kits tabs
await p.goto(U+'/collections/fardiga-paket#interior'); await p.waitForTimeout(200);
const k1=await p.evaluate(()=>[document.querySelector('[role=tab][aria-selected=true]').textContent.trim(), [...document.querySelectorAll('.nr-kit-panel')].filter(x=>!x.hidden).length]);
await p.getByRole('tab',{name:'Fälg & däck'}).click(); await p.waitForTimeout(200);
const k2=await p.evaluate(()=>[location.hash,[...document.querySelectorAll('.nr-kit-panel:not([hidden]) .nr-kitc__name')].map(e=>e.textContent.trim())]);
await p.keyboard.press('ArrowRight'); const k3=await p.evaluate(()=>document.activeElement.textContent.trim());
console.log('kits      ',JSON.stringify(k1),JSON.stringify(k2),k3);
console.log('events    ',ev.map(e=>e.split(':')[0]).join(','));
console.log('errs',errs); await b.close();})();
