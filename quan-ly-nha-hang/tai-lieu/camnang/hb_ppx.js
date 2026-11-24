/* ---------- Cẩm nang PPX: 4 mục vẽ theo mẫu ve-hinh-15-mau ----------
   Nguồn (Drive "Đào tạo AM Hưng"): Deadline báo cáo công việc hệ thống.xlsx, HM công việc.xlsx, Bộ mở - đóng ca & 6 note.xlsx,
   BỘ QUY ĐỊNH FULL 5S.xlsx, TỔNG HỢP CHÍNH SÁCH - QUY ĐỊNH KHỐI CH 15.04.25.xlsx, Nội quy lao động 21.08.24.docx,
   Career Path PPX 27.08.24.xlsx, QT ĐỀ XUẤT VÀ TRÌNH KÝ BÁO CÁO CHI 03.02.23.xlsx, QĐ Kiểm soát - đối chiếu hàng hóa, tiền.xlsx,
   2025 - QUY ĐỊNH HỦY BILL - HỦY NVL - ĐIỀU CHUYỂN.xlsx, 2025 - QUY TRÌNH BÁO - ĐẶT HÀNG.xlsx, Hướng dẫn xử lý sự việc.xlsx,
   bộ Leading A Shift Module 7–16. */
const DL=[
 {g:'Q',t:'25/01 · 25/07',w:'Nửa năm',it:[['CH gửi đề xuất thăng chức (đợt T03 – T09)','CH','AM','Mail']]},
 {g:'Q',t:'30/01 · 30/07',w:'Nửa năm',it:[['AM tổng hợp đề xuất thăng chức','AM','Ms. Dung','Mail']]},
 {g:'Q',t:'25/02 · 25/08',w:'Nửa năm',it:[['RGM gửi đề xuất nâng bậc (thâm niên đến 1/3 hoặc 1/9 ≥ 6 tháng, đã test P/B > 80%)','CH','AM','Promotion']]},
 {g:'Q',t:'Trước 20/02 · 20/08',w:'Nửa năm',it:[['Thi nâng bậc lý thuyết (≥ 80%)','RSC','','']]},
 {g:'Q',t:'Trước 20/03 · 20/09',w:'Nửa năm',it:[['Thi nâng bậc thực hành (Đạt)','RSC','','']]},
 {g:'Q',t:'25/03 · 25/09',w:'Nửa năm',it:[['Ms. Dung gửi danh sách đạt nâng bậc','RSC','OM, AM, CH','Mail']]},
 {g:'Q',t:'Tháng 4–5 · 10–11',w:'Nửa năm',it:[['Tái đào tạo, đào tạo cho level mới','OM','','']]},
 {g:'Q',t:'Cuối quý',w:'Quý',it:[['Kiểm kê tài sản – vật dụng, đối chiếu file N-X-T kế toán','CH','Kế toán','']]},
 {g:'Q',t:'Ngày 25 quý sau',w:'Quý',it:[['Nhận thưởng MS (TB > 97) / QSC (TB > 92) của quý','RSC','CH','']]},
 {g:'Q',t:'15 Tết âm lịch',w:'Năm',it:[['Chi 30% thưởng KPI năm','RSC','CH','']]},
 {g:'M',d:[1],t:'Ngày 1',it:[['Gửi chỉnh sửa chấm công từ ngày 16 đến cuối tháng','CH','AM','Mail'],['Gửi phiếu bổ sung lương','CH','AM','Zalo']]},
 {g:'M',d:[1,2,3,4,5],t:'Ngày 1 – 5',it:[['Phỏng vấn ứng viên & hẹn thử việc','CH','','']]},
 {g:'M',d:[2],t:'Ngày 2',it:[['Biên bản hủy hàng NVL & vật dụng (trước 15h)','CH','Ms. Nhi','Hardcopy'],['Ms. Dung gửi KPI','RSC','OM','Hardcopy']]},
 {g:'M',d:[3],t:'Ngày 3 · trước 16h',it:[['Biên bản kiểm kê hàng hóa','CH','AM, Ms. Nhi','Mail / Hardcopy'],['VP gửi chốt bảng điểm tháng cuối cùng','RSC','OM, AM, CH','Mail']]},
 {g:'M',d:[5],t:'Ngày 5',it:[['AM tổng hợp bảng chấm công zone (trước 10h)','AM','OM','Mail / Hardcopy'],['Chốt đối chiếu CPTH (trước 15h)','CH','Ms. Nhi','Mail'],['Phản hồi chốt số tồn đầu – nhập – hàng tổng hợp (trước 15h)','CH','Ms. Nhi','Mail'],['OM gửi chi phí lương (trước 16h)','OM','Ms. Nhi','Mail'],['Ms. Nhi gửi tổng hợp chi phí + P&L (trước 20h)','RSC','OM','Mail'],['Ms. Thơm cấp vật dụng, CCDC','RSC','CH','']]},
 {g:'M',d:[8],t:'Ngày 8',it:[['Ms. Nhi gửi file X – N – T','RSC','','']]},
 {g:'M',d:[10],t:'Ngày 10',it:[['Nhận lương + KPI (70%) + tiền đền','RSC','CH',''],['Ms. Dung cấp code NV mới','RSC','CH','Mail'],['Ms. Dung & Ms. Mai gửi record MS/QSC','RSC','Ms. Nhi','Mail'],['Hạn tuyển dụng – phỏng vấn – thử việc tháng n','CH','','']]},
 {g:'M',d:[15],t:'Ngày 15',it:[['Phản hồi chốt số bán – tồn cuối – hủy – đền hàng (trước 15h)','CH','Ms. Nhi','Mail'],['Báo cáo tình hình tuyển dụng (trước ngày 15)','CH','Ms. Dung','Mail'],['Gửi Sale và Turnover tháng n-1 (trước ngày 15)','CH','Ms. Nhi','Mail'],['Ms. Dung cấp VPP, biểu mẫu','RSC','CH','']]},
 {g:'M',d:[16],t:'Ngày 16',it:[['Gửi chỉnh sửa chấm công từ ngày 1 đến 15','CH','AM','Mail']]},
 {g:'M',d:[20],t:'Ngày 20',it:[['Ms. Nhi gửi file Record audit','RSC','OM, AM, CH','Mail'],['AM định hướng con đường thăng tiến','AM','','']]},
 {g:'M',d:[22],t:'Ngày 22',it:[['Ms. Thơm gửi chi phí bán hoạt động','RSC','Ms. Nhi','Viber']]},
 {g:'M',d:[23],t:'Ngày 23 · trước 15h',it:[['Phản hồi Record audit','CH','AM, Ms. Nhi','Mail']]},
 {g:'M',d:[25],t:'Ngày 25',it:[['Monthly Report (Manager roster, Best staff)','CH','AM, OM, Ms. Nhi','Mail'],['Staff List · Staffing Need','CH','AM, Ms. Dung','Mail'],['Đề xuất VPP & biểu mẫu · công cụ dụng cụ','CH','AM','Mail'],['Ms. Nhi chốt Record audit','RSC','OM, AM, CH','Mail'],['AM báo cáo kết quả thực hiện, đo lường KPI','AM','OM','']]},
 {g:'M',d:[26],t:'Ngày 26',it:[['AM tổng hợp VPP & BM, Staff need gửi HR','AM','Ms. Dung','Mail / Hardcopy']]},
 {g:'M',d:[27,28,29,30,31],t:'Ngày 27 → 10',it:[['Tuyển dụng & phỏng vấn; cho NV thử việc 3 ngày','CH','AM, Ms. Dung','']]},
 {g:'M',d:[28],t:'Ngày 28',it:[['Gửi KPI','CH','AM','Mail']]},
 {g:'M',d:[30],t:'Ngày 30',it:[['AM gửi KPI','AM','Ms. Dung','Hardcopy'],['Hủy / trả vật dụng về Bếp tổng (ngày 30 hoặc 31), kiểm kê hàng hóa cuối tháng','CH','Bếp tổng, Kế toán','Phiếu 2 liên']]},
 {g:'M',t:'Tuần 3 – 4',it:[['Học Orientation: tuần 3 thứ 5 (9h–12h), tuần 4 thứ 5 (14h–17h)','RSC','','Ms. Dung'],['Training bếp: thứ 6 tuần 3 và tuần 4 (9h–17h)','RSC','','Ms. Mai']]},
 {g:'W',d:[1],t:'Thứ 2',it:[['Gửi biên bản hủy, điều chuyển, ĐNTT','CH','AM','Hardcopy'],['Nộp sổ doanh thu về Ms. Thơm (theo xe hàng); nộp tiền DT (QTR, DD, SVH, NKKN, PCAC, TSN)','CH','Ms. Thơm','']]},
 {g:'W',d:[2],t:'Thứ 3',it:[['AM tổng hợp & ký biên bản hủy, ĐNTT','AM','Ms. Nhi','Hardcopy'],['AM tổng hợp đề xuất đồng phục / bảo trì','AM','Ms. Kiều / Mr. Đoan','Hardcopy'],['Nộp chứng từ chi về kế toán (trước 15h)','CH','Kế toán',''],['Gửi giấy doanh thu, phiếu ATM, bill hủy, bill test','CH','Ms. Hương',''],['Họp khối RSC · AM báo cáo Claim & Action Plan','AM','OM','Mail']]},
 {g:'W',d:[3],t:'Thứ 4',it:[['Check việc thực hiện quy trình & đưa hướng dẫn','AM','CH','']]},
 {g:'W',d:[4],t:'Thứ 5',it:[['Gửi đề xuất đồng phục, bảo trì','CH','AM','Mail'],['Ms. Nhi tổng hợp ĐNTT · Họp MKT · Họp Bảo trì','RSC','OM','Hardcopy'],['Check việc thực thi target','AM','CH',''],['Nộp tiền doanh thu','CH','Ms. Thơm','']]},
 {g:'W',d:[5],t:'Thứ 6 · trước 17h',it:[['Nhân viên đăng ký lịch rảnh tuần sau','CH','QL','']]},
 {g:'W',d:[6],t:'Thứ 7',it:[['Nộp tiền doanh thu','CH','Ms. Thơm','']]},
 {g:'W',d:[0],t:'Chủ nhật · trước 16h',it:[['Gửi Roster nhân viên tuần sau','CH','AM, OM','Mail']]},
 {g:'D',t:'Mỗi ngày',it:[['Gửi phiếu trả/hủy NVL kèm hàng về Bếp tổng khi có phát sinh (3 liên)','CH','Bếp tổng','Phiếu'],['Kiểm tra tiền, hàng hóa, đối chiếu O2C – Bếp – QL cuối ca (lệch tiền cho phép 20.000đ)','CH','AM, OM','BM ban hành']]},
 {g:'D',t:'Ngày n+1',it:[['QC gửi kết quả QSC','RSC','OM, AM, CH','Mail'],['Gửi đề xuất Claim điểm & Action Plan','CH','AM, Ms. Mai','Mail']]},
 {g:'D',t:'Sau 3 ngày kiểm kê',it:[['Gửi biên bản kiểm kê vật dụng & hàng hóa','CH','AM, Ms. Nhi','Mail / Hardcopy']]},
 {g:'D',t:'Trong 30 ngày',it:[['Chi phí quá 30 ngày kể từ ngày phát sinh không được giải quyết','CH','Kế toán','DNTT']]},
 {g:'H',h:600,t:'Trước 10h00',it:[['DSR','CH','AM, OM','Mail'],['Tồn hàng','CH','AM, OM, Ms. Nhi','Mail'],['Đặt hàng BTT','CH','Ms. Nhi, Ms. Ngân','Zalo']]},
 {g:'H',h:0,t:'Sau 3 giờ nhập hàng',it:[['Báo cáo hàng hóa sau khi nhập (quá hạn, chưa có QC xác nhận thì CH chịu đền)','CH','AM, Ms. Nhi, Ms. Ly, Ms. Mai','Viber']]},
 {g:'H',h:840,t:'Trước 14h00',it:[['Báo bổ sung / chỉnh sửa đơn hàng','CH','AM, Ms. Nhi','Mail / Viber']]},
 {g:'H',h:1260,t:'Trước 21h00',it:[['Báo bổ sung hàng hóa','CH','AM, Ms. Nhi, Ms. Ly','Viber'],['AM gửi xác nhận bổ sung hàng hóa','AM','Ms. Nhi, Ms. Ly','Viber']]}
];
const DLG=[['Q','Quý · nửa năm','Mốc theo quý, 6 tháng và năm'],['M','Tháng','Ngày cố định trong tháng'],['W','Tuần','Thứ cố định trong tuần'],['D','Ngày','Mốc tính theo sự việc'],['H','Giờ','Giờ chót trong ngày']];
const ICO={Q:'<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4M8 15h3"/>',M:'<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/><circle cx="12" cy="15" r="1.5"/>',W:'<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M7 14h2M11 14h2M15 14h2M7 17h2"/>',D:'<circle cx="12" cy="12" r="4"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M5 19l2-2M17 7l2-2"/>',H:'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'};
const dlIco=(g,s)=>`<svg viewBox="0 0 24 24" width="${s||22}" height="${s||22}" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${ICO[g]}</svg>`;
function poster(kind,title,sub,body,foot){return`<div class="panel poster"><div class="pst-h"><span class="lbl">${esc(kind)}</span><h2 class="pst-t">${title}</h2><p>${sub}</p></div>${body}<div class="pst-f">${foot}</div></div>`}
function hbDeadline(){
 const t=today(),dd=t.getDate(),wd=t.getDay(),nm=nowMin(),f=U.dlG||'all',am=!!U.dlAm;
 const now=x=>x.g==='M'&&x.d&&x.d.includes(dd)?'Hôm nay':x.g==='W'&&x.d&&x.d.includes(wd)?'Hôm nay':x.g==='H'&&x.h&&nm<x.h&&nm>=x.h-180?'Sắp đến hạn':'';
 const who=w=>`<span class="who-c ${w}">${w}</span>`;
 const sec=DLG.filter(([g])=>f==='all'||f===g).map(([g,n,s])=>{const rows=DL.filter(x=>x.g===g).map(x=>({...x,it:x.it.filter(i=>!am||i[1]==='AM')})).filter(x=>x.it.length);if(!rows.length)return'';
  return`<div class="tl2-sec"><div class="tl2-g"><span class="tl2-ico">${dlIco(g,26)}</span><div><b>${n}</b><small>${s}</small></div></div>
   ${rows.map(x=>{const hn=now(x);return`<div class="tl2-n ${hn?'hot':''}"><span class="tl2-dot"></span><div class="tl2-time"><b>${esc(x.t)}</b>${x.w?`<small>${esc(x.w)}</small>`:''}${hn?`<em>${hn}</em>`:''}</div>
    <ul>${x.it.map(([a,w,to,fm])=>`<li>${who(w)}<span>${esc(a)}${to||fm?` <small>→ ${esc([to,fm].filter(Boolean).join(' · '))}</small>`:''}</span></li>`).join('')}</ul></div>`}).join('')}</div>`}).join('');
 const seg=`<div class="row"><div class="seg">${[['all','Tất cả'],...DLG.map(x=>[x[0],x[1]])].map(([k,n])=>`<button class="${f===k?'on':''}" data-act="dl-g" data-k="${k}">${n}</button>`).join('')}</div><button class="btn sm ${am?'pri':''}" data-act="dl-am" aria-pressed="${am}">Chỉ việc của AM</button></div>`;
 return poster('Mẫu 15 · Timeline','Deadline công việc hệ thống','Báo cáo và công việc theo Quý → Tháng → Tuần → Ngày → Giờ. Mốc trùng hôm nay được tô sáng.',
  seg+`<div class="legend">${['CH','AM','OM','RSC'].map(w=>`<span>${who(w)} ${{CH:'Cửa hàng làm',AM:'AM làm',OM:'OM làm',RSC:'Văn phòng / RSC làm'}[w]}</span>`).join('')}</div><div class="tl2">${sec||'<div class="empty">Không có mục nào.</div>'}</div>`,
  'Nguồn: Deadline báo cáo công việc hệ thống, HM công việc, QT đề xuất trình ký báo cáo chi, QĐ hủy bill – hủy NVL, Career Path PPX, QĐ nộp tiền & sổ doanh thu.')}
