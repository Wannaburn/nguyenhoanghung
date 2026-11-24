/* Kiến thức vận hành PPX (bản 2): hình 1 mổ xẻ nhà hàng theo 6 NOTE QL, hình 2 "An toàn đỏ".
   Nguồn: Bộ mở - đóng ca các vị trí & 6 note.xlsx; sổ tay quy trình PPX (bảo quản, HSD, sự cố tủ); 2025 - QĐ hủy NVL (kiểm hàng ≤ 3 giờ). */
const N6_POS=[[300,138],[450,520],[590,500],[640,430],[390,245],[690,520]];
const N6_SUB=['Bảng hiệu · outside · bảo vệ','Sàn · bàn ghế · đèn · sạch','Đón · order · thanh toán','Gửi món · xốt · dọn bàn','Cửa · bồn · sàn · mùi','Phân công · hàng · an toàn'];
const N6_SHORT=['Brand','Không gian','O2C','Bưng món','Nhà vệ sinh','F-B-S OH'];
function svgRestaurant(){
 const T=(x,y)=>[Math.round(.75*x-100),Math.round(.75*y+60)];
 const pts=NOTE6.map(([id,n,r],i)=>{const[X,Y]=T(...N6_POS[i]);return[i+1,X,Y,`Note ${id} · ${N6_SHORT[i]} (${r.length})`,N6_SUB[i]]});
 return`<svg class="anat" viewBox="0 0 1080 560" role="img" aria-label="Mổ xẻ nhà hàng Papaxốt theo 6 NOTE QL">
 <g transform="translate(-100 60) scale(.75)">
 <rect x="230" y="170" width="620" height="420" class="wall"/><path d="M210 175 L540 70 L870 175 Z" class="roof"/>
 <rect x="420" y="112" width="240" height="44" rx="6" class="sign"/><text x="540" y="144" class="signt">PAPAXỐT</text>
 <line x1="160" y1="590" x2="920" y2="590" class="ground"/>
 <rect x="250" y="440" width="70" height="150" class="door"/><rect x="250" y="250" width="70" height="120" class="glass"/><path d="M180 590 v-90 h40 v90" class="std"/>
 <line x1="345" y1="370" x2="345" y2="590" class="part"/>
 ${[[400,520],[500,520]].map(([x,y])=>`<rect x="${x-35}" y="${y}" width="70" height="10" class="tbl"/><line x1="${x-25}" y1="${y+10}" x2="${x-25}" y2="590" class="part"/><line x1="${x+25}" y1="${y+10}" x2="${x+25}" y2="590" class="part"/>`).join('')}
 <rect x="560" y="470" width="60" height="120" class="counter"/>
 <line x1="640" y1="300" x2="640" y2="590" class="part"/><path d="M640 430 h-40" class="part"/><rect x="650" y="470" width="80" height="120" class="kit"/><circle cx="672" cy="470" r="9" class="burn"/><circle cx="708" cy="470" r="9" class="burn"/>
 <rect x="745" y="420" width="90" height="170" class="fridge"/><line x1="745" y1="500" x2="835" y2="500" class="part"/>
 <rect x="650" y="190" width="185" height="100" class="room"/><rect x="440" y="190" width="120" height="110" class="room"/><rect x="350" y="190" width="80" height="110" class="room"/>
 </g>
 ${calloutR(pts)}
 </svg>`}
function svgSafety(){
 const pts=[[1,105,450,'Tủ đông','≤ -18°C · đo, ghi phiếu'],[2,225,450,'Tủ mát','1–8°C · rã đông tại đây'],[3,165,215,'Kệ kho','HSD · tem nhãn · sống–chín riêng'],[4,320,600,'Thùng rác','Có nắp · không bụi, mùi, ruồi'],[5,582,592,'Bình gas','Kiểm đầu ca · khóa kết ca'],[6,505,225,'Tủ điện','Thiết bị tốt · tắt khi không dùng'],[7,420,340,'Bình chữa cháy','Đúng vị trí · còn hạn · lối thoát'],[8,375,505,'Sàn · dao · chảo','Sàn khô · dao, chảo đúng chỗ']];
 return`<svg class="anat safe-fig" viewBox="0 0 1080 700" role="img" aria-label="Mặt cắt bếp Papaxốt với 8 điểm an toàn đỏ">
 <rect x="30" y="120" width="580" height="520" class="wall"/><line x1="10" y1="640" x2="630" y2="640" class="ground"/>
 <text x="320" y="95" class="lb1" text-anchor="middle">BẾP · KHO</text>
 ${[180,250,320].map(y=>`<line x1="50" y1="${y}" x2="280" y2="${y}" class="part"/>`).join('')}
 ${[[60,140,40],[120,148,32],[190,140,40],[60,210,40],[150,214,36],[215,206,44],[70,280,40],[160,284,36]].map(([x,y,h])=>`<rect x="${x}" y="${y}" width="50" height="${h}" class="box"/><rect x="${x+8}" y="${y+8}" width="22" height="10" class="tag"/>`).join('')}
 <rect x="50" y="380" width="110" height="260" class="fridge"/><rect x="170" y="380" width="110" height="260" class="fridge"/>
 <text x="105" y="420" class="tiny" text-anchor="middle">-18°C</text><text x="225" y="420" class="tiny" text-anchor="middle">1–8°C</text>
 <line x1="148" y1="470" x2="148" y2="530" class="part"/><line x1="182" y1="470" x2="182" y2="530" class="part"/>
 <rect x="470" y="180" width="70" height="90" class="panel"/><path d="M510 195 l-14 30 h12 l-8 28 l22-36 h-12 l8-22z" class="bolt"/>
 <rect x="405" y="315" width="30" height="70" rx="8" class="ext"/><rect x="412" y="305" width="16" height="12" class="ext"/>
 <rect x="300" y="190" width="90" height="34" class="exit"/><text x="345" y="214" class="exitt">EXIT</text>
 <rect x="300" y="495" width="150" height="16" class="tbl"/><line x1="312" y1="511" x2="312" y2="640" class="part"/><line x1="438" y1="511" x2="438" y2="640" class="part"/>
 <path d="M340 492 l50 -6 l-2 6z" class="knife"/>
 <rect x="460" y="495" width="100" height="145" class="kit"/><circle cx="485" cy="495" r="10" class="burn"/><circle cx="530" cy="495" r="10" class="burn"/><path d="M505 488 v-22 h50 v22" class="pan"/>
 <rect x="565" y="545" width="34" height="95" rx="10" class="gas"/><path d="M582 545 v-30 h-30" class="pipe"/>
 <rect x="300" y="585" width="40" height="55" class="bin"/><line x1="296" y1="580" x2="344" y2="580" class="ground"/>
 ${calloutR(pts)}
 </svg>`}
