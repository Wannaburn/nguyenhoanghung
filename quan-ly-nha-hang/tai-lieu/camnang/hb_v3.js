/* Cẩm nang bản 3.
   1) Deadline công việc: bảng giống file "Deadline báo cáo công việc hệ thống.xlsx" (Thời gian | Nội dung | Người nhận | Hình thức | x người thực hiện).
   2) Kiến thức vận hành: sơ đồ mặt bằng 6 khu theo 6 NOTE + mặt bằng bếp – kho "An toàn đỏ" (HTML grid, không dùng đường chỉ dẫn). */
/* it: [nội dung, người nhận, hình thức, người thực hiện] — mã người thực hiện theo cột DLC */
const DLC=[['C','CH'],['A','AMs'],['D','Ms. Dung'],['M','Ms. Mai'],['L','Ms. Ly · Ngọc'],['N','Ms. Nhi'],['T','Ms. Thơm'],['K','MKT'],['B','Mr. Đoan'],['O','OM']];
const DL=[
 {g:'H',h:600,t:'Trước 10h hôm sau',it:[['CH gửi DSR','AM, OM','Mail','C'],['CH gửi Tồn hàng','AM, OM, Ms. Nhi','Mail','C'],['CH gửi Đặt hàng','Ms. Nhi, Ms. Ngân','Zalo','C']]},
 {g:'H',h:840,t:'Trước 14h mỗi ngày',it:[['CH báo bổ sung / chỉnh sửa đơn hàng','AM, Ms. Nhi','Mail / Viber','C']]},
 {g:'H',h:1260,t:'Trước 21h mỗi ngày',it:[['CH báo bổ sung hàng hóa','AM, Ms. Nhi, Ms. Ly','Viber','C'],['AM gửi xác nhận bổ sung hàng hóa','Ms. Nhi, Ms. Ly','Viber','A']]},
 {g:'H',t:'Sau 3 tiếng nhập hàng',it:[['CH báo cáo hàng hóa sau khi nhập','AM, Ms. Nhi, Ms. Ly, Ms. Mai','Viber','C']]},
 {g:'H',t:'Sau 3 ngày kể từ ngày kiểm kê',it:[['CH gửi biên bản kiểm kê vật dụng & hàng hóa','AM, Ms. Nhi','Mail / Hardcopy','C']]},
 {g:'H',t:'Ngày n+1 (sau audit)',it:[['QC gửi kết quả QSC','OM, AM, CH','Mail','M'],['CH gửi đề xuất Claim điểm & Action Plan','AM, Ms. Mai','Mail','C']]},
 {g:'W',d:[1],t:'Thứ 2 mỗi tuần',it:[['CH gửi các biên bản hủy, ĐNTT…','AM','Hardcopy','C']]},
 {g:'W',d:[2],t:'Thứ 3 mỗi tuần',it:[['AM tổng hợp & ký biên bản hủy, ĐNTT…','Ms. Nhi','Hardcopy','A'],['AM tổng hợp đề xuất Đồng phục','Ms. Kiều','Hardcopy','A'],['AM tổng hợp đề xuất Bảo trì','Mr. Đoan','Hardcopy','A'],['Họp khối RSC','','','ADMLNTKBO']]},
 {g:'W',d:[2],t:'Thứ 3 tuần gần nhất',it:[['AM báo cáo & đề xuất các lỗi Claim & Action Plan (đã xử lý)','OM','Mail','A'],['OM phê duyệt các lỗi được Claim','Ms. Dung, Ms. Mai, AM','Mail','O']]},
 {g:'W',d:[4],t:'Thứ 5 mỗi tuần',it:[['CH gửi đề xuất Đồng phục','AM','Mail','C'],['CH gửi đề xuất Bảo trì','AM','Mail','C'],['Ms. Nhi tổng hợp các ĐNTT','OM','Hardcopy','N'],['Họp MKT','','','K'],['Họp Bảo trì','','','B']]},
 {g:'W',d:[0],t:'Trước 16h Chủ nhật',it:[['CH gửi Roster nhân viên','AM, OM','Mail','C']]},
 {g:'M',d:[1],t:'Ngày 1',it:[['CH gửi chỉnh sửa chấm công từ ngày 16 đến cuối tháng','AM','Mail','C'],['CH gửi phiếu bổ sung lương','AM','Zalo','C']]},
 {g:'M',d:[1,2,3,4,5],t:'Từ ngày 1 đến ngày 5',it:[['CH phỏng vấn ứng viên & hẹn thử việc','','','C']]},
 {g:'M',d:[2],t:'Ngày 2',it:[['CH gửi biên bản hủy hàng NVL & vật dụng (trước 15h)','Ms. Nhi','Hardcopy','C'],['Ms. Dung gửi KPI','OM','Hardcopy','D']]},
 {g:'M',d:[3],t:'Ngày 3',it:[['VP gửi chốt bảng điểm tháng cuối cùng','OM, AM, CH','Mail','DM']]},
 {g:'M',d:[3],t:'Trước 16h – Ngày 3',it:[['CH gửi biên bản kiểm kê hàng hóa','AM, Ms. Nhi','Mail / Hardcopy','C']]},
 {g:'M',d:[5],t:'Ngày 5',it:[['CH chốt đối chiếu CPTH (trước 15h)','Ms. Nhi','Mail','C'],['Ms. Thơm cấp vật dụng, công cụ dụng cụ','CH','','T']]},
 {g:'M',d:[5],t:'Trước 10h – Ngày 5',it:[['AM tổng hợp bảng chấm công zone','OM','Mail / Hardcopy','A']]},
 {g:'M',d:[5],t:'Trước 15h – Ngày 5',it:[['CH phản hồi chốt số tồn đầu – nhập – hàng tổng hợp','Ms. Nhi','Mail','C'],['Ms. Nhi chốt số tồn đầu – nhập – hàng tổng hợp','CH','Mail','N']]},
 {g:'M',d:[5],t:'Trước 16h – Ngày 5',it:[['OM gửi chi phí lương','Ms. Nhi','Mail','O']]},
 {g:'M',d:[5],t:'Trước 20h – Ngày 5',it:[['Ms. Nhi gửi tổng hợp các chi phí + P&L','OM','Mail','N']]},
 {g:'M',d:[8],t:'Ngày 8',it:[['Ms. Nhi gửi file X – N – T','','','N']]},
 {g:'M',d:[10],t:'Ngày 10',it:[['Ms. Dung cấp code NV','CH','Mail','D'],['Nhận lương + KPI – tiền đền','','','T'],['Ms. Dung & Ms. Mai gửi record MS/QSC','Ms. Nhi','Mail','DM']]},
 {g:'M',t:'Trước ngày 15',it:[['CH gửi báo cáo tình hình tuyển dụng','Ms. Dung','Mail','C'],['CH gửi thông tin Sale và Turnover tháng n-1','Ms. Nhi','Mail','C'],['Ms. Dung cấp VPP, biểu mẫu','CH','','D'],['Ms. Dung gửi cập nhật file KPI (nếu có)','AM, CH','','D']]},
 {g:'M',d:[15],t:'Trước 15h – Ngày 15',it:[['CH phản hồi chốt số bán – tồn cuối – hủy hàng – đền hàng','Ms. Nhi','Mail','C'],['Ms. Nhi chốt số bán – tồn cuối – hủy hàng – đền hàng','CH','Mail','N']]},
 {g:'M',d:[16],t:'Ngày 16',it:[['CH gửi chỉnh sửa chấm công từ ngày 1 đến ngày 15','AM','Mail','C']]},
 {g:'M',d:[20],t:'Ngày 20',it:[['Ms. Nhi gửi file Record audit','OM, AM, CH','Mail','N']]},
 {g:'M',d:[22],t:'Ngày 22',it:[['Ms. Thơm gửi chi phí bán hoạt động','Ms. Nhi','Viber','T']]},
 {g:'M',d:[23],t:'Trước 15h ngày 23',it:[['CH phản hồi Record audit','AM, Ms. Nhi','Mail','C']]},
 {g:'M',d:[25],t:'Ngày 25',it:[['CH gửi Monthly Report (Manager roster, Best staff)','AM, OM, Ms. Nhi','Mail','C'],['CH gửi Staff List','AM, Ms. Dung','Mail','C'],['CH gửi Staffing Need','AM, Ms. Dung','Mail','C'],['CH đề xuất VPP & BM','AM, Ms. Dung','Mail','C'],['CH đề xuất công cụ dụng cụ','AM','Mail','C'],['Ms. Nhi gửi chốt Record audit','OM, AM, CH','Mail','N']]},
 {g:'M',d:[26],t:'Ngày 26',it:[['AM tổng hợp VPP & BM gửi Ms. Dung','Ms. Dung','Mail / Hardcopy','A'],['AM tổng hợp Staff need gửi Ms. Dung','Ms. Dung','Mail / Hardcopy','A']]},
 {g:'M',d:[27,28,29,30,31,1,2,3,4,5,6,7,8,9,10],t:'Từ ngày 27 đến ngày 10',it:[['CH tuyển dụng & phỏng vấn','AM, Ms. Dung','','C'],['CH cho NV được thử việc 3 ngày','','','C']]},
 {g:'M',d:[28],t:'Ngày 28',it:[['CH gửi KPI','AM','Mail','C']]},
 {g:'M',d:[30],t:'Ngày 30',it:[['AM gửi KPI cho Ms. Dung','Ms. Dung','Hardcopy','A']]},
 {g:'T',wk:3,d:[4],t:'Tuần 3 · Thứ 5 (9h–12h)',it:[['Học Orientation','','','D']]},
 {g:'T',wk:4,d:[4],t:'Tuần 4 · Thứ 5 (14h–17h)',it:[['Học Orientation','','','D']]},
 {g:'T',wk:3,d:[5],t:'Tuần 3 · Thứ 6 (9h–17h)',it:[['Training bếp','','','M']]},
 {g:'T',wk:4,d:[5],t:'Tuần 4 · Thứ 6 (9h–17h)',it:[['Training bếp','','','M']]},
 {g:'Q',md:['1-25','7-25'],t:'25/01 và 25/07',it:[['CH gửi đề xuất thăng chức T03 – T09','AM','Mail','C']]},
 {g:'Q',md:['1-30','7-30'],t:'30/01 và 30/07',it:[['AM tổng hợp đề xuất thăng chức','Ms. Dung','Mail','A']]},
 {g:'Q',t:'Trước ngày 20 tháng 2 & 8',it:[['Thi nâng bậc lý thuyết','','','']]},
 {g:'Q',t:'Trước ngày 20 tháng 3 & 9',it:[['Thi nâng bậc thực hành','','','']]},
 {g:'Q',md:['3-25','9-25'],t:'Trước ngày 25 tháng 3 & 9',it:[['Ms. Dung gửi danh sách đạt nâng bậc','OM, AM, CH','Mail','D']]}
];
const DLG=[['H','Hằng ngày','Giờ chót trong ngày, mốc theo sự việc'],['W','Hằng tuần','Thứ cố định trong tuần'],['M','Hằng tháng','Ngày cố định trong tháng'],['T','Đào tạo','Lịch học tuần 3 – tuần 4'],['Q','Nửa năm','Thăng chức, nâng bậc']];
const ICO={Q:'<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4M8 15h3"/>',M:'<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/><circle cx="12" cy="15" r="1.5"/>',W:'<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M7 14h2M11 14h2M15 14h2M7 17h2"/>',T:'<path d="M3 6l9-3 9 3-9 3z"/><path d="M7 8v5c0 1.5 2.5 3 5 3s5-1.5 5-3V8"/>',H:'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'};
const dlIco=(g,s)=>`<svg viewBox="0 0 24 24" width="${s||22}" height="${s||22}" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${ICO[g]}</svg>`;
function poster(kind,title,sub,body,foot){return`<div class="panel poster"><div class="pst-h"><span class="lbl">${esc(kind)}</span><h2 class="pst-t">${title}</h2><p>${sub}</p></div>${body}<div class="pst-f">${foot}</div></div>`}
function dlHot(x,dd,wd,nm,mo){
 if(x.g==='M')return x.d&&x.d.includes(dd)?'Hôm nay':'';
 if(x.g==='W')return x.d&&x.d.includes(wd)?'Hôm nay':'';
 if(x.g==='T')return x.d&&x.d.includes(wd)&&Math.ceil(dd/7)===x.wk?'Hôm nay':'';
 if(x.g==='Q')return x.md&&mo&&x.md.includes(mo+'-'+dd)?'Hôm nay':'';
 if(x.g==='H')return x.h&&nm<x.h&&nm>=x.h-180?'Sắp đến hạn':'';
 return''}