/* Hình giải phẫu nhà hàng: mặt cắt, chú thích đánh số */
function calloutR(pts){/* pts: [n,x,y,t1,t2] điểm đã ở hệ tọa độ ngoài; nhãn xếp cột phải */
 const top=70,gap=Math.min(78,600/Math.max(1,pts.length-1));
 return pts.map(([n,x,y,t1,t2],i)=>{const ly=top+i*gap,lx=660;return`<path d="M${x} ${y} L${lx-40} ${ly} H${lx}" class="ld"/><circle cx="${x}" cy="${y}" r="16" class="cn"/><text x="${x}" y="${y+7}" class="cnt">${n}</text><text x="${lx+8}" y="${ly-2}" class="lb1">${n}. ${t1}</text><text x="${lx+8}" y="${ly+26}" class="lb2">${t2}</text>`}).join('')}
function svgRestaurant(){
 const T=(x,y)=>[Math.round(.75*x-100),Math.round(.75*y+60)];
 const pts=[[1,300,138,'Mặt tiền','Note I · Brand in–out'],[2,390,245,'Nhà vệ sinh','Note V · 7 chú ý'],[3,500,215,'Phòng quản lý','17 HM · 6 NOTE QL'],[4,742,215,'Kho · nhận hàng','5S · kiểm hàng ≤ 3 giờ'],[5,450,530,'Khu khách','Note II · III · IV'],[6,590,520,'Quầy O2C','Note III · 5S CCDC O2C'],[7,690,520,'Bếp · bar · SBOH','Note VI · 5 tiêu chuẩn sạch'],[8,790,440,'Tủ đông · tủ mát','Note đỏ · ATVSTP'],[9,877,545,'Gas · điện','Note đỏ · PCCC – ATLĐ']].map(([n,x,y,a,b])=>{const[X,Y]=T(x,y);return[n,X,Y,a,b]});
 return`<svg class="anat" viewBox="0 0 1080 760" role="img" aria-label="Mặt cắt nhà hàng Papaxốt với 9 vị trí vận hành">
 <g transform="translate(-100 60) scale(.75)">
 <rect x="230" y="170" width="620" height="420" class="wall"/><path d="M210 175 L540 70 L870 175 Z" class="roof"/>
 <rect x="420" y="112" width="240" height="44" rx="6" class="sign"/><text x="540" y="144" class="signt">PAPAXỐT</text>
 <line x1="160" y1="590" x2="920" y2="590" class="ground"/>
 <rect x="250" y="440" width="70" height="150" class="door"/><rect x="250" y="250" width="70" height="120" class="glass"/><path d="M180 590 v-90 h40 v90" class="std"/>
 <line x1="345" y1="370" x2="345" y2="590" class="part"/>
 ${[[400,520],[500,520]].map(([x,y])=>`<rect x="${x-35}" y="${y}" width="70" height="10" class="tbl"/><line x1="${x-25}" y1="${y+10}" x2="${x-25}" y2="590" class="part"/><line x1="${x+25}" y1="${y+10}" x2="${x+25}" y2="590" class="part"/>`).join('')}
 <rect x="560" y="470" width="60" height="120" class="counter"/>
 <line x1="640" y1="300" x2="640" y2="590" class="part"/><rect x="650" y="470" width="80" height="120" class="kit"/><circle cx="672" cy="470" r="9" class="burn"/><circle cx="708" cy="470" r="9" class="burn"/>
 <rect x="745" y="420" width="90" height="170" class="fridge"/><line x1="745" y1="500" x2="835" y2="500" class="part"/>
 <rect x="650" y="190" width="185" height="100" class="room"/><rect x="440" y="190" width="120" height="110" class="room"/><rect x="350" y="190" width="80" height="110" class="room"/>
 <rect x="860" y="500" width="34" height="90" rx="10" class="gas"/>
 </g>
 ${calloutR(pts)}
 </svg>`}
