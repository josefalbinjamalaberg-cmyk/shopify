const { chromium } = require('playwright');
const ws=process.argv.slice(2).map(Number);
const URL='http://127.0.0.1:8765/after.html';
(async()=>{const b=await chromium.launch();
for(const w of ws){const p=await b.newPage({viewport:{width:w,height:w<750?844:900}});
const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
await p.goto(URL); await p.waitForTimeout(200);
const sec=p.locator('[data-nr-advisor]'); await sec.scrollIntoViewIfNeeded(); await p.waitForTimeout(300);
const tabs=p.locator('[role=tab]'); const n=await tabs.count(); const res=[];
for(let i=0;i<n;i++){await tabs.nth(i).click(); await p.waitForTimeout(420);
 res.push(await p.evaluate(()=>{const vis=[...document.querySelectorAll('[role=tabpanel]')].filter(x=>!x.hidden);
  const sel=[...document.querySelectorAll('[role=tab][aria-selected=true]')];const pn=vis[0];
  const over=[...pn.querySelectorAll('*')].filter(e=>{const q=e.getBoundingClientRect();return q.width&&(q.right>innerWidth+0.5||q.left<-0.5)}).map(e=>e.className).slice(0,3);
  const q=s=>pn.querySelector(s); const t=s=>q(s)?.textContent.replace(/\s+/g,' ').trim();
  return {vis:vis.length,sel:sel.map(s=>s.textContent.trim()).join(),name:t('.nr-adv__name'),price:t('.nr-adv__price'),cta:t('.nr-adv__cta'),pts:pn.querySelectorAll('.nr-adv__points li').length,stage:q('.nr-adv__stage').className.split('--')[1],addon:t('.nr-routine__name')+' '+t('.nr-routine__price'),kit:t('.nr-routine__kit-line'),over,h:Math.round(pn.getBoundingClientRect().height)}}));
 if([0,2,3,5,6].includes(i)) await sec.screenshot({path:`out/adv2-${w}-${i}.png`});}
const g=await p.evaluate(()=>({hscroll:document.documentElement.scrollWidth>innerWidth, tabsScroll:(t=>t.scrollWidth>t.clientWidth)(document.querySelector('[role=tablist]'))}));
console.log(w,JSON.stringify(g),'errs',errs.slice(0,3));
res.forEach(r=>console.log('  ',JSON.stringify(r)));
await p.close();}
await b.close();})();
