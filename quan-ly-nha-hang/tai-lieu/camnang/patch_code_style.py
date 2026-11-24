# Bỏ 3 tab cũ của Cẩm nang, đổi 4 mục PPX sang giao diện kiểu code (góc vuông, monospace, thanh terminal)
import pathlib,re
R=pathlib.Path(__file__).resolve().parents[2]
files={'app':R/'index.html','src':R/'tai-lieu/camnang/hb_ppx.js'}
T={k:v.read_text(encoding='utf-8') for k,v in files.items()}
def rep(a,b,only=None):
    for k in (only or T):
        assert T[k].count(a)==1,(k,T[k].count(a),a[:70]);T[k]=T[k].replace(a,b)
old_poster=T['src'][T['src'].index('function poster('):T['src'].index('\n',T['src'].index('function poster('))]
rep(old_poster,"""function poster(kind,title,sub,body,foot,file){return`<section class="panel poster"><div class="pst-bar"><span class="dots" aria-hidden="true"><i></i><i></i><i></i></span><span class="path">~/papaxot/cam-nang/${file}</span><span class="kind">${esc(kind)}</span></div>
 <div class="pst-body"><div class="pst-h"><h2 class="pst-t"><span class="pr" aria-hidden="true">$</span> ${title}</h2><p><span class="cmt">// </span>${sub}</p></div>${body}<div class="pst-f"><span class="cmt">// nguồn: </span>${foot.replace(/^Nguồn:\\s*/,'')}</div></div></section>`}
function dlHot(x,dd,wd,nm){return x.g==='M'&&x.d&&x.d.includes(dd)?'Hôm nay':x.g==='W'&&x.d&&x.d.includes(wd)?'Hôm nay':x.g==='H'&&x.h&&nm<x.h&&nm>=x.h-180?'Sắp đến hạn':''}""")
rep(" const now=x=>x.g==='M'&&x.d&&x.d.includes(dd)?'Hôm nay':x.g==='W'&&x.d&&x.d.includes(wd)?'Hôm nay':x.g==='H'&&x.h&&nm<x.h&&nm>=x.h-180?'Sắp đến hạn':'';"," const now=x=>dlHot(x,dd,wd,nm);")
for a,f in [("Đường đi","")]:pass
# thêm tên file vào 4 poster
for key,fn in [("Nguồn: Deadline báo cáo công việc hệ thống, HM công việc, QT đề xuất trình ký báo cáo chi, QĐ hủy bill – hủy NVL, Career Path PPX, QĐ nộp tiền & sổ doanh thu.')","deadline.ts"),
 ("Hình minh hoạ, không theo mặt bằng cửa hàng cụ thể.')","van-hanh.svg"),
 ("khi công ty ra memo mới cần cập nhật lại.')","quy-dinh.md"),
 ("Dòng \"Liên hệ PPX\" do em nối sang quy định Papaxốt.')","nganh.roadmap")]:
    rep(key,key[:-1]+",'"+fn+"')")
