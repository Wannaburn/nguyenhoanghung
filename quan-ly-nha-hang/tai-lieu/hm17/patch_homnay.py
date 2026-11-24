# Viết lại trang Hôm nay theo 17 hạng mục vận hành PPX.
# Nguồn (Drive "Đào tạo AM Hưng"): HM công việc.xlsx, Bộ mở - đóng ca các vị trí & 6 note.xlsx, BỘ QUY ĐỊNH FULL 5S.xlsx
import re, pathlib
P = pathlib.Path(__file__).resolve().parents[2] / 'index.html'
s = P.read_text(encoding='utf-8')

def rep(old, new, cnt=1):
    global s
    n = s.count(old)
    assert n == cnt, (n, old[:80])
    s = s.replace(old, new)

# 1. Dữ liệu: thêm S.ops
rep("chk:{},staff:[],attend:{},profile:{},logbook:[]}}", "chk:{},staff:[],attend:{},profile:{},logbook:[],ops:{}}}")
rep("if(S.sample&&!S.logbook.length){seedToday(S);save()}}",
    "if(S.sample&&!S.logbook.length){seedToday(S);save()}if(S.sample&&!Object.keys(S.ops).length){seedOps(S);save()}}")
rep("S.logbook=(S.logbook||[]).filter(x=>!x.s);S.staff=",
    "S.logbook=(S.logbook||[]).filter(x=>!x.s);for(const k in S.ops||{})if(S.ops[k]._s)delete S.ops[k];S.staff=")

# 2. Bỏ checklist khung giờ cũ (tổng hợp nhiều thương hiệu), thay bằng dữ liệu PPX
a = s.index("const SHIFT_CL=")
b = s.index("const STAFF_GROUP=")
s = s[:a] + "/* Nguồn cũ SHIFT_CL (checklist khung giờ tổng hợp) đã thay bằng 17 hạng mục PPX, xem tai-lieu/hm17 */\n" + s[b:]
rep("const STAFF_GROUP={pv:'PV',tn:'TN',bc:'BEP',pb:'BEP',rc:'BEP',kho:'BEP',pc:'BAR',ql:'QL'};",
    "const STAFF_GROUP={pv:'PV',tn:'O2C',bc:'BEP',pb:'BEP',rc:'BEP',kho:'BEP',pc:'PC',ql:'QL'};")
a = s.index("function clItems(g)")
b = s.index("const readerName=")
s = s[:a] + s[b:]