function hbOps(){
 const nd=NOTE6.reduce((a,x)=>a+x[2].length,0);
 const card=(n,title,body,cls)=>`<div class="ana-c ${cls||''}"><div class="ana-h"><span class="ana-n">${n}</span><h3>${title}</h3></div>${body}</div>`;
 const hm=`<div class="hm17"><div><span class="lbl">10 hạng mục ngày</span><ol>${[...HM_DAY].sort((a,b)=>a.n-b.n).map(h=>`<li><b>${esc(h.t)}</b> <small>${h.w.map(w=>fmtH(w[0])+'–'+fmtH(w[1])).join(' & ')} · ${esc(h.tool)}</small></li>`).join('')}</ol></div>
  <div><span class="lbl">4 hạng mục tuần</span><ol start="11">${HM_WEEK.map(h=>`<li><b>${esc(h.t)}</b></li>`).join('')}</ol><span class="lbl">3 hạng mục tháng</span><ol start="15">${HM_MONTH.map(h=>`<li><b>${esc(h.t)}</b></li>`).join('')}</ol>
  <p class="muted">AM dùng 17 HM để kiểm tra vận hành cửa hàng trong zone. Khung giờ QL: 8h–9h mở ca, 9h–10h30 công việc QL, 10h30–14h và 17h–21h tập trung vận hành, 14h–15h giao ca, 21h–22h30 kết ca.</p></div></div>`;
 const n6=`<div class="n6g">${NOTE6.map(([id,n,r])=>`<div><b>${id}. ${esc(n)}</b> <span class="chip">${r.length} chú ý</span><ul>${r.map(x=>`<li>${esc(x)}</li>`).join('')}</ul></div>`).join('')}</div><p class="muted">Tổng ${nd} chú ý, QL check ca sáng và ca tối, ghi bàn giao ca cuối bảng.</p>`;
 const sw=(bg,fg,t)=>`<span class="sw" style="background:${bg};color:${fg}">${t}</span>`;
 const G='#2e7d4f',LG='#cfe8d6',R='#c0392b',Y='#f2c94c',BR='#7a4e2d',GR='#8a8f93',W='#ffffff';
 const s5=`<div class="s5x"><div><span class="lbl">Mục tiêu</span><ul><li>Môi trường sạch sẽ, ngăn nắp</li><li>Dễ tìm, dễ lấy khi cần</li><li>Người hỗ trợ và người kiểm hiệu quả</li><li>Nâng cao kỷ luật, chuyên nghiệp</li><li>Nhân viên tự hào về nơi làm việc</li></ul>
  <span class="lbl">Bộ full set up (7 phần)</span><ol><li>9 tiêu chuẩn set up</li><li>5 tiêu chuẩn vệ sinh</li><li>Bộ set up màu</li><li>Bộ phân bổ khu vực</li><li>Bộ liệt kê chi tiết các nhóm khu vực</li><li>Bảng vẽ sơ đồ</li><li>Bộ 3 nghiệm thu (FOH · SBOH · BOH)</li></ol>
  <span class="lbl">Quy trình</span><p>Set up → Nghiệm thu → Bàn giao + đào tạo → Kiểm tra (bộ 3 nghiệm thu) → Duy trì (QL & NV giữ sắp xếp 5S + tiêu chuẩn 5S sạch).</p></div>
  <div><span class="lbl">9 tiêu chuẩn set up</span><ol><li>Tên nhóm chính</li><li>Tên nhóm phụ</li><li>Bảng hướng dẫn</li><li>Dụng cụ</li><li>Thiết bị</li><li>Nguyên liệu</li><li>Kho + kệ (có tab treo 5S)</li><li>Tab treo 5S</li><li>Kiểm tra set up 5S màu (chất liệu, kích thước, màu, tab treo)</li></ol>
  <span class="lbl">Bộ màu nhãn</span><table class="sw-t"><thead><tr><th>Loại</th><th>FOH</th><th>BOH</th></tr></thead><tbody>
  <tr><td>Nhóm chính · 7×20</td><td>${sw(G,W,'Xanh lá')}</td><td>${sw(LG,'#111','Nhận hàng')} ${sw(R,W,'Bếp')} ${sw(BR,W,'Hỗ trợ')} ${sw(Y,'#111','Điện')}</td></tr>
  <tr><td>Nhóm phụ</td><td>${sw(LG,'#111','Xanh nhạt 4×10')}</td><td>${sw('#2f6fa3',W,'7×10')}</td></tr>
  <tr><td>Bảng hướng dẫn</td><td>${sw(W,'#111','Trắng')}</td><td>${sw(W,'#111','Trắng')}</td></tr>
  <tr><td>Dụng cụ · 2,5×6</td><td>${sw(LG,'#111','Xanh nhạt')}</td><td>${sw(G,W,'Xanh lá')}</td></tr>
  <tr><td>Thiết bị · 2,5×6</td><td>${sw(R,W,'Đỏ')}</td><td>${sw(R,W,'Đỏ')}</td></tr>
  <tr><td>Nguyên liệu · 2,5×6</td><td>${sw(Y,'#111','Vàng')}</td><td>${sw(Y,'#111','Vàng')}</td></tr>
  <tr><td>Kho · 2,5×6</td><td>${sw(BR,W,'Nâu')}</td><td>${sw(GR,W,'Xám')}</td></tr>
  <tr><td>5S</td><td>${sw(W,'#111','Trắng')}</td><td>${sw(W,'#111','Trắng')}</td></tr></tbody></table>
  <small class="muted">Nhóm phụ BOH: file ghi "Nâu CF" nhưng mô tả "nền xanh dương chữ đen", em để theo mô tả, anh xác nhận lại.</small></div></div>`;
 const clean=`<ol class="big5">${S5_STD.map((x,i)=>`<li><b>${i+1}</b><span>${esc(x)}</span></li>`).join('')}</ol><p class="muted">Áp dụng cho từng khu vực: FOH (Khách hàng, O2C, Phục vụ, Bar), SBOH (check món, giao món, trộn món, clear, tạp vụ, giặt khô, rác), BOH (nhận hàng, kho, bếp trong, phụ bếp). Khăn: xanh lá lau ướt, vàng lau khô, xanh dương bếp/kính, trắng muỗng nĩa, nâu đế gỗ; CIF pha 1:3; lau 1 chiều.</p>`;
 const safe=`<div class="sf2">${SAFE.map(([n,r])=>`<div><b>${esc(n)}</b><ul>${r.map(([x,s])=>`<li>${esc(x)}${s==='?'?' <span class="chip ask">chờ xác nhận</span>':''}</li>`).join('')}</ul></div>`).join('')}</div>
  <p class="muted">Bảo quản: đông -18°C, mát 1–8°C, vùng nguy hiểm 5–60°C; rã lần 1 HSD 12h, lần 2 6h; kiểm nhiệt tủ 3 lần/ngày. Sự cố tủ: báo AM → thùng xốp + đá khô 2kg/20kg → giữ hàng hoặc chuyển BTT.</p>`;
 return poster('Mẫu 10 · Sơ đồ giải phẫu','Giải phẫu vận hành Papaxốt','9 vị trí trong nhà hàng gắn với 17 HM, 6 NOTE, Full 5S, 5 tiêu chuẩn sạch và note an toàn đỏ.',
  svgRestaurant()+`<div class="ana-grid">${card('A','17 hạng mục vận hành · 10 ngày · 4 tuần · 3 tháng',hm,'wide')}${card('B',`6 NOTE QL · ${nd} chú ý`,n6,'wide')}${card('C','Bộ Full 5S',s5,'wide')}${card('D','5 tiêu chuẩn sạch',clean)}${card('E','Note an toàn đỏ',safe,'red')}</div>`,
  'Nguồn: HM công việc, Bộ mở – đóng ca các vị trí & 6 note, BỘ QUY ĐỊNH FULL 5S, sổ tay quy trình PPX. Hình minh hoạ, không theo mặt bằng cửa hàng cụ thể.')}
