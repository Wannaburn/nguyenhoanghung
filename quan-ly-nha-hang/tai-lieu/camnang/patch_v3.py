# Cẩm nang bản 3: Deadline dạng bảng như file gốc; tab vận hành dùng sơ đồ mặt bằng 6 NOTE + mặt bằng An toàn đỏ.
import pathlib,re
R=pathlib.Path(__file__).resolve().parents[2];P=R/'index.html';s=P.read_text(encoding='utf-8')
src=(R/'tai-lieu/camnang/hb_v3.js').read_text(encoding='utf-8')
cut=src.index('/* ---------- Kiến thức vận hành');head=src[:cut];tail=src[cut:]
a=s.index('const DL=[');b=s.index('/* Hình giải phẫu nhà hàng');s=s[:a]+head+s[b:]
a=s.index('const N6_POS=');b=s.index('const QD=[');s=s[:a]+tail+s[b:]
old="hot=DL.filter(x=>dlHot(x,t.getDate(),t.getDay(),nowMin())),hotN=hot.reduce((a,x)=>a+x.it.length,0),amN=hot.reduce((a,x)=>a+x.it.filter(i=>i[1]==='AM').length,0);"
assert s.count(old)==1;s=s.replace(old,"hot=DL.filter(x=>dlHot(x,t.getDate(),t.getDay(),nowMin(),t.getMonth()+1)),hotN=hot.reduce((a,x)=>a+x.it.length,0),amN=hot.reduce((a,x)=>a+x.it.filter(i=>i[3].includes('A')).length,0);")
old="    case 'dl-am':"
assert s.count(old)==1;s=s.replace(old,"    case 'n6-open':U.n6=U.n6===+ds.i?null:+ds.i;{const y=window.scrollY;render();window.scrollTo(0,y)}return;\n"+old)
# màu tím cho khu 5
for blk,val in [('--blue:#2c5f8a; --blue-soft:#dde8f1;','--plum:#7a4a8c; --plum-soft:#ece2f0;'),('--blue:#7fb2dc; --blue-soft:#1c2c3a;','--plum:#c79ad8; --plum-soft:#33253a;')]:
    assert s.count(blk)>=1;s=s.replace(blk,blk+' '+val)
