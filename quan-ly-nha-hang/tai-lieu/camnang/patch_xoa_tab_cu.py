# Xóa hẳn code 3 tab cũ của Cẩm nang (Bản đồ công việc, Lộ trình 90 ngày, Kiến thức & công thức), giữ 4 mục PPX kiểu poster
import pathlib,re
P=pathlib.Path(__file__).resolve().parents[2]/'index.html';s=P.read_text(encoding='utf-8')
def cut(a,b):
    global s
    i=s.index(a);j=s.index(b,i);s=s[:i]+s[j:]
def rep(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:70]);s=s.replace(a,b)
cut("/* ---------- Cẩm nang quản lý ---------- */","/* ---------- Cẩm nang PPX")
cut("function calcUpdate(box){","/* ---------- Nhà hàng trực tiếp")
i=s.index("function vHandbook(){");j=s.index("/* ---------- Nhà hàng trực tiếp",i)
s=s[:i]+r"""function vHandbook(){
  const t=today(),hot=DL.filter(x=>dlHot(x,t.getDate(),t.getDay(),nowMin())),hotN=hot.reduce((a,x)=>a+x.it.length,0),amN=hot.reduce((a,x)=>a+x.it.filter(i=>i[1]==='AM').length,0);
  const md=MOD.filter(m=>(S.mod||{})[m[0]]).length,qn=QD.reduce((a,g)=>a+g.it.length,0);
  if(!['dl','vh','qd','nganh'].includes(U.hbTab))U.hbTab='dl';
  const tabs=[['dl','Deadline công việc'],['vh','Kiến thức vận hành PPX'],['qd','Quy định công ty'],['nganh','Kiến thức ngành']];
  return`<div class="head"><div><span class="lbl">Cẩm nang Papaxốt</span><h1>Cẩm nang quản lý PPX</h1><p>Deadline, kiến thức vận hành, quy định công ty và kiến thức ngành, lấy từ thư mục "Đào tạo AM Hưng".</p></div></div>
  <div class="grid g3"><div class="panel kpi"><span class="lbl">Deadline hôm nay</span><span class="v">${hotN} việc</span><span class="sub">${amN} việc của AM</span></div>
  <div class="panel kpi"><span class="lbl">Quy định công ty</span><span class="v">6 nhóm</span><span class="sub">${qn} điểm chính · 17 HM vận hành</span></div>
  <div class="panel kpi"><span class="lbl">Kiến thức ngành</span><span class="v">${md}/10 module</span><div class="bar"><i style="width:${md*10}%"></i></div></div></div>
  <div class="seg">${tabs.map(([k,n])=>`<button class="${U.hbTab===k?'on':''}" data-act="hb-tab" data-k="${k}">${n}</button>`).join('')}</div>
  ${{dl:hbDeadline,vh:hbOps,qd:hbRules,nganh:hbIndustry}[U.hbTab]()}`;
}
"""+s[j:]
# dlHot dùng chung
rep(" const now=x=>x.g==='M'&&x.d&&x.d.includes(dd)?'Hôm nay':x.g==='W'&&x.d&&x.d.includes(wd)?'Hôm nay':x.g==='H'&&x.h&&nm<x.h&&nm>=x.h-180?'Sắp đến hạn':'';"," const now=x=>dlHot(x,dd,wd,nm);")
rep("function hbDeadline(){","function dlHot(x,dd,wd,nm){return x.g==='M'&&x.d&&x.d.includes(dd)?'Hôm nay':x.g==='W'&&x.d&&x.d.includes(wd)?'Hôm nay':x.g==='H'&&x.h&&nm<x.h&&nm>=x.h-180?'Sắp đến hạn':''}\nfunction hbDeadline(){")
# thao tác cũ
for pat in [r"    case 'hb-dom':[^\n]*\n",r"    case 'hb-back':[^\n]*\n",r"    case 'toc':[^\n]*\n",r"    case 'lesson':[^\n]*\n",r"    case 'learn':[^\n]*\n",r"    case 'hb-cal':[^\n]*\n[^\n]*\n",r"    case 'path':[^\n]*\n"]:
    s,n=re.subn(pat,'',s);assert n==1,(pat,n)
rep("case 'ev-done':case 'hb-cal':return","case 'ev-done':return")
rep("    case 'hb-tab':U.hbTab=ds.k;U.hbDomain=null;break;","    case 'hb-tab':U.hbTab=ds.k;break;")
rep("hbTab:'dl',hbDomain:null};","hbTab:'dl'};")
rep("const cb=e.target.closest&&e.target.closest('[data-calc]');if(cb){calcUpdate(cb);return}","")
rep("sample:false,learn:{},path:{},chk:{}","sample:false,chk:{}")
# CSS cũ
i=s.index("/* Cẩm nang */\n");j=s.index(".ck{display:flex",i)
s=s[:i]+s[j:]
rep(".ck-t small{display:block;font-size:.72rem;color:var(--dc);font-weight:500}\n",".ck-t small{display:block;font-size:.72rem;color:var(--muted);font-weight:500}\n")
for ln in ["  .hb-map{","  .hb-row{","  .hb-row>*{","  .hb-dom{","  .hb-head,","  .hb-cell .fq{"]:
    i=s.index(ln);j=s.index("\n",i)+1;s=s[:i]+s[j:]
P.write_text(s,encoding='utf-8');print('OK',len(s))