function hbDeadline(){
 const t=today(),dd=t.getDate(),wd=t.getDay(),mo=t.getMonth()+1,nm=nowMin(),f=U.dlG||'all',am=!!U.dlAm;
 const dot=k=>`<span class="dlx-x ${k}" aria-label="x">x</span>`;
 const body=DLG.filter(([g])=>f==='all'||f===g).map(([g,n,s])=>{
  const rows=DL.filter(x=>x.g===g).map(x=>({...x,it:x.it.filter(i=>!am||i[3].includes('A'))})).filter(x=>x.it.length);if(!rows.length)return'';
  return`<tr class="dlx-g"><td colspan="${4+DLC.length}"><span class="dlx-gi">${dlIco(g,18)}</span><b>${n}</b><small>${s}</small></td></tr>`+
   rows.map(x=>{const hn=dlHot(x,dd,wd,nm,mo);return x.it.map(([a,to,fm,w],j)=>`<tr class="${hn?'hot':''}">${j?'':`<td class="dlx-t" rowspan="${x.it.length}"><b>${esc(x.t)}</b>${hn?`<em>${hn}</em>`:''}</td>`}<td class="dlx-c">${esc(a)}</td><td>${esc(to)}</td><td class="dlx-f">${esc(fm)}</td>${DLC.map(([k])=>`<td class="dlx-o">${w.includes(k)?dot(k):''}</td>`).join('')}</tr>`).join('')}).join('')}).join('');
 const seg=`<div class="row"><div class="seg">${[['all','Tất cả'],...DLG.map(x=>[x[0],x[1]])].map(([k,n])=>`<button class="${f===k?'on':''}" data-act="dl-g" data-k="${k}">${n}</button>`).join('')}</div><button class="btn sm ${am?'pri':''}" data-act="dl-am" aria-pressed="${am}">Chỉ việc của AM</button></div>`;
 return poster('Bảng deadline','Tổng deadline báo cáo – công việc','Trình bày giống file Deadline của hệ thống. Cột bên phải đánh <b>x</b> cho người thực hiện. Dòng tô vàng là mốc rơi vào hôm nay hoặc sắp đến giờ.',
  seg+`<p class="dlx-hint muted">Vuốt ngang bảng để xem cột người thực hiện.</p><div class="dlx-wrap"><table class="dlx"><thead><tr><th class="dlx-t">Thời gian</th><th>Nội dung</th><th>Người nhận</th><th>Hình thức</th>${DLC.map(([k,n])=>`<th class="dlx-o">${esc(n)}</th>`).join('')}</tr></thead><tbody>${body||`<tr><td colspan="${4+DLC.length}" class="empty">Không có mục nào.</td></tr>`}</tbody></table></div>`,
  'Nguồn: Deadline báo cáo công việc hệ thống.xlsx (sheet Deadline tổng), Drive "Đào tạo AM Hưng".')}
