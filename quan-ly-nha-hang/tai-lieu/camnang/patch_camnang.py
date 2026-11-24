# Thêm 4 mục Cẩm nang PPX (deadline timeline, giải phẫu vận hành, giải phẫu quy định, lộ trình module 7–16)
import pathlib
R=pathlib.Path(__file__).resolve().parents[2]
P=R/'index.html';s=P.read_text(encoding='utf-8')
JS=(R/'tai-lieu/camnang/hb_ppx.js').read_text(encoding='utf-8')
def rep(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:70]);s=s.replace(a,b)
rep("profile:{},logbook:[],ops:{}}}","profile:{},logbook:[],ops:{},mod:{}}}")
rep("function vHandbook(){",JS+"\nfunction vHandbook(){")
rep("  const tabs=[['map','Bản đồ công việc'],['path','Lộ trình 90 ngày'],['kb','Kiến thức & công thức']];\n  const body=U.hbDomain?hbChapter(U.hbDomain):U.hbTab==='path'?hbPath():U.hbTab==='kb'?hbKb():hbMap();",
    "  const tabs=[['dl','Deadline công việc'],['vh','Kiến thức vận hành PPX'],['qd','Quy định công ty'],['nganh','Kiến thức ngành'],['map','Bản đồ công việc'],['path','Lộ trình 90 ngày'],['kb','Kiến thức & công thức']];\n  const body=U.hbDomain?hbChapter(U.hbDomain):({dl:hbDeadline,vh:hbOps,qd:hbRules,nganh:hbIndustry,path:hbPath,kb:hbKb}[U.hbTab]||hbMap)();")
rep("hbTab:'map',hbDomain:null};","hbTab:'dl',hbDomain:null};")
rep("    case 'oc-g':U.ocG=ds.g;",
    "    case 'dl-g':U.dlG=ds.k;{const y=window.scrollY;render();window.scrollTo(0,y)}return;\n    case 'dl-am':U.dlAm=!U.dlAm;{const y=window.scrollY;render();window.scrollTo(0,y)}return;\n    case 'qd-open':U.qdOpen=U.qdOpen===+ds.n?null:+ds.n;{const y=window.scrollY;render();window.scrollTo(0,y)}return;\n    case 'mod-done':{S.mod=S.mod||{};if(S.mod[ds.n])delete S.mod[ds.n];else S.mod[ds.n]=1;save();const y=window.scrollY;render();window.scrollTo(0,y)}return;\n    case 'oc-g':U.ocG=ds.g;")
