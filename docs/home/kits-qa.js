const { chromium } = require('playwright');
const ws=process.argv.slice(2).map(Number);
(async()=>{const b=await chromium.launch();
for(const w of ws){const p=await b.newPage({viewport:{width:w,height:w<750?844:900}});
const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('http://127.0.0.1:8765/after.html'); const sec=p.locator('#nr-bundle'); await sec.scrollIntoViewIfNeeded(); await p.waitForTimeout(300);
await sec.screenshot({path:`out/kits-${w}.png`});
const t=p.locator('[data-nr-kitx-toggle]'); const n=await t.count();
for(let i=0;i<n;i++){ if(await t.nth(i).isVisible()) await t.nth(i).click(); }
await p.waitForTimeout(400); await sec.screenshot({path:`out/kits-${w}-open.png`});
const m=await p.evaluate(()=>({hscroll:document.documentElement.scrollWidth>innerWidth, cards:[...document.querySelectorAll('.nr-kitx')].map(c=>{const r=c.getBoundingClientRect();return [c.className.split('--')[1],Math.round(r.width),Math.round(r.height), c.querySelector('.nr-kitx__price').textContent.replace(/\s+/g,' ').trim(), (c.querySelector('.nr-kitx__value')||{}).textContent?.replace(/\s+/g,' ').trim(), c.querySelectorAll('.nr-kitx__part').length, c.querySelector('[data-nr-kitx-toggle]').getAttribute('aria-expanded')]}), over:[...document.querySelectorAll('#nr-bundle *')].filter(e=>{const q=e.getBoundingClientRect();return q.width&&(q.right>innerWidth+0.5||q.left<-0.5)&&!e.closest('.nr-kitx__strip')}).map(e=>e.className).slice(0,4)}));
console.log(w,JSON.stringify(m),errs);await p.close();}
await b.close();})();
