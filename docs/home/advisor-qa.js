const { chromium } = require('playwright');
const ws=process.argv.slice(2).map(Number);
(async()=>{const b=await chromium.launch();
for(const w of ws){const p=await b.newPage({viewport:{width:w,height:w<750?844:900}});
const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('file://'+process.cwd()+'/out/after.html'); await p.waitForTimeout(200);
const sec=p.locator('[data-nr-advisor]'); await sec.scrollIntoViewIfNeeded();
const tabs=p.locator('[role=tab]'); const n=await tabs.count(); const res=[];
for(let i=0;i<n;i++){await tabs.nth(i).click(); await p.waitForTimeout(260);
 res.push(await p.evaluate(()=>{const vis=[...document.querySelectorAll('[role=tabpanel]')].filter(x=>!x.hidden);
  const sel=[...document.querySelectorAll('[role=tab][aria-selected=true]')];const pn=vis[0];
  const r=pn.getBoundingClientRect(); const over=[...pn.querySelectorAll('*')].filter(e=>{const q=e.getBoundingClientRect();return q.right>innerWidth+0.5||q.left<-0.5}).map(e=>e.className).slice(0,3);
  return {vis:vis.length,sel:sel.map(s=>s.textContent.trim()),name:pn.querySelector('.nr-advisor__name').textContent,price:pn.querySelector('.nr-advisor__price').textContent.trim(),pts:pn.querySelectorAll('.nr-advisor__points li').length,next:pn.querySelector('.nr-advisor__next-name')?.textContent.replace(/\s+/g,' ').trim(),ctrl:sel[0].getAttribute('aria-controls')===pn.id,over,h:Math.round(r.height)}}));
 if(i==0||i==2) await sec.screenshot({path:`out/adv-${w}-${i}.png`});}
// keyboard
await tabs.nth(0).click(); await p.keyboard.press('ArrowRight'); await p.keyboard.press('ArrowRight');
const k1=await p.evaluate(()=>document.activeElement.textContent.trim()+'|'+document.activeElement.getAttribute('aria-selected'));
await p.keyboard.press('End'); const k2=await p.evaluate(()=>document.activeElement.textContent.trim()); await p.keyboard.press('Home');await p.keyboard.press('ArrowLeft');
const k3=await p.evaluate(()=>document.activeElement.textContent.trim());
await p.keyboard.press('Tab'); const k4=await p.evaluate(()=>document.activeElement.className);
const g=await p.evaluate(()=>({hscroll:document.documentElement.scrollWidth>innerWidth, chipsScroll:(t=>t.scrollWidth>t.clientWidth)(document.querySelector('[role=tablist]'))}));
console.log(w,JSON.stringify(g),'keys',k1,k2,k3,k4,'errs',errs);
res.forEach(r=>console.log('  ',JSON.stringify(r)));
await tabs.nth(0).click(); await p.waitForTimeout(260);
await p.evaluate(()=>scrollTo(0,0)); await p.close();}
await b.close();})();
