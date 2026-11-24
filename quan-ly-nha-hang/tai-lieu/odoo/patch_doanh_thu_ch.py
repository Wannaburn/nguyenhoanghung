# Gắn dữ liệu Odoo: thay doanh thu mẫu bằng số thật, thêm bảng doanh thu theo cửa hàng ở trang Doanh thu
import pathlib
P=pathlib.Path(__file__).resolve().parents[2]/'index.html';s=P.read_text(encoding='utf-8')
def rep(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:70]);s=s.replace(a,b)
JS=r"""
const STORE_T_DEF={'003_PPX-DD':1300e6,'008_PPX-SVH':1000e6,'HH':null,'Café-PCAC':650e6,'010_PPX-NKKN':650e6};
const ODOO_STORES=['003_PPX-DD','008_PPX-SVH','HH','Café-PCAC','010_PPX-NKKN','NAT'];
const CH_GROUP=[['Tại chỗ',['Tại Chỗ'],'var(--accent)'],['Mang về',['Mang Về','Second Order - Ăn Vặt','Hotline'],'var(--blue)'],['App giao hàng',['Grab','ShopeeFood','Xanh Sm','Be Food'],'var(--saffron)']];
function applyOdoo(s){const O=ODOO_SALES,v=O.updated+'|'+O.to;if(s.odooVer===v)return false;
 for(const k in s.revenue)if(s.revenue[k].s)delete s.revenue[k];
 (s.sampleTargets||[]).forEach(k=>delete s.targets[k]);s.sampleTargets=[];
 const z={};for(const c in O.daily)for(const d in O.daily[c]){const a=O.daily[c][d],e=z[d]=z[d]||{amount:0,guests:0};e.amount+=a[2];e.guests+=a[3]}
 for(const d in z)s.revenue[d]={amount:z[d].amount,guests:z[d].guests,note:'Odoo · '+Object.keys(O.daily).length+' cửa hàng',odoo:1};
 s.storeT=Object.assign({},STORE_T_DEF,s.storeT||{});s.odooVer=v;return true}
function storeRows(){const O=ODOO_SALES,from=parse(O.from),to=parse(O.to),days=diffDays(from,to)+1,dm_=dim(from),T=S.storeT||STORE_T_DEF;
 return ODOO_STORES.filter(c=>O.daily[c]).map(c=>{const v=Object.values(O.daily[c]),sum=i=>v.reduce((a,x)=>a+x[i],0),g=sum(0),ck=sum(1),n=sum(2),b=sum(3),ch=O.ch[c]||{};
  const grp=CH_GROUP.map(([nm,ks])=>ks.reduce((a,k)=>a+((ch[k]||[0])[0]),0));return{c,g,ck,n,b,aov:b?n/b:0,day:n/days,fc:n/days*dm_,t:T[c],grp}})}
function storeSales(){
 const O=ODOO_SALES,from=parse(O.from),to=parse(O.to),m=U.revMonth;
 if(m.getFullYear()!==from.getFullYear()||m.getMonth()!==from.getMonth())return'';
 const days=diffDays(from,to)+1,dm_=dim(from),expect=days/dm_*100,rows=storeRows(),Z=rows.reduce((a,r)=>({n:a.n+r.n,b:a.b+r.b,g:a.g+r.g,ck:a.ck+r.ck}),{n:0,b:0,g:0,ck:0});
 const tAll=rows.every(r=>r.t)?rows.reduce((a,r)=>a+r.t,0):0,mx=Math.max(...rows.map(r=>Math.max(r.n,r.t||0)));
 const nm=c=>stShort(c),edit=can('mucTieu','S'),sel=U.revStore&&rows.some(r=>r.c===U.revStore)?U.revStore:'all';
 const bar=r=>{const p=r.t?r.n/r.t*100:null,cls=p==null?'':p>=expect?'':p>=expect*0.9?'warn':'bad';return`<div class="sb-row"><b>${esc(nm(r.c))}</b><div class="sb-track"><i class="${cls}" style="width:${r.n/mx*100}%"></i>${r.t?`<em style="left:${r.t/mx*100}%" title="Target ${money(r.t)}"></em>`:''}</div><span class="num">${money(r.n)}${p!=null?` · <span class="${cls?'t-'+cls:'t-ok'}">${Math.round(p)}%</span>`:''}</span></div>`};
 const mix=r=>{const tot=r.grp.reduce((a,x)=>a+x,0)||1;return`<div class="mix">${r.grp.map((x,i)=>x?`<i style="width:${x/tot*100}%;background:${CH_GROUP[i][2]}" title="${CH_GROUP[i][0]} ${Math.round(x/tot*100)}%"></i>`:'').join('')}</div><small class="muted">${r.grp.map((x,i)=>`${CH_GROUP[i][0]} ${Math.round(x/tot*100)}%`).join(' · ')}</small>`};
 const list=sel==='all'?null:O.daily[sel],dlist=[];for(let d=from;d<=addDays(from,dm_-1);d=addDays(d,1))dlist.push(d);
 const val=d=>{const k=ymd(d);if(list)return(list[k]||[0,0,0])[2];return rows.reduce((a,r)=>a+((O.daily[r.c][k]||[0,0,0])[2]),0)};
 const tline=sel==='all'?(tAll?tAll/dm_:null):((S.storeT||{})[sel]?(S.storeT[sel]/dm_):null);
 const chart=barChart(dlist.map(d=>String(d.getDate())),dlist.map(val),dlist.map(()=>tline),{hi:null,maxLabels:31,aria:'Doanh thu thuần từng ngày theo cửa hàng'});
 return`<div class="panel" id="rev-store"><div class="panel-h"><div><h2>Doanh thu theo cửa hàng · ${dm(from)} – ${dm(to)}</h2><p class="muted" style="margin:2px 0 0;font-size:.82rem">Số thật từ Odoo, doanh thu thuần (gộp − chiết khấu), mọi kênh. Đã qua ${days}/${dm_} ngày (${Math.round(expect)}% tháng). Cập nhật ${esc(O.updated.split('-').reverse().join('/'))}.</p></div>
  <div class="row"><span class="chip done">Zone ${money(Z.n)}</span><span class="chip">${fmt(Z.b)} bill · AOV ${fmt(Z.n/Z.b)}đ</span>${tAll?`<span class="chip ${Z.n/tAll*100>=expect?'done':'off'}">${Math.round(Z.n/tAll*100)}% target zone</span>`:''}</div></div>
  <div class="sb">${rows.map(bar).join('')}</div>
  <div class="tbl-wrap"><table class="st-t"><thead><tr><th>Cửa hàng</th><th class="r">DT thuần</th><th class="r">% zone</th><th class="r">Bill</th><th class="r">AOV</th><th class="r">% CK</th><th class="r">TB/ngày</th><th class="r">Dự báo tháng</th><th class="r">Target (tr)</th><th class="r">Đạt</th><th class="r">Dự báo / target</th><th>Kênh bán</th></tr></thead><tbody>
  ${rows.map(r=>`<tr><td><b>${esc(nm(r.c))}</b></td><td class="r num">${fmt(r.n)}</td><td class="r num">${Math.round(r.n/Z.n*100)}%</td><td class="r num">${fmt(r.b)}</td><td class="r num">${fmt(r.aov)}</td><td class="r num">${(r.ck/r.g*100).toFixed(1)}%</td><td class="r num">${money(r.day)}</td><td class="r num">${money(r.fc)}</td>
   <td class="r">${edit?`<input class="st-in num" type="text" inputmode="decimal" data-storet="${esc(r.c)}" value="${r.t?r.t/1e6:''}" placeholder="?" aria-label="Target tháng ${esc(nm(r.c))} (triệu)">`:(r.t?fmt(r.t/1e6):'–')}</td>
   <td class="r num">${r.t?Math.round(r.n/r.t*100)+'%':'–'}</td><td class="r num">${r.t?`<span class="t-${r.fc>=r.t?'ok':'bad'}">${Math.round(r.fc/r.t*100)}%</span>`:'–'}</td><td class="mixc">${mix(r)}</td></tr>`).join('')}
  <tr class="tot"><td><b>Zone</b></td><td class="r num"><b>${fmt(Z.n)}</b></td><td class="r">100%</td><td class="r num">${fmt(Z.b)}</td><td class="r num">${fmt(Z.n/Z.b)}</td><td class="r num">${(Z.ck/Z.g*100).toFixed(1)}%</td><td class="r num">${money(Z.n/days)}</td><td class="r num">${money(Z.n/days*dm_)}</td><td class="r num">${tAll?fmt(tAll/1e6):'–'}</td><td class="r num">${tAll?Math.round(Z.n/tAll*100)+'%':'–'}</td><td class="r num">${tAll?Math.round(Z.n/days*dm_/tAll*100)+'%':'–'}</td><td></td></tr></tbody></table></div>
  ${rows.some(r=>!r.t)?`<p class="muted" style="margin:0;font-size:.8rem">Chưa có target tháng của ${rows.filter(r=>!r.t).map(r=>nm(r.c)).join(', ')}. Nhập ở cột Target (đơn vị triệu) để tính % đạt và target zone. Target DD, SVH, NKKN, PCAC đang lấy theo bảng KPI tham khảo.</p>`:''}
  <div class="panel-h"><h3>Doanh thu thuần từng ngày</h3><div class="seg">${[['all','Zone'],...rows.map(r=>[r.c,nm(r.c)])].map(([k,n])=>`<button class="${sel===k?'on':''}" data-act="rev-store" data-s="${esc(k)}">${esc(n)}</button>`).join('')}</div></div>
  ${chart}
  <p class="muted" style="margin:0;font-size:.78rem">Nguồn: ${esc(O.src)}. Ngày ${dm(to)} có thể chưa đủ nếu còn bill chưa chốt. Chưa có số lượng bán theo món.</p></div>`}
"""
rep("/* ---------- Doanh thu & mục tiêu ---------- */",JS+"/* ---------- Doanh thu & mục tiêu ---------- */")
rep("if(S.sample&&!Object.keys(S.ops).length){seedOps(S);save()}}","if(S.sample&&!Object.keys(S.ops).length){seedOps(S);save()}if(applyOdoo(S))save()}")
rep("""  <div class="grid g4">
    <div class="panel kpi"><span class="lbl">Doanh thu tháng</span>""","""  ${storeSales()}
  <div class="grid g4">
    <div class="panel kpi"><span class="lbl">Doanh thu tháng</span>""")