/* Quy định: giải phẫu một nhân viên PPX */
const QD=[
 {n:1,p:'Đầu',t:'Thăng tiến & đào tạo',s:['Career Path PPX 27.08.24','Lịch đào tạo NV'],it:[
  'Tuyển dụng: CH gửi staff need trước 25 tháng n-1 → AM tổng hợp 26 → tuyển, phỏng vấn, thử việc 12 tiếng trước ngày 10 → HR cấp code ngày 12 → báo cáo tuyển dụng ngày 15.',
  'Đào tạo NV: lớp P1 Orientation + Phục vụ, P2 Pha chế + Thu ngân, P3 Kiểm soát món (tuần 3); B1 Luộc + Soạn + Xèo, B2 Bò + Chiên, B3 Thực hành bếp (tuần 4). Test lý thuyết ≥ 80%, thực hành Đạt.',
  'Nâng bậc PT/FT 2 đợt/năm: đề xuất 25/2 và 25/8, test tháng 3 và 9, kết quả 25/3 và 25/9. PT1 → PT2: ≥ 6 tháng; PT2 → PT3: giữ PT2 ≥ 6 tháng; FT2: ≥ 12 tháng và đã test đủ P1–P3, B1–B3.',
  'Quản lý: T-ARGM (≥ 6 tháng, test P&B ≥ 80%, đậu PV AM, OM) → ARGM1 (≥ 2 tháng, nắm 9 note, test ≥ 80% / thực hành ≥ 90%) → ARGM2 (≥ 6 tháng) → Acting RGM (≥ 12 tháng) → RGM1 (≥ 6 tháng, KPI 3 tháng TB ≥ 3.5) → RGM2 (≥ 12 tháng, KPI ≥ 4) → RGM3 (≥ 12 tháng, KPI ≥ 4.5).']},
 {n:2,p:'Tim',t:'Lương, thưởng & phúc lợi',s:['Tổng hợp chính sách 15.04.25','Điều chỉnh lương 01/05/2025'],it:[
  'Mức lương từ 01/05/2025: PT1 25.000 · PT2 26.000 · PT3 28.000đ/giờ; FT1 6,2tr · FT2 6,5tr; ARGM1 7,4tr · ARGM2 7,9tr · Acting 9,3tr; RGM1 10,4tr · RGM2 11,4tr · RGM3 12,4tr.',
  'Lương tháng n nhận ngày 10 tháng n+1; KPI 70% và tiền đền hao hụt ngày 10 tháng n+2; KPI 30% chi ngày 15 Tết âm lịch.',
  'KPI = KPI điều hành CH & giao việc (≥ 3 mới được cộng KPI doanh thu) + KPI doanh thu theo % target (100% → 150%). Điều hành 75%: chi phí 30%, DVKH – nhân sự 25% (turnover, MS, QSC, training audit), tuân thủ quy trình 15%, đặt hàng 5%; việc được giao 25%.',
  'Thâm niên: QL & FT ≥ 12 tháng = lương cơ bản; < 12 tháng = LCB/12 × tháng FT + 50.000 × tháng PT; PT 50.000/tháng, tối đa 50 tháng.',
  'Lễ Tết: lương ×2 các ngày lễ, ×3 mùng 1–3 Tết; hỗ trợ phần ăn 69.000/ca ≥ 5h mùng 1–6. Nghỉ phép năm 12 ngày (RSC & QL), kết hôn 3, tang 3, thai sản 5–7 ngày.',
  'Target cashier: 2 mục tiêu/ca, 15.000đ/mục tiêu, gấp đôi thành tích gấp đôi thưởng (ca ≥ 5h). Best staff: 5 voucher 100.000đ. Sinh nhật: chỉ chi cho RGM/ARGM. Đã hủy ứng lương.',
  'MS/QSC: MS TB > 97 / QSC TB > 92 một quý thưởng 500k, 2 quý 1,5tr, 3 quý 3tr, 4 quý 4tr. MS < 85 / QSC < 80: 1 tháng nhắc miệng, 2 tháng cảnh cáo văn bản, 3 tháng hạ bậc 3 tháng.']},
 {n:3,p:'Thân',t:'Nội quy lao động & tác phong',s:['Nội quy lao động 21.08.24','Chính sách chấm công 01/07/2024','Chính sách đồng phục'],it:[
  'Nội quy 9 chương: nguyên tắc chung; tuyển dụng; thời giờ làm việc – nghỉ ngơi; tiền lương – thưởng; trật tự doanh nghiệp (tác phong, đồng phục, cấm rượu bia, ma túy, cờ bạc, gây rối); an toàn vệ sinh lao động; bảo vệ tài sản – bí mật kinh doanh; kỷ luật & trách nhiệm vật chất; điều khoản thi hành.',
  'Kỷ luật: khiển trách miệng → cảnh cáo văn bản → cảnh cáo + kéo dài nâng lương ≤ 6 tháng / hạ bậc → sa thải. Bỏ ca không người thay: lập biên bản, 3 biên bản trong 3 tháng bị cho nghỉ việc.',
  'Chấm công: FT ≤ 8 tiếng tính theo giờ thực tế; > 8 tiếng phải bật tăng ca, cuối ngày báo AM duyệt. Phạt trễ PT / FT + QL / RSC: 6–9 phút 5k/10k/20k, 10–19 phút 10k/15k/30k, ≥ 20 phút 15k/20k/40k.',
  'Lịch làm: đăng ký trước 17h thứ 6; nghỉ 1 ngày/tuần, nghỉ > 2 ngày phải xin vào thứ 6; trễ/về sớm xin trước 2 tiếng; nghỉ việc báo trước 2 tuần (PT) / 1 tháng (FT).',
  'Nghỉ giải lao: 5–6h làm được 15 phút, 7–8h được 20 phút, thêm 5 phút mỗi giờ trên 8h; không nghỉ 11h–13h và 18h–20h; mặc áo khoác khi ngồi khu khách.',
  'Đồng phục: NV mới đóng 200.000đ/bộ (công ty hỗ trợ 50%), cấp đổi 1 lần/năm; CH đề xuất thứ 5, AM tổng hợp gửi Ms. Kiều.']},
 {n:4,p:'Tay phải',t:'Tiền & chi phí',s:['QĐ nộp tiền & sổ DT 04/04/2023','QT đề xuất trình ký báo cáo chi 03.02.23','QĐ kiểm soát – đối chiếu tiền 02/2026'],it:[
  'Nộp tiền: NTT, NTR, PH Mr. Hùng nhận mỗi ngày; QTR, DD, SVH, NKKN, PCAC, TSN nộp Ms. Thơm thứ 2, 5, 7; ATP nộp Aeon. Tiền bọc đen, ghi chi nhánh + ngày; sổ DT nộp thứ 2; giấy DT, ATM, bill hủy gửi Ms. Hương thứ 3.',
  'Kiểm tra tiền mỗi ngày lúc giao ca / cuối ca: đối chiếu tiền mặt, thẻ/QR, app, voucher, tiền chi với POS. Lệch cho phép 20.000đ; vượt thì lập biên bản, truy bill, báo AM – OM. Cấm thu không nhập POS, giao tiền không đếm, che giấu chênh lệch.',
  'Đối chiếu chéo O2C – Bếp – QL: lệch tiền truy O2C, lệch món truy Bếp, không rõ thì QL ca chịu.',
  'Petty cash 6.000.000đ/CH, mọi khoản chi phải có hóa đơn, chứng từ. Nộp chứng từ thứ 3 trước 15h. DNTT hợp lệ: đủ chữ ký người đề nghị và AM, đủ chứng từ, ghi rõ vật dụng mua mới, xếp đúng thứ tự; quá 30 ngày không giải quyết.',
  'Giảm giá: bill ≥ 1.500.000đ giảm 10% (trừ phần KM), gộp bill lẻ gian lận bị sa thải. Free ship cho đơn ≥ 1.500.000đ, đơn khác khách trả ship.']},
 {n:5,p:'Tay trái',t:'Hàng hóa',s:['QĐ hủy bill – hủy NVL – điều chuyển 2025','QT báo – đặt hàng 2025','QĐ kiểm tra hàng hóa 02/2026'],it:[
  'Đặt hàng BTT trước 10h; bổ sung/chỉnh sửa đơn trước 14h; báo bổ sung trước 21h (AM xác nhận). Tin nhắn thay đổi phải gửi tin mới, không sửa tin cũ.',
  'Kiểm hàng nhập trễ nhất 3 giờ sau khi xe xuống hàng; hàng lỗi nhắn group @QC xác nhận trong ngày, quá hạn CH chịu đền.',
  'Hủy bill chưa làm món: ghi "Hủy bill" + lý do trên bill, gửi Ms. Thơm hôm sau để xóa.',
  'Hủy NVL không đền: app/khách hủy đã làm món, thiết bị hư đột xuất, test món / đãi khách (không bấm bill, có chữ ký), hàng BTT không đạt. Có đền nếu vượt % cho phép: hàng hư tại CH, báo trễ, đổ món, làm sai món, hủy tồn cuối ngày (gà phủ xốt, bột chiên, trứng).',
  'Phiếu trả/hủy 3 liên (1 lưu CH, 2 về BTT); biên bản hủy, điều chuyển theo tuần gửi AM thứ 2 → AM ký gửi Ms. Nhi thứ 3. Hủy vật dụng ghi riêng, 1 lần cuối tháng.',
  'Kiểm tra hàng mỗi cuối ca: kiểm đếm → đối chiếu N-X-T với số bán POS. Định kỳ: hàng hóa cuối tháng, tài sản – vật dụng cuối quý. Thiếu: lập biên bản, CH bồi thường; dư: giải trình.']},
 {n:6,p:'Chân',t:'Vận hành cửa hàng & xử lý sự vụ',s:['Giờ hoạt động 17/10/2022','QĐ đồ ăn từ ngoài 10/03/2025','QĐ vị trí NKKN 10/03/2025','Hướng dẫn xử lý sự việc'],it:[
  'Giờ hoạt động: check in 8h00; nhận khách T2–T6 9h30–22h00, T7–CN 9h00–22h00; check out 22h30.',
  'Khách mang đồ từ ngoài: nước uống thì đổi ly CH; đồ ăn thì nhắc sau khi khách ăn xong; trẻ em được dùng cháo dinh dưỡng. CH phải có bảng thông báo dễ thấy.',
  'NKKN: 6h30–17h khách PPX & PCAC ngồi được khu BNC (khu A 3 bàn để bảng đặt bàn); 17h–22h chỉ khách BNC. Khách BNC được gọi full menu PPX và nước PCAC; khách PPX được gọi bia BNC.',
  'Xử lý sự vụ gian lận 4 giai đoạn: thu thập chứng cứ (POS, camera, chứng từ) → phân tích, lập Incident Report → làm việc ở phòng riêng (OM, HR, AM, người liên quan) → kết luận Level 1 đào tạo, Level 2 kỷ luật, Level 3 kỷ luật nặng, Level 4 điều tra mở rộng.',
  'KPI cảnh báo OM theo dõi: discount > 5% doanh thu, manager override > 3 lần/ngày, void bill > 2% số bill, re-open bill > 1%, voucher vượt trung bình chuỗi, đơn delivery hủy vượt chuẩn.']}
];
function svgStaff(){
 const pts=[[1,340,110,'Đầu','Thăng tiến & đào tạo'],[2,340,290,'Tim','Lương, thưởng & phúc lợi'],[3,340,420,'Thân · đồng phục','Nội quy & tác phong'],[4,502,470,'Tay phải · két tiền','Tiền & chi phí'],[5,178,475,'Tay trái · thùng hàng','Hàng hóa'],[6,370,700,'Chân · đứng ở cửa hàng','Vận hành & xử lý sự vụ']];
 return`<svg class="anat" viewBox="0 0 1080 760" role="img" aria-label="Giải phẫu một nhân viên Papaxốt theo 6 nhóm quy định">
 <g transform="translate(-200 0)">
 <circle cx="540" cy="130" r="62" class="skin"/><path d="M478 110 q62-70 124 0 v-18 q-62-48-124 0z" class="cap"/>
 <path d="M440 250 q100-50 200 0 l40 260 h-280z" class="shirt"/><path d="M480 270 h120 v280 h-120z" class="apron"/><text x="540" y="340" class="tiny" text-anchor="middle">PPX</text>
 <rect x="560" y="280" width="44" height="18" rx="3" class="badge"/>
 <path d="M440 255 l-70 170 l28 12 l60-140" class="shirt"/><path d="M640 255 l70 170 l-28 12 l-60-140" class="shirt"/>
 <circle cx="378" cy="440" r="22" class="skin"/><circle cx="702" cy="440" r="22" class="skin"/>
 <rect x="350" y="455" width="56" height="40" rx="6" class="box"/><rect x="676" y="452" width="52" height="34" rx="4" class="cash"/>
 <path d="M490 510 v190 h40 v-190 M550 510 v190 h40 v-190" class="pants"/><path d="M478 700 h60 v20 h-60z M542 700 h60 v20 h-60z" class="shoe"/>
 <path d="M520 285 q20-22 40 0 q-20 30-20 30 q0 0-20-30z" class="heart"/>
 <line x1="300" y1="722" x2="780" y2="722" class="ground"/>
 </g>
 ${calloutR(pts)}
 </svg>`}