DATA = r'''
/* ---------- 17 hạng mục vận hành PPX: 10 ngày, 4 tuần, 3 tháng ----------
   Nguồn: HM công việc.xlsx (giờ, công cụ), Bộ mở - đóng ca các vị trí & 6 note.xlsx (khung giờ QL, bộ mở/đóng ca, 6 NOTE QL),
   BỘ QUY ĐỊNH FULL 5S.xlsx (5 tiêu chuẩn vệ sinh, phân bổ khu vực). */
const HM_DAY=[
 {n:1,t:'Bộ QĐ mở ca – giao ca – đóng ca',w:[[540,600],[900,960]],lb:['Mở ca','Giao ca'],tool:'Cam',sub:'oc',d:'Kiểm tra bộ mở ca, giao ca, đóng ca của từng vị trí: Quản lý, Phục vụ, O2C, Pha chế, Kiểm soát món, Bếp.'},
 {n:2,t:'Doanh thu',w:[[540,660]],tool:'Excel',sub:'rev',d:'Kiểm tra doanh thu, gửi DSR trước 10h. Giao ca và kết ca: kiểm tra doanh thu – tiền bàn giao O2C.'},
 {n:3,t:'Chi phí',w:[[540,660]],tool:'Excel',d:'Kiểm tra chi phí trong ngày: CP bán hoạt động, CP tổng hợp, CP lương so với target.'},
 {n:4,t:'Quản lý hàng hóa',w:[[570,600]],tool:'NH, Cam',d:'Đặt hàng – trả hàng (đặt BTT trước 10h). Giao kế hoạch forecast cho các nhóm bếp, kiểm tra việc chuẩn bị hàng so với forecast.'},
 {n:5,t:'Chương trình MKT',w:[[600,660]],tool:'NH, Viber',d:'Kiểm tra chương trình MKT, CTKM đang chạy tại cửa hàng.'},
 {n:6,t:'Thiết bị & hệ thống POS',w:[[510,540]],tool:'Viber',d:'Kiểm tra thiết bị, hệ thống POS trước giờ nhận khách.'},
 {n:7,t:'Tốc độ',w:[[660,780],[1080,1200]],tool:'NH, Cam',d:'Kiểm soát tốc độ ra món giờ cao điểm. Chuẩn: món đầu ≤ 8 phút, bill 2 món ≤ 12 phút, gà phủ xốt ≤ 17 phút.'},
 {n:8,t:'Chất lượng',w:[[630,840],[1020,1260]],tool:'NH',d:'Kiểm soát chất lượng dịch vụ – sản phẩm, quy trình FOH – BOH – SBOH.'},
 {n:9,t:'6 note',w:[[630,840],[1020,1260]],tool:'NH',sub:'n6',d:'Kiểm tra checklist 6 NOTE QL theo ca sáng và ca tối.'},
 {n:10,t:'TC an toàn (ATVSTP – PCCC – Vệ sinh NH)',w:[[630,840],[1020,1260]],tool:'NH, Viber',sub:'safe',d:'Note an toàn đỏ (ATVSTP, PCCC – ATLĐ) và 5S theo 5 tiêu chuẩn sạch.'}
];
const HM_WEEK=[{n:11,t:'Hài lòng khách hàng'},{n:12,t:'Tài chính'},{n:13,t:'Local Deli'},{n:14,t:'Data'}];
const HM_MONTH=[{n:15,t:'Năng lực nhân sự & kế thừa'},{n:16,t:'Đào tạo theo Circle & hạng mục đào tạo (RSC/NH)'},{n:17,t:'Tài sản (kiểm kê / thay mới / bảo trì)'}];
const OC={
 QL:{n:'Quản lý',o:['Kiểm tra thiết bị, hệ thống POS','Kiểm tra hình ảnh Brand','Kiểm tra vệ sinh + 5S','Kiểm tra doanh thu','Kiểm tra chi phí','Đủ nhân sự + tác phong','Họp đầu ca – phân công công việc','Giao kế hoạch chuẩn bị hàng hóa cho các vị trí','Đặt hàng – trả hàng'],
  c:['Bổ sung đơn hàng (nếu cần)','Kiểm đếm hàng hóa','Kiểm tra xả hàng cho sáng hôm sau, kiểm tra vệ sinh','Kiểm tra vệ sinh các khu vực','Kiểm tra khóa thiết bị: điện, nước, gas, khóa cửa → quay kết ca','Ghi sổ bàn giao ca','Kiểm tra doanh thu – tiền bàn giao O2C','Xử lý các công việc tồn đọng khác']},
 PV:{n:'Phục vụ',o:['Kiểm tra vệ sinh khu vực (lau dọn bàn, sàn…)','Kiểm tra + vệ sinh + mở thiết bị: máy lạnh, quạt, máy bắt côn trùng, đèn, wifi, tivi','Sắp xếp CCDC theo 5S: bàn ghế, khu shipper, kệ xốt, bộ DC phục vụ, bộ DC vệ sinh, xe clear, xe tiệc'],
  c:['Vệ sinh cuối ca: lau bàn ghế, sàn nhà; thiết bị, CCDC; giặt khăn, giặt thảm; đổ rác','Kiểm tra thông số nhiệt độ & tắt các thiết bị không sử dụng','Bàn giao ca: vấn đề vệ sinh, những vấn đề phát sinh']},
 O2C:{n:'O2C',o:['Kiểm tra vệ sinh khu vực POS','Kiểm tra + vệ sinh + mở thiết bị: máy POS, máy in bill + giấy in bill, máy quẹt thẻ, điện thoại bàn, menu','Sắp xếp CCDC theo 5S: bộ DC Order (rổ lưới, menu, thẻ bàn, phiếu order), bộ DC O2C (menu, thẻ bàn, phiếu order, nón, táp kẹp bill, bộ đàm)','Kiểm tra tiền két, doanh thu và các lưu ý bàn giao của ca tối'],
  c:['Vệ sinh cuối ca theo lịch phân công: khu vực, thiết bị, CCDC; sắp xếp giấy tờ, hóa đơn','Kiểm tra hàng hóa: kiểm đếm hàng tồn, kiểm tra bảo quản','Tắt và sạc pin các thiết bị','Bàn giao ca: in báo cáo doanh thu từ POS, kiểm tiền két, bàn giao tiền cho QL + ký xác nhận, thông tin cho ca sáng mai']},
 PC:{n:'Pha chế',o:['Kiểm tra vệ sinh khu vực','Kiểm tra + vệ sinh + mở thiết bị: tủ lạnh, máy Pepsi, ấm đun siêu tốc','Sắp xếp CCDC – NL theo 5S: dụng cụ pha chế, ly, ống hút, nguyên liệu','Kiểm tra và chuẩn bị hàng hóa: syrup, nước pha sẵn, NVL decor'],
  c:['Vệ sinh cuối ca theo lịch phân công: thiết bị, CCDC, kệ bàn, sàn, cống; đổ rác','Kiểm tra hàng hóa: kiểm đếm hàng tồn, kiểm tra bảo quản','Kiểm tra thông số nhiệt độ & tắt các thiết bị không sử dụng','Bàn giao ca: vấn đề vệ sinh, chất lượng sản phẩm (HSD, màu, mùi), vấn đề phát sinh']},
 KSM:{n:'Kiểm soát món',o:['Kiểm tra vệ sinh khu vực','Kiểm tra + vệ sinh + mở thiết bị: tủ salad, tủ lạnh, lò vi sóng, máy in bill, lò nướng, cân điện tử','Sắp xếp CCDC – NL theo 5S','Kiểm tra và chuẩn bị hàng hóa: các loại xốt, rau decor, salad, canh soup, cá ngừ, đồ mang về'],
  c:['Vệ sinh cuối ca theo lịch phân công: thiết bị, CCDC, kệ bàn, sàn, cống; đổ rác','Kiểm tra hàng hóa: kiểm đếm hàng tồn, kiểm tra bảo quản','Kiểm tra thông số nhiệt độ & tắt các thiết bị không sử dụng','Bàn giao ca: vấn đề vệ sinh, chất lượng sản phẩm (HSD, màu, mùi), vấn đề phát sinh']},
 BEP:{n:'Bếp',o:['Kiểm tra vệ sinh khu vực','Kiểm tra + vệ sinh + mở thiết bị: bếp từ, lò viba, lò nướng, lò chiên gà + dầu chiên, lò nấu cơm, nhiệt độ tủ đông/tủ mát; mở và kiểm tra thông số gas','Sắp xếp CCDC – NL theo 5S','Kiểm tra và chuẩn bị hàng hóa: thịt/rau/xốt/khô; nấu cơm, ép cơm; nướng gà; chiên trứng; nấu canh súp; luộc rau mì, rau cơm, mì udon; sơ chế rau củ; pha bột, định hình gà chiên'],
  c:['Vệ sinh cuối ca theo lịch phân công: thiết bị, CCDC, kệ bàn, sàn, cống; rửa lại rau cơm – rau mì và cấp đá bảo quản; đổ rác','Kiểm tra hàng hóa: kiểm đếm tồn, cấp đông/cấp mát lại, hủy hàng (nếu có), xả hàng cho ca sau','Kiểm tra thông số nhiệt độ & tắt các thiết bị không sử dụng','Bàn giao ca: vấn đề vệ sinh, chất lượng sản phẩm (HSD, màu, mùi), vấn đề phát sinh']}
};
const NOTE6=[
 ['I','Hình ảnh Brand in – out',['Bảng hiệu + logo + đèn + camera','Hình ảnh SP + bộ outside: bảng slogan xốt, standee sân, khung tranh, 2 poster trên kính, khung menu nhóm đại tiệc','Khung sắt kính','Sân + khung để dù + thùng rác','Các quy định bảo vệ']],
 ['II','Không gian trong nhà hàng',['Sàn','Bàn / ghế','Khu quầy xốt','Cây xanh','Quạt / máy lạnh đứng','Tường + tranh','Trần + đèn','Thiết bị khác: wifi + tivi + loa + camera','SẠCH: không mùi lạ, không côn trùng']],
 ['III','Quy trình O2C',['Hình ảnh + tác phong + thái độ: "Bữa ăn vui vẻ"','Chào KH + xác nhận dịch vụ + chỗ ngồi','Gửi bộ phục vụ: menu + thẻ bàn + phiếu order','Tư vấn thêm CTKM / offer món thêm','Xác nhận lại order + thời gian chờ món','Hướng dẫn KH sử dụng chuông khi cần hỗ trợ','Thông báo KH nhận thanh toán sau khi order xong','Xác nhận hình thức thanh toán: tiền mặt / thẻ / chuyển khoản','Gửi hóa đơn cho KH, nhận và thối đúng tiền','Cảm ơn và chúc khách "BỮA ĂN VUI VẺ"']],
 ['IV','Quy trình bưng món',['Gửi món + đặt khay muỗng/nĩa (có rút mâm)','Đọc tên món + xốt','Xin phép tưới xốt cho khách','Kiểm tra và gạch bill khi đưa món cho khách','Nhắc khách trộn đều trước khi ăn (các món xèo)','Cảm ơn và chúc khách "BỮA ĂN VUI VẺ"','Cất số chờ khi trả đủ món','NV/QL đi check bill của khách, hẹn thời gian chờ khi khách đông','Thực hiện đúng quy trình dọn bàn, bàn sạch']],
 ['V','Nhà vệ sinh',['Cửa','Trần + đèn + quạt hút / quạt gió','Tường + kính + các note dán quảng cáo','Bồn rửa + bồn cầu + thùng rác','Xà bông + giấy vệ sinh','Sàn + thảm + ổ thoát nước','Mùi toilet']],
 ['VI','Kiểm tra nhắc lại 3 khu vực FOH – BOH – SBOH',['Phân công nhân viên đúng vị trí đã được chỉ định','Kiểm soát các quy trình 3 khu vực được thực hiện chính xác','Kiểm soát hàng hóa, chuẩn bị SL trữ hàng trước giờ cao điểm','An toàn vệ sinh thực phẩm','An toàn – phòng chống cháy nổ','Thiết bị hoạt động tốt / CCDC sạch sẽ','Các khu vực vệ sinh sạch sẽ + 5S']]
];
/* Note an toàn đỏ. Mục có nguồn '?' là em bổ sung theo quy định chung, chờ anh Hưng xác nhận. */
const SAFE=[
 ['ATVSTP',[['Nhiệt độ tủ đông ≤ -18°C, tủ mát 1–8°C; đo và ghi phiếu theo dõi','PPX'],['Hàng hóa trong HSD; tem nhãn đủ TÊN – NSX – HSD – Bảo quản','PPX'],['Rã đông trong tủ mát, không rã ở nhiệt độ phòng, không cấp đông lần 2','PPX'],['Sống – chín để riêng; hàng không để sát sàn; NL dở dang bọc kín','?'],['Thùng rác có nắp; 3 không: không bụi – không mùi – không ruồi','PPX']]],
 ['PCCC – ATLĐ',[['Mở và kiểm tra thông số gas đầu ca','PPX'],['Thiết bị điện hoạt động tốt; tắt thiết bị không sử dụng','PPX'],['Bình chữa cháy đúng vị trí, còn hạn; lối thoát hiểm không bị chắn','?'],['Sàn bếp khô, không trơn trượt; dao, chảo nóng để đúng vị trí','?'],['Kết ca: khóa điện, nước, gas, cửa → quay clip kết ca','PPX']]]
];
const S5_STD=['Thiết bị sạch','Dụng cụ sạch','Tường – sàn – 4 góc','3 không: không bụi – không mùi – không ruồi','Sàng lọc định kỳ'];
const S5_AREA=[['FOH','Khách hàng'],['FOH','O2C'],['FOH','Phục vụ'],['FOH','Bar'],['SBOH','Khu hỗ trợ'],['BOH','Nhận hàng'],['BOH','Kho'],['BOH','Bếp trong'],['BOH','Phụ bếp']];
const fmtH=m=>Math.floor(m/60)+'h'+(m%60?pad(m%60):'');
const stShort=c=>String(c||'').replace(/^\d+_PPX-/,'').replace('Café-','');
function opStores(){const p=S.profile||{};if(['RGM','ARGM'].includes(p.role)&&p.store)return[p.store];if(p.role==='NV'){const st=S.staff.find(x=>x.id===p.staffId);if(st)return[storeOf(st)]}return mySites().flatMap(x=>x.stores)}
function opStore(){const l=opStores();if(!l.includes(U.opStore))U.opStore=l[0];return U.opStore}
function opKey(kind,code){const t=today();return(kind==='W'?'W'+t.getFullYear()+'-'+pad(isoWeek(t)):kind==='M'?'M'+ymd(t).slice(0,7):'D'+ymd(t))+'|'+(code||opStore())}
const opBox=(kind,code)=>{const k=opKey(kind,code);return[k,(S.ops||{})[k]||{}]};
const curShift=()=>nowMin()<900?0:1;
function hmState(h,b,nm){const tk=h.w.map((w,i)=>!!b['hm'+h.n+'.'+i]);if(tk.every(Boolean))return'done';if(h.w.some((w,i)=>!tk[i]&&nm>=w[1]))return'late';if(h.w.some(w=>nm>=w[0]&&nm<w[1]))return'now';return''}
function safeDone(b,sh){return SAFE.every((g,gi)=>g[1].every((x,i)=>b['sf.'+gi+'.'+i+'.'+sh]))}
function cntPre(b,pre){return Object.keys(b).filter(k=>k.startsWith(pre)&&b[k]).length}
function opCk(k,id,on,label,g){return`<button class="check ${on?'done':''}" data-act="op" data-k="${k}" data-id="${id}"${g?` data-g="${g}"`:''} aria-label="${esc(label)}">${on?'✓':''}</button>`}
function ck2(k,b,head,rows,pre,g){return`<div class="tbl-wrap"><table class="ck2"><thead><tr><th>${esc(head)}</th><th>Ca sáng</th><th>Ca tối</th></tr></thead><tbody>${rows.map((r,i)=>{const lab=Array.isArray(r)?r[0]:r,ask=Array.isArray(r)&&r[1]==='?';return`<tr><td>${esc(lab)}${ask?' <span class="chip ask">chờ xác nhận</span>':''}</td>${[0,1].map(sh=>{const id=pre+i+'.'+sh;return`<td>${opCk(k,id,b[id],lab+(sh?' ca tối':' ca sáng'),g)}</td>`}).join('')}</tr>`}).join('')}</tbody></table></div>`}
function ocHtml(k,b){const nv=myRole()==='NV',g=nv?myGroup():(U.ocG||'QL'),G=OC[g]||OC.QL;
 const tabs=nv?'':`<div class="seg">${Object.entries(OC).map(([id,x])=>`<button class="${id===g?'on':''}" data-act="oc-g" data-g="${id}">${x.n}</button>`).join('')}</div>`;
 return tabs+ck2(k,b,'Bộ mở ca · '+G.n,G.o,'oc.'+g+'.o.',g)+ck2(k,b,'Bộ đóng ca · '+G.n,G.c,'oc.'+g+'.c.',g)}
function n6Html(k,b){return NOTE6.map(([id,n,rows])=>ck2(k,b,`${id}. ${n} (${rows.length} chú ý)`,rows,'n6.'+id+'.')).join('')}
function safeHtml(k,b){return SAFE.map(([n,rows],gi)=>ck2(k,b,n,rows,'sf.'+gi+'.')).join('')}
function s5Html(k,b){let ok=0,ng=0;const rows=S5_AREA.map(([z,a],ai)=>`<tr><td><small class="muted">${z}</small> ${esc(a)}</td>${S5_STD.map((x,si)=>{const v=b['s5.'+ai+'.'+si];if(v==='ok')ok++;if(v==='ng')ng++;return`<td><button class="s5b ${v||''}" data-act="s5" data-k="${k}" data-id="s5.${ai}.${si}" aria-label="${esc(a+': '+x)}">${v==='ok'?'Đạt':v==='ng'?'Lỗi':'–'}</button></td>`}).join('')}</tr>`).join('');
 const tot=S5_AREA.length*S5_STD.length;
 return`<div class="s5-h"><b>5S · 5 tiêu chuẩn sạch</b><span class="muted">${ok} đạt · ${ng} lỗi · ${tot-ok-ng} chưa chấm</span></div>
 <ol class="s5-leg">${S5_STD.map(x=>`<li>${esc(x)}</li>`).join('')}</ol>
 <div class="tbl-wrap"><table class="ck2 s5"><thead><tr><th>Khu vực</th>${S5_STD.map((x,i)=>`<th title="${esc(x)}">${i+1}</th>`).join('')}</tr></thead><tbody>${rows}</tbody></table></div>
 <small class="muted">Bấm ô để đổi: – → Đạt → Lỗi. Theo BỘ QUY ĐỊNH FULL 5S: QL & NV duy trì sắp xếp 5S + tiêu chuẩn 5S sạch.</small>`}
function revSub(){if(!can('dtCH'))return'';const yd=addDays(today(),-1),e=S.revenue[ymd(yd)];return`<div class="row"><span>DSR ngày ${dm(yd)}: <b>${e?money(e.amount):'chưa nhập'}</b></span><span class="spacer"></span>${can('nhapDT','S')?`<button class="btn sm" data-act="edit-rev" data-d="${ymd(yd)}">${e?'Sửa':'Nhập'} DSR</button>`:''}</div>`}
function hmCard(h,k,b,nm){
 const st=hmState(h,b,nm),lb=h.lb||(h.w.length>1?['Ca sáng','Ca tối']:['Xong']),open=U.hmOpen===h.n;
 const subCnt=h.sub==='oc'?`${cntPre(b,'oc.')} việc mở/đóng ca`:h.sub==='n6'?`${cntPre(b,'n6.')}/${NOTE6.reduce((a,x)=>a+x[2].length,0)*2} chú ý`:h.sub==='safe'?`${cntPre(b,'s5.')}/${S5_AREA.length*S5_STD.length} ô 5S`:'';
 const sub=h.sub==='oc'?ocHtml(k,b):h.sub==='n6'?n6Html(k,b):h.sub==='safe'?`<p class="muted" style="margin:0">Note an toàn đỏ nằm ở đầu trang.</p>${s5Html(k,b)}`:h.sub==='rev'?revSub():'';
 return`<div class="hm ${st}${h.n===10?' red':''}" id="hm-${h.n}">
  <div class="hm-h"><span class="hm-n">${h.n}</span>
   <button class="hm-t" data-act="hm-open" data-n="${h.n}" aria-expanded="${open}"><b>${esc(h.t)}</b><small>${h.w.map(w=>fmtH(w[0])+'–'+fmtH(w[1])).join(' & ')} · ${esc(h.tool)}${subCnt?' · '+subCnt:''}${st==='late'?' · <em class="late">Quá giờ</em>':st==='now'?' · <em>Đang diễn ra</em>':''}</small></button>
   <div class="hm-ticks">${h.w.map((w,i)=>{const id='hm'+h.n+'.'+i,on=!!b[id];return`<button class="hm-tk ${on?'on':''}" data-act="op" data-k="${k}" data-id="${id}" aria-pressed="${on}"><span class="check ${on?'done':''}">${on?'✓':''}</span>${lb[i]}</button>`}).join('')}</div>
   <button class="icon-btn" data-act="hm-open" data-n="${h.n}" aria-label="${open?'Thu gọn':'Xem chi tiết'}">${open?'▴':'▾'}</button></div>
  ${open?`<div class="hm-b"><p>${esc(h.d)}</p>${sub}<label class="hm-note">Ghi lỗi / việc cần sửa<input type="text" data-opnote="${k}" data-id="note.${h.n}" value="${esc(b['note.'+h.n]||'')}" placeholder="VD: Máy in bill quầy 2 kẹt giấy, đã báo bảo trì"></label></div>`:(b['note.'+h.n]?`<div class="hm-b sm"><small>Ghi chú: ${esc(b['note.'+h.n])}</small></div>`:'')}
 </div>`}
function opsHead(){
 if(!can('checklist'))return'';
 const L=opStores(),code=opStore(),nm=nowMin(),[,b]=opBox('D'),[,bw]=opBox('W'),[,bm]=opBox('M');
 const dDone=HM_DAY.filter(h=>hmState(h,b,nm)==='done').length,late=HM_DAY.filter(h=>hmState(h,b,nm)==='late').length;
 const wDone=HM_WEEK.filter(h=>bw['w'+h.n]).length,mDone=HM_MONTH.filter(h=>bm['m'+h.n]).length;
 const seg=L.length>1?`<div class="seg">${L.map(c=>`<button class="${c===code?'on':''}" data-act="op-store" data-s="${esc(c)}">${esc(stShort(c))}</button>`).join('')}</div>`:`<span class="chip">${esc(stShort(code))}</span>`;
 const box=(lbl,d,t,cls)=>`<div class="op-k ${cls||''}"><span class="lbl">${lbl}</span><b class="num">${d}/${t}</b><div class="bar${cls==='bad'?' bad':''}"><i style="width:${d/t*100}%"></i></div></div>`;
 return`<div class="panel" id="hm"><div class="panel-h"><div><h2>17 hạng mục vận hành</h2><p class="muted" style="margin:2px 0 0;font-size:.82rem">10 ngày · 4 tuần · 3 tháng. Theo HM công việc và bộ mở – đóng ca PPX.</p></div>${seg}</div>
  <div class="op-sum">${box('Hạng mục ngày',dDone,10,late?'bad':'')}${box('Hạng mục tuần '+isoWeek(today()),wDone,4)}${box('Hạng mục tháng '+(today().getMonth()+1),mDone,3)}</div></div>`}
function safetyPanel(){
 if(!can('checklist'))return'';const[k,b]=opBox('D'),sh=curShift(),d=safeDone(b,sh),tot=SAFE.reduce((a,g)=>a+g[1].length,0);
 const cur=SAFE.reduce((a,g,gi)=>a+g[1].filter((x,i)=>b['sf.'+gi+'.'+i+'.'+sh]).length,0);
 return`<div class="panel safe" id="safe"><div class="panel-h"><div><h2>Note an toàn đỏ · HM 10</h2><p class="muted" style="margin:2px 0 0;font-size:.82rem">ATVSTP và PCCC – ATLĐ. Kiểm tra mỗi ca, chưa đạt thì xử lý ngay trước khi làm việc khác.</p></div><span class="chip ${d?'done':'off'}">${sh?'Ca tối':'Ca sáng'} ${cur}/${tot}</span></div>${safeHtml(k,b)}</div>`}
function hmPanel(){
 if(!can('checklist'))return'';const[k,b]=opBox('D'),nm=nowMin();
 if(myRole()==='NV')return`<div class="panel"><div class="panel-h"><h2>Bộ mở – đóng ca của tôi</h2><span class="muted">${esc(stShort(opStore()))}</span></div>${ocHtml(k,b)}</div>`;
 const list=[...HM_DAY].sort((x,y)=>x.w[0][0]-y.w[0][0]||x.n-y.n);
 return`<div class="panel"><div class="panel-h"><h2>10 hạng mục ngày</h2><span class="muted" style="font-size:.82rem">Theo giờ trong ngày · bấm tên để xem chi tiết</span></div><div class="hm-list">${list.map(h=>hmCard(h,k,b,nm)).join('')}</div></div>`}
function wmPanel(){
 if(!can('checklist')||myRole()==='NV')return'';const[kw,bw]=opBox('W'),[km,bm]=opBox('M');
 const row=(k,b,h,p)=>{const id=p+h.n,on=!!b[id];return`<div class="ck ${on?'on':''}">${opCk(k,id,on,h.t)}<div class="ck-t"><b>${h.n}. ${esc(h.t)}</b></div></div>`};
 return`<div class="panel"><div class="panel-h"><h2>Hạng mục tuần ${isoWeek(today())}</h2><span class="num muted">${HM_WEEK.filter(h=>bw['w'+h.n]).length}/4</span></div><div>${HM_WEEK.map(h=>row(kw,bw,h,'w')).join('')}</div>
  <div class="panel-h"><h2>Hạng mục tháng ${today().getMonth()+1}</h2><span class="num muted">${HM_MONTH.filter(h=>bm['m'+h.n]).length}/3</span></div><div>${HM_MONTH.map(h=>row(km,bm,h,'m')).join('')}</div></div>`}
function seedOps(s){const t=today(),nm=nowMin();s.ops=s.ops||{};
 SITES.flatMap(x=>x.stores).forEach((code,si)=>{const b=s.ops['D'+ymd(t)+'|'+code]={_s:1};
  HM_DAY.forEach(h=>h.w.forEach((w,i)=>{if(nm>=w[1]&&(h.n+si)%4!==1)b['hm'+h.n+'.'+i]=1}));
  if(nm>=660&&si%2===0)SAFE.forEach((g,gi)=>g[1].forEach((x,i)=>{b['sf.'+gi+'.'+i+'.0']=1}));
  if(nm>=600)OC.QL.o.forEach((x,i)=>{if((i+si)%5)b['oc.QL.o.'+i+'.0']=1})})}
'''
rep("const readerName=", DATA + "const readerName=")