/* ---------- Kiến thức vận hành: mặt bằng 6 NOTE + An toàn đỏ ---------- */
const N6_SUB=['Bảng hiệu · outside · bảo vệ · xe','Sàn · bàn ghế · đèn · nhiệt độ · nhạc','Đón khách · order · thanh toán','Gửi món · xốt · dọn bàn','Cửa · bồn · sàn · mùi · giấy','Phân công · hàng · an toàn 3 khu'];
const N6_SHORT=['Mặt tiền','Khu khách','Quầy O2C','Lối bưng món','Nhà vệ sinh','Bếp · Bar · Kho'];
const N6_AREA=['front','khach','o2c','lane','wc','boh'];
const N6_ICO=['<path d="M3 21h18M5 21V9l7-5 7 5v12"/><path d="M9 21v-6h6v6"/>','<circle cx="12" cy="12" r="4"/><path d="M12 3v3M12 18v3M3 12h3M18 12h3"/>','<rect x="3" y="7" width="18" height="12" rx="2"/><path d="M7 11h4M7 15h10"/>','<path d="M4 15h16M6 15a6 6 0 0 1 12 0M12 7V5"/><path d="M3 19h18"/>','<path d="M7 3h10v7a5 5 0 0 1-10 0z"/><path d="M9 21h6M12 15v6"/>','<path d="M4 10h16v10H4z"/><path d="M8 10V6M12 10V4M16 10V6"/>'];
const nIco=(i,s)=>`<svg viewBox="0 0 24 24" width="${s||22}" height="${s||22}" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${i}</svg>`;
const SAFE_PT=[['dong','Tủ đông','≤ -18°C · đo nhiệt, ghi phiếu 3 lần/ngày','A'],['mat','Tủ mát','1–8°C · rã đông tại đây, không rã ngoài','A'],['kho','Kệ kho','HSD · tem nhãn · sống – chín để riêng','A'],['rac','Thùng rác','Có nắp · không bụi, mùi, ruồi','A'],['gas','Bình gas','Kiểm đầu ca · khóa van khi kết ca','B'],['dien','Tủ điện','Thiết bị tốt · tắt khi không dùng','B'],['pccc','Bình chữa cháy · lối thoát','Đúng vị trí · còn hạn · lối thoát thông','B'],['san','Sàn · dao · chảo','Sàn khô · dao, chảo nóng để đúng chỗ','B']];
function hbOps(){
 const nd=NOTE6.reduce((a,x)=>a+x[2].length,0),op=U.n6==null?-1:U.n6;
 const plan=`<div class="plan6" role="group" aria-label="Mặt bằng nhà hàng chia 6 khu theo 6 NOTE">${NOTE6.map(([id,n,r],i)=>`<button class="pz z${i+1} ${op===i?'on':''}" style="grid-area:${N6_AREA[i]}" data-act="n6-open" data-i="${i}" aria-pressed="${op===i}"><span class="pz-n">${i+1}</span><span class="pz-i">${nIco(N6_ICO[i],22)}</span><b>${N6_SHORT[i]}</b><small>Note ${id} · ${r.length} chú ý</small></button>`).join('')}<span class="pz-door">Cửa vào ↑</span></div>`;
 const n6=`<div class="n6c">${NOTE6.map(([id,n,r],i)=>(op<0||op===i)?`<div class="ana-c n6k z${i+1}"><div class="ana-h"><span class="ana-n">${i+1}</span><h3>Note ${id} · ${esc(n)}<small>${N6_SHORT[i]} · ${r.length} chú ý · ${esc(N6_SUB[i])}</small></h3></div><ol>${r.map(x=>`<li>${esc(x)}</li>`).join('')}</ol></div>`:'').join('')}</div>`;
 const card=(n,t,body,cls)=>`<div class="ana-c ${cls||''}"><div class="ana-h"><span class="ana-n">${n}</span><h3>${t}</h3></div>${body}</div>`;
 const li=a=>`<ul>${a.map(x=>`<li>${x}</li>`).join('')}</ul>`;
 const q=' <span class="chip ask">chờ xác nhận</span>';
 const sA=card('A','ATVSTP · an toàn vệ sinh thực phẩm',li(SAFE[0][1].map(([x,s])=>esc(x)+(s==='?'?q:'')))+
  `<span class="lbl">Bảo quản & HSD</span>`+li(['Tủ đông -18°C, tủ mát 1–8°C; vùng nguy hiểm 5–60°C','Kiểm nhiệt độ tủ 3 lần/ngày, ghi phiếu theo dõi','Rã đông lần 1: HSD 12h; lần 2: 6h; không cấp đông lại lần 2','HSD: đông lạnh 30 ngày · mì miến 96h · kim chi 14 ngày · rau 72h · bánh mì 24h','Rau sơ chế: ngâm muối 3 phút (4gr/1L), rửa 3 lần','Kiểm hàng nhập trễ nhất 3 giờ sau khi xe xuống hàng']),'red');
 const sB=card('B','PCCC – ATLĐ · an toàn lao động',li(SAFE[1][1].map(([x,s])=>esc(x)+(s==='?'?q:'')))+
  `<span class="lbl">Kết ca</span>`+li(['Tắt thiết bị không dùng, kiểm nhiệt độ tủ','Khóa điện, nước, gas, cửa → quay clip kết ca','Bàn giao bảo vệ, ký sổ']),'red');
 const sC=card('C','Khi có sự cố',li(['<b>Tủ đông/mát hư:</b> báo AM → chuyển hàng vào thùng xốp + đá khô 2kg/20kg → giữ hàng hoặc chuyển về BTT','<b>Hàng nhập lỗi, cận/hết date:</b> nhắn group bếp @QC trong ngày; quá hạn không có QC xác nhận thì CH chịu đền','<b>Hàng hết HSD tại CH:</b> hủy có tính đền, phải trả hàng về Bếp tổng kèm phiếu','<b>Tai nạn, cháy nổ:</b> ưu tiên an toàn người, báo QL ca → AM → OM']),'red');
 const safe=`<div class="plan8" role="img" aria-label="Mặt bằng bếp – kho với 8 điểm an toàn đỏ">${SAFE_PT.map(([a,n,r,k],i)=>`<div class="sz ${k}" style="grid-area:${a}"><span class="sz-n">${i+1}</span><div><b>${n}</b><small>${r}</small></div><em>${k==='A'?'ATVSTP':'PCCC – ATLĐ'}</em></div>`).join('')}</div>`;
 return poster('Sơ đồ mặt bằng','Mổ xẻ Papaxốt theo 6 NOTE',`Mặt bằng chia 6 khu, mỗi khu là 1 note QL kiểm mỗi ca sáng và ca tối, tổng ${nd} chú ý. Bấm vào khu để xem riêng note đó, bấm lại để xem cả 6.`,
  plan+n6+
  `<div class="pst-h safe-h"><span class="lbl">Hình 2</span><h2 class="pst-t">An toàn đỏ</h2><p>Mặt bằng bếp – kho với 8 điểm nguy cơ. Không đạt thì dừng việc khác để xử lý ngay.</p></div>`+
  safe+`<div class="legend"><span><i class="sw A"></i> Thẻ A · ATVSTP</span><span><i class="sw B"></i> Thẻ B · PCCC – ATLĐ</span></div><div class="ana-grid">${sA}${sB}${sC}</div>`,
  'Nguồn: Bộ mở – đóng ca các vị trí & 6 note, sổ tay quy trình PPX, QĐ hủy bill – hủy NVL 2025. Sơ đồ minh hoạ, không theo mặt bằng cửa hàng cụ thể.')}