function hbRules(){
 const open=U.qdOpen;
 return poster('Mẫu 10 · Sơ đồ giải phẫu','Giải phẫu quy định Papaxốt','Toàn bộ quy định khối cửa hàng gom thành 6 nhóm, gắn lên 6 bộ phận của một nhân viên PPX. Bấm vào từng nhóm để xem chi tiết.',
  svgStaff()+`<div class="qd-grid">${QD.map(g=>{const on=open==null||open===g.n;return`<div class="ana-c qd ${on?'':'mini'}"><button class="ana-h" data-act="qd-open" data-n="${g.n}" aria-expanded="${open===g.n}"><span class="ana-n">${g.n}</span><h3>${esc(g.t)}<small>${esc(g.p)} · ${g.it.length} điểm chính</small></h3></button>
   ${on?`<ul>${g.it.map(x=>`<li>${esc(x)}</li>`).join('')}</ul><div class="src">${g.s.map(x=>`<span class="chip">${esc(x)}</span>`).join('')}</div>`:''}</div>`}).join('')}</div>`,
  'Nguồn: thư mục QĐ KHỐI NHÀ HÀNG và QĐ BẾP TỔNG trên Drive. Số liệu lấy theo bản có ngày ban hành mới nhất; khi công ty ra memo mới cần cập nhật lại.')}