# hình vuông thay hình tròn trong SVG
rep('<circle cx="${x}" cy="${y}" r="16" class="cn"/>','<rect x="${x-16}" y="${y-16}" width="32" height="32" class="cn"/>')
rep('<circle cx="${x}" cy="${y}" r="38" class="stop"/>','<rect x="${x-38}" y="${y-38}" width="76" height="76" class="stop"/>')
# vHandbook mới, chỉ 4 mục
a=T['app'].index('function vHandbook(){');b=T['app'].index('function calcUpdate(box){')
T['app']=T['app'][:a]+r"""function vHandbook(){
  const t=today(),dd=t.getDate(),wd=t.getDay(),nm=nowMin();
  if(!['dl','vh','qd','nganh'].includes(U.hbTab))U.hbTab='dl';
  const hot=DL.filter(x=>dlHot(x,dd,wd,nm)),hotN=hot.reduce((a,x)=>a+x.it.length,0),amN=hot.reduce((a,x)=>a+x.it.filter(i=>i[1]==='AM').length,0);
  const md=MOD.filter(m=>(S.mod||{})[m[0]]).length,qn=QD.reduce((a,g)=>a+g.it.length,0);
  const tabs=[['dl','01','Deadline công việc','deadline.ts'],['vh','02','Kiến thức vận hành PPX','van-hanh.svg'],['qd','03','Quy định công ty','quy-dinh.md'],['nganh','04','Kiến thức ngành','nganh.roadmap']];
  const body={dl:hbDeadline,vh:hbOps,qd:hbRules,nganh:hbIndustry}[U.hbTab]();
  return`<div class="hb-code">
  <div class="head"><div><span class="lbl">// cẩm nang papaxốt</span><h1>Cẩm nang quản lý PPX</h1><p>Deadline · vận hành · quy định · kiến thức ngành. Dữ liệu lấy từ thư mục "Đào tạo AM Hưng".</p></div></div>
  <div class="kv"><div><span>deadline.homNay</span><b class="num">${hotN}</b><small>${amN} việc của AM</small></div><div><span>vanHanh.hangMuc</span><b class="num">17</b><small>10 ngày · 4 tuần · 3 tháng</small></div><div><span>quyDinh.nhom</span><b class="num">6</b><small>${qn} điểm chính</small></div><div><span>module.daHoc</span><b class="num">${md}/10</b><small>Module 7 → 16</small></div></div>
  <div class="ftabs" role="tablist">${tabs.map(([k,n,l,f])=>`<button role="tab" aria-selected="${U.hbTab===k}" class="${U.hbTab===k?'on':''}" data-act="hb-tab" data-k="${k}"><span><b>${n}</b> ${l}</span><small>${f}</small></button>`).join('')}</div>
  ${body}</div>`;
}
"""+T['app'][b:]
CSS=r"""
/* Cẩm nang kiểu code: góc vuông, monospace, thanh terminal, nền lưới */
.hb-code{--mono:"JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;--grid:rgba(127,140,130,.09);display:flex;flex-direction:column;gap:18px;font-family:var(--mono);font-size:.86rem}
.hb-code,.hb-code *{border-radius:0!important}
.hb-code h1,.hb-code h2,.hb-code h3,.hb-code .lbl,.hb-code .btn,.hb-code .seg button,.hb-code .chip,.hb-code button,.hb-code small,.hb-code b{font-family:var(--mono)}
.hb-code h1{font-size:1.45rem;letter-spacing:-.02em}
.hb-code .lbl{text-transform:none;letter-spacing:0;color:var(--faint)}
.kv{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));border:1px solid var(--ink);background:var(--surface)}
.kv>div{padding:12px 14px;border-right:1px solid var(--line);display:flex;flex-direction:column;gap:2px;min-width:0}.kv>div:last-child{border-right:0}
.kv span{color:var(--faint);font-size:.74rem}.kv b{font-size:1.6rem;color:var(--accent);line-height:1.2}.kv small{color:var(--muted);font-size:.72rem}
.ftabs{display:flex;border-bottom:2px solid var(--ink);gap:0}
.ftabs button{border:1px solid var(--line);border-bottom:0;background:var(--sunk);padding:8px 14px;text-align:left;font:500 .82rem var(--mono);color:var(--muted);display:flex;flex-direction:column;gap:2px;margin-right:-1px;cursor:pointer}
.ftabs button:hover{color:var(--ink)}
.ftabs button.on{background:var(--ink);color:var(--bg);border-color:var(--ink)}
.ftabs button b{color:var(--accent)}.ftabs button.on b{color:var(--saffron)}
.ftabs button small{font-size:.68rem;color:var(--faint)}.ftabs button.on small{color:var(--bg);opacity:.7}
.hb-code .poster{padding:0;gap:0;border:1px solid var(--ink)}
.pst-bar{display:flex;align-items:center;gap:12px;background:var(--ink);color:var(--bg);padding:7px 12px;font:600 .76rem var(--mono);min-width:0}
.pst-bar .dots{display:flex;gap:6px;flex:none}.pst-bar .dots i{width:10px;height:10px;display:block;background:#e5534b}.pst-bar .dots i:nth-child(2){background:#d29922}.pst-bar .dots i:nth-child(3){background:#3fb950}
.pst-bar .path{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;opacity:.85}
.pst-bar .kind{border:1px solid currentColor;padding:0 6px;font-size:.7rem;white-space:nowrap}
.pst-body{padding:16px;display:flex;flex-direction:column;gap:16px;background-color:var(--surface);background-image:linear-gradient(var(--grid) 1px,transparent 1px),linear-gradient(90deg,var(--grid) 1px,transparent 1px);background-size:24px 24px}
.hb-code .pst-h{border-bottom:1px dashed var(--ink)}
.hb-code .pst-t{font-size:1.5rem}.hb-code .pr{color:var(--accent)}
.hb-code .cmt{color:var(--faint)}
.hb-code .pst-f{border-top:1px dashed var(--line)}
.hb-code .seg{background:transparent;padding:0;gap:0;border:1px solid var(--line)}
.hb-code .seg button{border-right:1px solid var(--line);padding:5px 11px;font-size:.8rem}.hb-code .seg button:last-child{border-right:0}
.hb-code .seg button.on{background:var(--ink);color:var(--bg);box-shadow:none}
.hb-code .btn{border-color:var(--ink);font-size:.8rem}
.hb-code .btn.pri{background:var(--accent);border-color:var(--accent)}
.hb-code .who-c{background:transparent!important;padding:0;min-width:0;font-size:.74rem;flex:none;margin-right:8px;white-space:nowrap}
.hb-code .who-c::before{content:"[";color:var(--faint)}.hb-code .who-c::after{content:"]";color:var(--faint)}
.hb-code .tl2-ico{background:var(--ink)}
.hb-code .tl2-n{border-left:2px solid var(--ink);grid-template-columns:200px minmax(0,1fr)}
@media (max-width:820px){.hb-code .tl2-n{grid-template-columns:minmax(0,1fr)}}
.hb-code .tl2-dot{transform:rotate(45deg);left:-8px;width:13px;height:13px;border-width:2px}
.hb-code .tl2-n.hot{background:var(--saffron-soft);box-shadow:inset 3px 0 0 var(--saffron)}
.hb-code .tl2-time b::before{content:"@ ";color:var(--faint)}
.hb-code .tl2-n li{font-size:.82rem}
.hb-code .anat{border:1px solid var(--ink);background-color:var(--bg);background-image:linear-gradient(var(--grid) 1px,transparent 1px),linear-gradient(90deg,var(--grid) 1px,transparent 1px);background-size:24px 24px}
.hb-code .anat .lb1,.hb-code .anat .lb2,.hb-code .anat .cnt,.hb-code .anat .stopn,.hb-code .anat .signt,.hb-code .anat .tiny{font-family:var(--mono)!important}
.hb-code .anat .lb1{font-size:28px}.hb-code .anat .lb2{font-size:23px}
.hb-code .anat.road .rd{stroke-linecap:butt;stroke-linejoin:miter}
.hb-code .ana-c,.hb-code .mod{border:1px solid var(--line);border-left:3px solid var(--ink);background:var(--surface)}
.hb-code .ana-c.red{border:1px solid var(--red);border-left:3px solid var(--red)}
.hb-code .mod.on{border-left-color:var(--accent)}
.hb-code .ana-n,.hb-code .mod-i,.hb-code .big5 b{background:var(--ink);color:var(--bg)}
.hb-code .ana-h h3,.hb-code .mod h3{font-size:.95rem}
.hb-code .ana-c ul,.hb-code .mod ul,.hb-code .tl2-n ul{list-style:none;padding-left:0}
.hb-code .ana-c ul>li,.hb-code .mod ul>li{padding-left:16px;position:relative}
.hb-code .ana-c ul>li::before,.hb-code .mod ul>li::before{content:">";position:absolute;left:0;color:var(--accent);font-weight:700}
.hb-code .ana-c ol{list-style:decimal-leading-zero;padding-left:30px}
.hb-code .chip{background:transparent;border:1px solid var(--line);color:var(--muted)}
.hb-code .chip.ask{border-color:var(--saffron);color:var(--saffron)}
.hb-code .bar{height:6px}
@media (max-width:820px){.kv{grid-template-columns:repeat(2,minmax(0,1fr))}.kv>div:nth-child(2){border-right:0}.kv>div:nth-child(-n+2){border-bottom:1px solid var(--line)}.ftabs{display:grid;grid-template-columns:repeat(2,minmax(0,1fr))}.ftabs button{margin:0 -1px -1px 0;border-bottom:1px solid var(--line)}}
"""
rep("@media (prefers-reduced-motion:reduce)",CSS+"@media (prefers-reduced-motion:reduce)",only=['app'])
rep('family=Lexend:wght@500;600;700&display=swap','family=Lexend:wght@500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap',only=['app'])
for k,p in files.items():p.write_text(T[k],encoding='utf-8')
print('OK')