rep("    case 'oc-g':U.ocG=ds.g;","    case 'rev-store':U.revStore=ds.s;{const y=window.scrollY;render();window.scrollTo(0,y)}return;\n    case 'oc-g':U.ocG=ds.g;")
rep("document.addEventListener('change',e=>{const on=e.target.dataset&&e.target.dataset.opnote;",
 "document.addEventListener('change',e=>{const stc=e.target.dataset&&e.target.dataset.storet;if(stc){if(!can('mucTieu','S')){toast('Bạn chỉ được xem mục này');return}const v=parseFloat(String(e.target.value).replace(',','.'));S.storeT=S.storeT||{};S.storeT[stc]=isNaN(v)||v<=0?null:Math.round(v*1e6);const rs=storeRows();if(rs.every(r=>r.t)){const f=parse(ODOO_SALES.from);S.targets[period('month',f).key]=rs.reduce((a,r)=>a+r.t,0)}save();toast('Đã lưu target');const y=window.scrollY;render();window.scrollTo(0,y);return}const on=e.target.dataset&&e.target.dataset.opnote;")
CSS=r"""
/* Doanh thu theo cửa hàng (Odoo) */
.sb{display:flex;flex-direction:column;gap:8px}
.sb-row{display:grid;grid-template-columns:70px minmax(0,1fr) 150px;gap:10px;align-items:center;font-size:.86rem}
.sb-track{position:relative;height:16px;background:var(--sunk);border-radius:4px}
.sb-track i{display:block;height:100%;border-radius:4px;background:var(--accent)}.sb-track i.warn{background:var(--saffron)}.sb-track i.bad{background:var(--red)}
.sb-track em{position:absolute;top:-3px;bottom:-3px;width:2px;background:var(--ink)}
.t-ok{color:var(--accent);font-weight:600}.t-warn{color:var(--saffron);font-weight:600}.t-bad{color:var(--red);font-weight:600}
.st-t td,.st-t th{padding:6px 7px;font-size:.82rem}.st-t tr.tot td{border-top:2px solid var(--ink);background:var(--sunk)}
.st-in{width:72px;text-align:right;padding:4px 6px}
.mixc{min-width:180px;white-space:normal!important}.mix{display:flex;height:8px;border-radius:4px;overflow:hidden;background:var(--sunk);margin-bottom:2px}.mix i{display:block;height:100%}
@media (max-width:560px){.sb-row{grid-template-columns:52px minmax(0,1fr);}.sb-row>span{grid-column:2;font-size:.78rem}}
"""
rep("@media (prefers-reduced-motion:reduce)",CSS+"@media (prefers-reduced-motion:reduce)")
P.write_text(s,encoding='utf-8');print('OK')

# Chỉnh sau: bỏ cột Kênh bán khỏi bảng, thêm khối 'Cơ cấu kênh bán' (.mixg); banner mẫu ghi rõ doanh thu là số thật Odoo.