/* Kiến thức ngành: lộ trình Module 7–16 (Leading A Shift) */
const MOD=[
 [7,'Sẵn sàng để lãnh đạo','Từ nhân viên thành người quản lý',['Khác biệt vai trò nhân viên và quản lý: phạm vi, trách nhiệm, quyền hạn, ảnh hưởng','Năng lực cần có của người quản lý','Kỹ năng cơ bản: phân công công việc, cho phản hồi tích cực và mang tính xây dựng, ghi nhận công lao','Xử lý phản ứng không mong đợi từ nhân viên']],
 [8,'Kỹ năng đào tạo','Huấn luyện nhân viên hiệu quả',['Vai trò và lợi ích của huấn luyện, đối tượng cần huấn luyện','Quy trình 4 bước: Chuẩn bị → Hướng dẫn → Thực hành → Theo dõi & đánh giá','Chương trình hướng nghiệp và các chương trình huấn luyện cơ bản tại nhà hàng','Tiêu chuẩn đánh giá kết quả huấn luyện']],
 [9,'Hết lòng vì khách hàng','Khách có trải nghiệm tốt và muốn quay lại',['Thái độ luôn nói "YES!" với yêu cầu của khách','Giải quyết vấn đề, thu thập phản hồi và đưa giải pháp làm khách hài lòng','Phương pháp xử lý than phiền 4L','Huấn luyện nhân viên tự tin xử lý ngay tại chỗ']],
 [10,'Vệ sinh an toàn thực phẩm','Sạch sẽ theo góc nhìn của khách',['Khách đánh giá qua: toilet sạch, bàn sạch, thấy nhân viên rửa tay, nhà hàng sạch','Tiêu chuẩn VSATTP và QA checklist','Trách nhiệm QL bảo đảm nhân viên làm đúng chuẩn','Liên hệ PPX: note an toàn đỏ, nhiệt độ tủ, HSD, tem nhãn']],
 [11,'Chất lượng sản phẩm','Món ra đúng chuẩn mọi lúc',['Kiểm soát món theo tiêu chuẩn sản phẩm: định lượng, nhiệt độ, hình thức','Kiểm tra cảm quan tai – mắt – mũi trước khi ra món','Liên hệ PPX: chuẩn xốt, tốc độ ra món, khu kiểm soát món (KSM)']],
 [12,'An toàn an ninh','Bảo vệ khách, nhân viên và nhà hàng',['Huấn luyện nguyên tắc an toàn lao động, an ninh','Dùng hóa chất, thiết bị máy móc an toàn','An toàn cho nhân viên giao hàng','Xử lý tai nạn, tình huống bạo lực, khủng hoảng']],
 [13,'Kiểm kê hàng hóa','Kiểm soát chi phí qua hàng hóa',['Nhận hàng và bảo quản đúng tiêu chuẩn, hạn chế loại bỏ hàng','Đủ hàng để chuẩn bị món, dùng đúng hạn, dễ tìm','Kho khoa học, có tổ chức','Liên hệ PPX: kiểm hàng ≤ 3 giờ, kiểm kê cuối tháng, N-X-T']],
 [14,'Quản lý giờ công','Cân đối chi phí nhân công (COL)',['Chu trình: dự đoán giờ công → xếp lịch → thực hiện kế hoạch → đánh giá cải thiện','Weekly roster, bảng triển khai nhân viên từng bộ phận','Bố trí giờ nghỉ, phân công đúng bộ phận','Liên hệ PPX: roster CN trước 16h, target CP lương theo CH']],
 [15,'Kiểm soát tiền mặt','Tiền bán hàng là tài sản quan trọng nhất',['3 điểm kiểm soát: máy tính tiền, két trữ tiền, đi ngân hàng','Giảm chênh lệch giữa tiền thu và doanh thu báo cáo','Không biến kiểm soát tiền thành áp lực cho nhân viên','Liên hệ PPX: lệch cho phép 20.000đ, đối chiếu O2C – Bếp – QL']],
 [16,'Vận hành ca hoàn hảo','Tổng hợp mọi kỹ năng trong một ca',['Mở ca, giao ca, đóng ca của ca mở và ca đóng','Tiêu chuẩn vận hành 4P, 4L, 6T','Chuẩn bị trước, có tổ chức, kiểm tra nhân viên hoàn thành việc','Liên hệ PPX: bộ mở – đóng ca, 6 NOTE QL, 17 HM']]
];
const MOD_ICO={7:'<path d="M12 3l2.5 5 5.5.8-4 3.9 1 5.5-5-2.6-5 2.6 1-5.5-4-3.9 5.5-.8z"/>',8:'<path d="M3 7l9-4 9 4-9 4z"/><path d="M7 9v5c3 2 7 2 10 0V9"/>',9:'<path d="M12 20s-7-4.5-7-10a4 4 0 0 1 7-2.5A4 4 0 0 1 19 10c0 5.5-7 10-7 10z"/>',10:'<path d="M12 3c3 4 5 6.5 5 9.5a5 5 0 0 1-10 0C7 9.5 9 7 12 3z"/>',11:'<circle cx="12" cy="13" r="7"/><path d="M8 13h8M12 6V3"/>',12:'<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/>',13:'<rect x="4" y="4" width="16" height="16" rx="2"/><path d="M4 10h16M10 4v16"/>',14:'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',15:'<rect x="3" y="7" width="18" height="11" rx="2"/><circle cx="12" cy="12.5" r="2.5"/>',16:'<path d="M5 12l4 4 10-10"/>'};
function svgRoad(){
 const P=[[170,130],[540,130],[910,130],[910,330],[540,330],[170,330],[170,530],[540,530],[910,530],[910,730]];
 const d=`M60 130 H910 a100 100 0 0 1 0 200 H170 a100 100 0 0 0 0 200 H910 V770`;const SH=['Sẵn sàng lãnh đạo','Kỹ năng đào tạo','Hết lòng vì KH','VSATTP','Chất lượng SP','An toàn an ninh','Kiểm kê hàng hóa','Quản lý giờ công','Kiểm soát tiền','Vận hành ca'];
 return`<svg class="anat road" viewBox="0 0 1080 830" role="img" aria-label="Lộ trình học Module 7 đến 16">
 <path d="${d}" class="rd"/><path d="${d}" class="rdl"/>
 <text x="60" y="90" class="lb2">Bắt đầu</text>
 ${MOD.map(([n,t],i)=>{const[x,y]=P[i];return`<g><circle cx="${x}" cy="${y}" r="38" class="stop"/><text x="${x}" y="${y+12}" class="stopn">${n}</text><text x="${x}" y="${y+80}" class="lb1" text-anchor="middle">${SH[i]}</text></g>`}).join('')}
 </svg>`}