# 3. Cảnh báo
a = s.index("  if(can('checklist')){const g=U.clGroup||myGroup();")
b = s.index("\n", a)
s = s[:a] + """  if(can('checklist')&&myRole()!=='NV'){const[,b]=opBox('D'),code=stShort(opStore());const late=HM_DAY.filter(h=>hmState(h,b,nm)==='late');if(late.length)out.push({lv:'yellow',t:`${late.length} hạng mục ngày đã quá giờ nhưng chưa tick · ${code}`,d:late.map(h=>'HM'+h.n+' '+h.t).join('; '),a:'<button class="btn sm" data-act="scroll-to" data-id="hm">Xem 17 hạng mục</button>'});
    [[0,780,'ca sáng'],[1,1200,'ca tối']].forEach(([sh,lim,n])=>{if(nm>=lim&&(sh===1||nm<900)&&!safeDone(b,sh))out.push({lv:'red',t:`Note an toàn đỏ ${n} chưa kiểm xong · ${code}`,d:'ATVSTP, PCCC – ATLĐ phải tick đủ trước '+fmtH(lim)+'.',a:'<button class="btn sm" data-act="scroll-to" data-id="safe">Kiểm ngay</button>'})})}""" + s[b:]

# 4. Bỏ timeline cũ
a = s.index("function timeline(){")
b = s.index("function logbookPanel(){")
s = s[:a] + s[b:]

