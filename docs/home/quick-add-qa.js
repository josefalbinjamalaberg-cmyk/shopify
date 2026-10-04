const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch(); const p=await b.newPage({viewport:{width:390,height:844}});
const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('http://127.0.0.1:8765/after.html'); await p.evaluate(()=>fetch('/__set',{method:'POST',body:JSON.stringify({products:[]})}));
const btn=p.locator('[data-nr-quick-add]').first(); await btn.scrollIntoViewIfNeeded(); await btn.click(); await p.waitForTimeout(500);
console.log(await btn.getAttribute('class'), '|', await p.locator('[data-nr-quick-add-status]').first().textContent(), '|', await p.evaluate(async()=>JSON.stringify((await (await fetch('/cart.js')).json()).items.map(i=>i.product_id))));
const sizes=await p.evaluate(()=>[...document.querySelectorAll('.nr-best__add, .nr-routine__add, .nr-adv__tab, .nr-kitx__cta')].filter(e=>e.offsetParent).map(e=>{const r=e.getBoundingClientRect();return Math.round(Math.min(r.width,r.height))}).filter(x=>x<44));
console.log('small targets',sizes,'errs',errs); await b.close();})();