function hbIndustry(){
 const done=S.mod||{};const c=MOD.filter(m=>done[m[0]]).length;
 return poster('Mẫu 02 · Lộ trình','Lộ trình kiến thức ngành · Module 7 → 16','Bộ đào tạo quản lý ca "Leading A Shift": 10 chặng từ sẵn sàng lãnh đạo đến vận hành ca hoàn hảo. Đánh dấu chặng đã học.',
  `<div class="row"><span class="lbl">Đã học</span><b class="num">${c}/10 chặng</b><div class="bar" style="flex:1;min-width:120px"><i style="width:${c*10}%"></i></div></div>`+svgRoad()+
  `<div class="mod-list">${MOD.map(([n,t,sub,pts])=>{const on=!!done[n];return`<div class="mod ${on?'on':''}"><div class="mod-h"><span class="mod-i">${`<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${MOD_ICO[n]}</svg>`}</span><div><span class="lbl">Chặng ${n-6} · Module ${n}</span><h3>${esc(t)}</h3><small>${esc(sub)}</small></div>
   <button class="btn sm ${on?'pri':''}" data-act="mod-done" data-n="${n}" aria-pressed="${on}">${on?'✓ Đã học':'Đánh dấu đã học'}</button></div><ul>${pts.map(x=>`<li>${esc(x)}</li>`).join('')}</ul>${n===11?'<small class="muted">File Module 11 trên Drive đang trùng nội dung Module 7, ý chính viết theo tên module và chuẩn PPX. Anh gửi file đúng để em cập nhật.</small>':''}</div>`}).join('')}</div>`,
  'Nguồn: bộ Leading A Shift – In Store Management (Trainee Guide 2020), Module 07–16 trên Drive. Dòng "Liên hệ PPX" do em nối sang quy định Papaxốt.')}