CSS=r"""
/* Cẩm nang PPX: poster theo mẫu ve-hinh-15-mau */
.poster{gap:16px}
.pst-h{display:flex;flex-direction:column;gap:4px;border-bottom:2px solid var(--ink);padding-bottom:12px}
.pst-t{font-size:1.7rem;line-height:1.15}
.pst-h p{margin:0;color:var(--muted);max-width:70ch}
.pst-f{border-top:1px dashed var(--line);padding-top:10px;font-size:.76rem;color:var(--faint)}
.who-c{display:inline-block;min-width:34px;text-align:center;font-size:.66rem;font-weight:700;border-radius:5px;padding:1px 5px;margin-right:6px;vertical-align:1px}
.who-c.CH{background:var(--accent-soft);color:var(--accent)}.who-c.AM{background:var(--saffron-soft);color:var(--saffron)}.who-c.OM{background:var(--red-soft);color:var(--red)}.who-c.RSC{background:var(--blue-soft);color:var(--blue)}
.tl2{display:flex;flex-direction:column;gap:18px}
.tl2-sec{display:flex;flex-direction:column;position:relative}
.tl2-g{display:flex;gap:10px;align-items:center;margin-bottom:6px}
.tl2-g b{font-family:var(--font-head);font-size:1.15rem;display:block}.tl2-g small{color:var(--muted)}
.tl2-ico{width:44px;height:44px;border-radius:50%;background:var(--ink);color:var(--bg);display:grid;place-items:center;flex:none}
.tl2-n{display:grid;grid-template-columns:150px minmax(0,1fr);gap:4px 16px;position:relative;padding:8px 0 8px 40px;border-left:3px solid var(--line);margin-left:20px}
.tl2-dot{position:absolute;left:-9px;top:14px;width:15px;height:15px;border-radius:50%;background:var(--surface);border:3px solid var(--ink)}
.tl2-n.hot{background:var(--saffron-soft);border-radius:0 10px 10px 0}.tl2-n.hot .tl2-dot{background:var(--saffron);border-color:var(--saffron)}
.tl2-time{display:flex;flex-direction:column}.tl2-time b{font-family:var(--font-head)}.tl2-time small{color:var(--muted);font-size:.74rem}.tl2-time em{font-style:normal;font-weight:700;font-size:.74rem;color:var(--saffron)}
.tl2-n ul{margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:5px}
.tl2-n li{display:flex;align-items:flex-start;font-size:.88rem;line-height:1.4}.tl2-n li small{color:var(--muted)}
.anat{width:100%;height:auto;display:block;background:var(--bg);border:1px solid var(--line);border-radius:10px}
.anat .wall{fill:var(--surface);stroke:var(--ink);stroke-width:3}.anat .roof{fill:var(--red-soft);stroke:var(--ink);stroke-width:3}
.anat .sign{fill:var(--red);stroke:var(--ink);stroke-width:2}.anat .signt{fill:#fff;font:700 28px var(--font-head);text-anchor:middle;letter-spacing:2px}
.anat .ground{stroke:var(--ink);stroke-width:4}.anat .part{stroke:var(--ink);stroke-width:2}
.anat .door,.anat .glass,.anat .room,.anat .tbl,.anat .counter,.anat .std{fill:var(--sunk);stroke:var(--ink);stroke-width:2}
.anat .kit{fill:var(--saffron-soft);stroke:var(--ink);stroke-width:2}.anat .burn{fill:var(--red);stroke:var(--ink)}
.anat .fridge{fill:var(--blue-soft);stroke:var(--ink);stroke-width:2}.anat .gas{fill:var(--red-soft);stroke:var(--red);stroke-width:3}
.anat .skin{fill:#f1c9a5;stroke:var(--ink);stroke-width:2.5}.anat .cap{fill:var(--red);stroke:var(--ink);stroke-width:2}
.anat .shirt{fill:var(--red-soft);stroke:var(--ink);stroke-width:2.5}.anat .apron{fill:var(--surface);stroke:var(--ink);stroke-width:2}
.anat .badge{fill:var(--saffron);stroke:var(--ink)}.anat .pants{fill:none;stroke:var(--ink);stroke-width:3}.anat .shoe{fill:var(--ink)}
.anat .box{fill:var(--saffron-soft);stroke:var(--ink);stroke-width:2}.anat .cash{fill:var(--accent-soft);stroke:var(--ink);stroke-width:2}.anat .heart{fill:var(--red)}
.anat .tiny{fill:var(--muted);font:600 20px var(--font-body)}
.anat .ld{fill:none;stroke:var(--muted);stroke-width:2;stroke-dasharray:6 4}
.anat .cn{fill:var(--ink)}.anat .cnt{fill:var(--bg);font:700 20px var(--font-head);text-anchor:middle}
.anat .lb1{fill:var(--ink);font:700 30px var(--font-head)}.anat .lb2{fill:var(--muted);font:500 25px var(--font-body)}
.anat.road .rd{fill:none;stroke:var(--sunk);stroke-width:46;stroke-linecap:round;stroke-linejoin:round}
.anat.road .rdl{fill:none;stroke:var(--faint);stroke-width:3;stroke-dasharray:14 12}
.anat.road .stop{fill:var(--accent);stroke:var(--surface);stroke-width:6}.anat.road .stopn{fill:var(--accent-ink);font:700 32px var(--font-head);text-anchor:middle}
.ana-grid,.qd-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;align-items:start}
.ana-c{border:1px solid var(--line);border-radius:10px;padding:12px 14px;display:flex;flex-direction:column;gap:8px;min-width:0}
.ana-c.wide{grid-column:1/-1}.ana-c.red{border:2px solid var(--red)}.ana-c.red h3{color:var(--red)}
.ana-h{display:flex;gap:10px;align-items:center;border:0;background:none;padding:0;text-align:left;font:inherit;color:inherit;width:100%}
button.ana-h{cursor:pointer}
.ana-h h3{display:flex;flex-direction:column}.ana-h h3 small{font:500 .76rem var(--font-body);color:var(--muted)}
.ana-n{width:30px;height:30px;border-radius:50%;background:var(--ink);color:var(--bg);display:grid;place-items:center;font-weight:700;flex:none}
.ana-c ul,.ana-c ol{margin:0;padding-left:20px;display:flex;flex-direction:column;gap:4px;font-size:.86rem;line-height:1.45}
.ana-c p{margin:0;font-size:.84rem}
.ana-c .lbl{display:block;margin-top:4px}
.qd.mini{opacity:.85}.qd .src{display:flex;gap:6px;flex-wrap:wrap}
.hm17,.s5x{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px 20px}
.hm17 small{color:var(--muted)}
.n6g{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.n6g ul{font-size:.8rem}
.sw{display:inline-block;padding:2px 7px;border-radius:4px;font-size:.72rem;font-weight:600;border:1px solid var(--line);margin:1px 2px 1px 0}
.sw-t td,.sw-t th{white-space:normal;padding:5px 6px;font-size:.8rem}
.big5{list-style:none;padding:0!important}
.big5 li{display:flex;gap:10px;align-items:center}.big5 b{width:30px;height:30px;border-radius:8px;background:var(--accent);color:var(--accent-ink);display:grid;place-items:center;flex:none}
.sf2{display:flex;flex-direction:column;gap:8px}
.mod-list{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.mod{border:1px solid var(--line);border-radius:10px;padding:12px 14px;display:flex;flex-direction:column;gap:8px}
.mod.on{border-color:var(--accent);background:var(--accent-soft)}
.mod-h{display:flex;gap:10px;align-items:flex-start}.mod-h>div{flex:1;min-width:0}.mod-h small{color:var(--muted)}
.mod-i{width:40px;height:40px;border-radius:50%;background:var(--accent);color:var(--accent-ink);display:grid;place-items:center;flex:none}
.mod ul{margin:0;padding-left:20px;font-size:.86rem;display:flex;flex-direction:column;gap:3px}
@media (max-width:820px){.ana-grid,.qd-grid,.hm17,.s5x,.mod-list{grid-template-columns:minmax(0,1fr)}.n6g{grid-template-columns:repeat(2,minmax(0,1fr))}.tl2-n{grid-template-columns:minmax(0,1fr);padding-left:24px;margin-left:12px}.pst-t{font-size:1.35rem}}
@media (max-width:460px){.n6g{grid-template-columns:minmax(0,1fr)}}
"""
rep("@media (prefers-reduced-motion:reduce)",CSS+"@media (prefers-reduced-motion:reduce)")
P.write_text(s,encoding='utf-8');print('OK',len(s))