css='''
.dlx-wrap{overflow-x:auto;border:1px solid var(--line);border-radius:10px;-webkit-overflow-scrolling:touch}
.dlx{border-collapse:collapse;width:100%;min-width:1120px;font-size:.84rem}
.dlx th{background:var(--ink);color:var(--bg);text-align:left;padding:8px;font-weight:700;white-space:nowrap}
.dlx td{border-top:1px solid var(--line);padding:7px 8px;vertical-align:top;white-space:normal;background:var(--surface)}
.dlx td+td,.dlx th+th{border-left:1px solid var(--line)}
.dlx .dlx-t{position:sticky;left:0;z-index:1;min-width:150px;max-width:170px;box-shadow:2px 0 0 var(--line)}
.dlx th.dlx-t{background:var(--ink);z-index:2}
.dlx-t b{display:block;font-family:var(--font-head)}
.dlx-t em{display:inline-block;margin-top:4px;font-style:normal;font-weight:700;font-size:.72rem;background:var(--saffron);color:#fff;border-radius:4px;padding:1px 6px}
.dlx-c{min-width:270px}.dlx-f{white-space:nowrap!important}
.dlx .dlx-o{text-align:center;width:54px;padding:6px 4px}
.dlx th.dlx-o{white-space:normal;line-height:1.2;font-size:.74rem}
.dlx tr.hot td{background:var(--saffron-soft)}
.dlx-g td{background:var(--sunk);padding:9px 10px}
.dlx-g b{font-family:var(--font-head);font-size:1rem;margin:0 8px 0 6px}.dlx-g small{color:var(--muted)}
.dlx-gi{display:inline-block;vertical-align:-4px}
.dlx-x{display:inline-grid;place-items:center;width:22px;height:22px;border-radius:50%;background:var(--ink);color:var(--bg);font-weight:700;font-size:.72rem}
.dlx-x.C{background:var(--accent);color:var(--accent-ink)}.dlx-x.A{background:var(--saffron);color:#fff}.dlx-x.O{background:var(--red);color:#fff}
.dlx-hint{display:none;font-size:.78rem;margin:0}
.plan6,.plan8{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:6px;padding:14px;border:3px solid var(--ink);border-radius:12px;background:var(--bg);position:relative}
.plan6{grid-template-areas:"boh boh wc" "lane lane lane" "khach khach o2c" "front front front";grid-template-rows:auto auto minmax(140px,auto) auto;margin-bottom:22px}
.z1{--zc:var(--red);--zs:var(--red-soft)}.z2{--zc:var(--accent);--zs:var(--accent-soft)}.z3{--zc:var(--saffron);--zs:var(--saffron-soft)}
.z4{--zc:var(--blue);--zs:var(--blue-soft)}.z5{--zc:var(--plum);--zs:var(--plum-soft)}.z6{--zc:var(--ink);--zs:var(--sunk)}
.pz{display:grid;grid-template-columns:auto 1fr;align-items:center;align-content:start;gap:4px 8px;text-align:left;border:2px solid var(--zc);background:var(--zs);border-radius:8px;padding:12px;cursor:pointer;color:var(--ink);font:inherit;min-height:84px;min-width:0}
.pz b,.pz small{grid-column:1/-1}.pz b{font-family:var(--font-head);font-size:1.05rem;line-height:1.2}.pz small{color:var(--muted);font-size:.76rem}
.pz-n{width:30px;height:30px;border-radius:50%;background:var(--zc);color:var(--bg);display:grid;place-items:center;font-weight:700;font-family:var(--font-head)}
.pz-i{color:var(--zc);display:flex}
.pz.z4{border-style:dashed;min-height:0}
.pz.on{outline:3px solid var(--ink);outline-offset:2px}.pz:hover{filter:brightness(.97)}
.pz-door{position:absolute;bottom:-13px;right:16%;background:var(--bg);border:2px solid var(--ink);border-radius:6px;padding:0 8px;font-size:.74rem;font-weight:700}
.n6k{border-top:4px solid var(--zc)}.n6k .ana-n{background:var(--zc);color:var(--bg)}
.plan8{grid-template-areas:"kho dong mat" "dien san gas" "pccc san rac"}
.sz{display:grid;grid-template-columns:auto 1fr;gap:6px 10px;align-content:start;border:2px solid var(--zc);background:var(--zs);border-radius:8px;padding:12px;min-height:96px;min-width:0}
.sz.A{--zc:var(--red);--zs:var(--red-soft)}.sz.B{--zc:var(--saffron);--zs:var(--saffron-soft)}
.sz-n{width:30px;height:30px;border-radius:50%;background:var(--zc);color:#fff;display:grid;place-items:center;font-weight:700;font-family:var(--font-head)}
.sz b{display:block;font-family:var(--font-head);line-height:1.2}.sz small{color:var(--muted);font-size:.78rem}
.sz em{grid-column:1/-1;font-style:normal;font-size:.68rem;font-weight:700;color:var(--zc);letter-spacing:.04em}
.sw{display:inline-block;width:12px;height:12px;border-radius:3px;vertical-align:-1px}.sw.A{background:var(--red)}.sw.B{background:var(--saffron)}
@media (max-width:820px){.dlx-hint{display:block}}
@media (max-width:560px){.plan6,.plan8{padding:8px;gap:5px}.pz,.sz{padding:8px}.pz b{font-size:.92rem}.pz-i{display:none}
 .plan8{grid-template-columns:repeat(2,minmax(0,1fr));grid-template-areas:"kho dong" "mat rac" "dien gas" "pccc san"}}
'''
m='@media (max-width:820px){.ana-grid'
assert s.count(m)==1;s=s.replace(m,css.strip()+'\n'+m)
P.write_text(s,encoding='utf-8');print('ok')