function hbOps(){
 const nd=NOTE6.reduce((a,x)=>a+x[2].length,0);
 const n6=`<div class="n6c">${NOTE6.map(([id,n,r],i)=>`<div class="ana-c"><div class="ana-h"><span class="ana-n">${i+1}</span><h3>Note ${id} · ${esc(n)}<small>${r.length} chú ý · ${esc(N6_SUB[i])}</small></h3></div><ol>${r.map(x=>`<li>${esc(x)}</li>`).join('')}</ol></div>`).join('')}</div>`;
 const card=(n,t,body,cls)=>`<div class="ana-c ${cls||''}"><div class="ana-h"><span class="ana-n">${n}</span><h3>${t}</h3></div>${body}</div>`;
 const li=a=>`<ul>${a.map(x=>`<li>${x}</li>`).join('')}</ul>`;
 const q=' <span class="chip ask">chờ xác nhận</span>';
 const sA=card('A','ATVSTP · an toàn vệ sinh thực phẩm',li(SAFE[0][1].map(([x,s])=>esc(x)+(s==='?'?q:'')))+
  `<span class="lbl">Bảo quản & HSD</span>`+li(['Tủ đông -18°C, tủ mát 1–8°C; vùng nguy hiểm 5–60°C','Kiểm nhiệt độ tủ 3 lần/ngày, ghi phiếu theo dõi','Rã đông lần 1: HSD 12h; lần 2: 6h; không cấp đông lại lần 2','HSD: đông lạnh 30 ngày · mì miến 96h · kim chi 14 ngày · rau 72h · bánh mì 24h','Rau sơ chế: ngâm muối 3 phút (4gr/1L), rửa 3 lần','Kiểm hàng nhập trễ nhất 3 giờ sau khi xe xuống hàng']),'red');
 const sB=card('B','PCCC – ATLĐ · an toàn lao động',li(SAFE[1][1].map(([x,s])=>esc(x)+(s==='?'?q:'')))+
  `<span class="lbl">Kết ca</span>`+li(['Tắt thiết bị không dùng, kiểm nhiệt độ tủ','Khóa điện, nước, gas, cửa → quay clip kết ca','Bàn giao bảo vệ, ký sổ']),'red');
 const sC=card('C','Khi có sự cố',li(['<b>Tủ đông/mát hư:</b> báo AM → chuyển hàng vào thùng xốp + đá khô 2kg/20kg → giữ hàng hoặc chuyển về BTT','<b>Hàng nhập lỗi, cận/hết date:</b> nhắn group bếp @QC trong ngày; quá hạn không có QC xác nhận thì CH chịu đền','<b>Hàng hết HSD tại CH:</b> hủy có tính đền, phải trả hàng về Bếp tổng kèm phiếu','<b>Tai nạn, cháy nổ:</b> ưu tiên an toàn người, báo QL ca → AM → OM']),'red');
 return poster('Mẫu 10 · Sơ đồ giải phẫu','Mổ xẻ Papaxốt theo 6 NOTE',`6 khu vực QL kiểm mỗi ca sáng và ca tối, tổng ${nd} chú ý. Sau đó là hình "An toàn đỏ".`,
  svgRestaurant()+n6+
  `<div class="pst-h safe-h"><span class="lbl">Hình 2</span><h2 class="pst-t">An toàn đỏ</h2><p>8 điểm nguy cơ trong bếp – kho. Không đạt thì dừng việc khác để xử lý ngay.</p></div>`+
  svgSafety()+`<div class="ana-grid">${sA}${sB}${sC}</div>`,
  'Nguồn: Bộ mở – đóng ca các vị trí & 6 note, sổ tay quy trình PPX, QĐ hủy bill – hủy NVL 2025. Hình minh hoạ, không theo mặt bằng cửa hàng cụ thể.')}