# 5. Bố cục trang Hôm nay
rep("""  ${revLine()}
  <div class="grid g3">
    <div class="span2">${timeline()||'<div class="panel"><div class="empty">Chức vụ của bạn không có checklist ca.</div></div>'}</div>
    <div class="col">""",
"""  ${opsHead()}
  ${safetyPanel()}
  <div class="grid g3">
    <div class="span2">${hmPanel()||'<div class="panel"><div class="empty">Chức vụ của bạn không theo dõi hạng mục vận hành.</div></div>'}</div>
    <div class="col">
      ${wmPanel()}
      ${revLine()}""")

# 6. Seed cũ dùng clItems
rep("""  const c=s.chk['D'+ymd(t)]=s.chk['D'+ymd(t)]||{};
  clItems('QL').forEach((x,i)=>{if(x.end<=nm&&i%5!==3)c[x.id]=1});
""", "")

# 7. Quyền và thao tác
rep("    case 'chk':return can('checklist','S')&&(myRole()!=='NV'||!ds.g||ds.g===myGroup());",
    "    case 'op':return can('checklist','S')&&(myRole()!=='NV'||(String(ds.id).startsWith('oc.')&&ds.g===myGroup()));\n    case 's5':return can('checklist','S')&&myRole()!=='NV';")
rep("    case 'cl-group':U.clGroup=ds.g;{const y=window.scrollY;render();window.scrollTo(0,y)}return;",
    "    case 'oc-g':U.ocG=ds.g;{const y=window.scrollY;render();window.scrollTo(0,y)}return;\n    case 'op-store':U.opStore=ds.s;{const y=window.scrollY;render();window.scrollTo(0,y)}return;\n    case 'hm-open':U.hmOpen=U.hmOpen===+ds.n?null:+ds.n;{const y=window.scrollY;render();window.scrollTo(0,y)}return;")
a = s.index("    case 'chk':{const c=S.chk[ds.k]")
b = s.index("\n", a)
s = s[:a] + """    case 'op':{S.ops=S.ops||{};const c=S.ops[ds.k]=S.ops[ds.k]||{};if(c[ds.id])delete c[ds.id];else c[ds.id]=1;delete c._s;save();const y=window.scrollY;render();window.scrollTo(0,y);return}
    case 's5':{S.ops=S.ops||{};const c=S.ops[ds.k]=S.ops[ds.k]||{};const v=c[ds.id];if(!v)c[ds.id]='ok';else if(v==='ok')c[ds.id]='ng';else delete c[ds.id];delete c._s;save();const y=window.scrollY;render();window.scrollTo(0,y);return}""" + s[b:]
rep("document.addEventListener('change',e=>{if(e.target.id==='w-date'",
    "document.addEventListener('change',e=>{const on=e.target.dataset&&e.target.dataset.opnote;if(on){if(!can('checklist','S')){toast('Bạn chỉ được xem mục này');return}S.ops=S.ops||{};const c=S.ops[on]=S.ops[on]||{};const v=e.target.value.trim();if(v)c[e.target.dataset.id]=v;else delete c[e.target.dataset.id];delete c._s;save();toast('Đã lưu ghi chú');return}if(e.target.id==='w-date'")

# 8. CSS
CSS = """
/* 17 hạng mục vận hành */
.op-sum{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
.op-k{display:flex;flex-direction:column;gap:4px;background:var(--sunk);border-radius:9px;padding:10px 12px}
.op-k b{font-family:var(--font-head);font-size:1.25rem}
.op-k.bad b{color:var(--red)}
.hm-list{display:flex;flex-direction:column;gap:8px}
.hm{border:1px solid var(--line);border-radius:10px;background:var(--surface)}
.hm.now{border-color:var(--accent);box-shadow:inset 3px 0 0 var(--accent)}
.hm.late{box-shadow:inset 3px 0 0 var(--saffron)}
.hm.done .hm-t b{color:var(--muted);text-decoration:line-through}
.hm-h{display:flex;gap:10px;align-items:center;padding:9px 10px;flex-wrap:wrap}
.hm-n{width:28px;height:28px;border-radius:8px;background:var(--sunk);display:grid;place-items:center;font-weight:700;font-size:.85rem;flex:none}
.hm.red .hm-n{background:var(--red);color:#fff}
.hm.done .hm-n{background:var(--accent);color:var(--accent-ink)}
.hm-t{flex:1;min-width:170px;display:flex;flex-direction:column;align-items:flex-start;text-align:left;border:0;background:none;padding:0;font:inherit;color:inherit;cursor:pointer}
.hm-t b{font-weight:600}
.hm-t small{color:var(--muted);font-size:.78rem}
.hm-t em{font-style:normal;font-weight:600;color:var(--accent)}
.hm-t em.late{color:var(--red)}
.hm-ticks{display:flex;gap:6px;flex-wrap:wrap}
.hm-tk{display:inline-flex;align-items:center;gap:6px;border:1px solid var(--line);background:var(--surface);border-radius:8px;padding:5px 10px 5px 6px;font:inherit;font-size:.8rem;cursor:pointer;color:inherit;min-height:34px}
.hm-tk .check{pointer-events:none;margin:0}
.hm-tk.on{background:var(--accent-soft);border-color:var(--accent)}
.hm-b{padding:10px 12px 12px;display:flex;flex-direction:column;gap:10px;border-top:1px solid var(--line)}
.hm-b.sm{padding:6px 12px}
.hm-b p{margin:0;font-size:.86rem}
.hm-note{display:flex;flex-direction:column;gap:4px;font-size:.78rem;color:var(--muted)}
.hm-note input{font:inherit;font-size:.86rem;padding:7px 9px;border:1px solid var(--line);border-radius:8px;background:var(--surface);color:var(--ink)}
.tbl-wrap{overflow-x:auto;max-width:100%}
.ck2{width:100%;border-collapse:collapse;font-size:.84rem}
.ck2 th{text-align:left;font-size:.74rem;color:var(--muted);font-weight:600;padding:6px 4px;border-bottom:1px solid var(--line)}
.ck2 th:not(:first-child),.ck2 td:not(:first-child){text-align:center;width:62px}
.ck2 th,.ck2 td{white-space:normal}
.ck2 td{padding:6px 4px;border-top:1px solid var(--line);border-bottom:0;vertical-align:middle}
.ck2 td .check{margin:0 auto}
.chip.ask{background:var(--saffron-soft);color:var(--saffron);font-size:.66rem}
.panel.safe{border:2px solid var(--red)}
.panel.safe h2{color:var(--red)}
.s5-h{display:flex;gap:10px;flex-wrap:wrap;align-items:baseline;font-size:.86rem}
.s5-leg{margin:0;padding-left:20px;font-size:.78rem;color:var(--muted);columns:2;column-gap:20px}
.ck2.s5 th:not(:first-child),.ck2.s5 td:not(:first-child){width:auto;min-width:46px}
.s5b{width:100%;min-width:42px;height:30px;border-radius:6px;border:1px solid var(--line);background:var(--surface);font:inherit;font-size:.74rem;cursor:pointer;color:var(--faint)}
.s5b.ok{background:var(--accent-soft);color:var(--accent);border-color:var(--accent);font-weight:600}
.s5b.ng{background:var(--red-soft);color:var(--red);border-color:var(--red);font-weight:600}
@media (max-width:560px){.op-sum{grid-template-columns:1fr}.hm-ticks{width:100%}.hm-tk{flex:1;justify-content:center}.s5-leg{columns:1}}
"""
rep("@media (prefers-reduced-motion:reduce)", CSS + "@media (prefers-reduced-motion:reduce)")

P.write_text(s, encoding='utf-8')
print('OK', len(s))
