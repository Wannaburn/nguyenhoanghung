import json,sys;sys.path.insert(0,'pq')
from perm import ROLES,M,STORES
perm={k:dict(zip(['OM','AM','RGM','ARGM','NV'],lv)) for k,g,t,*lv,n in [(r[0],r[1],r[2],*r[3:8],r[8]) for r in M]}
rows=[[r[0],r[1],r[2]] for r in M]
roles=[[r[0],r[1],r[4],r[5]] for r in ROLES]
stores=[[s[0],s[1]] for s in STORES]
open('pq/perm.js','w').write('/* ---------- Phân quyền (đồng bộ với file Phan-quyen-app-PPX.xlsx) ---------- */\nconst PERM='+json.dumps(perm,ensure_ascii=False)+';\nconst PERM_ROWS='+json.dumps(rows,ensure_ascii=False)+';\nconst ROLE_INFO='+json.dumps(roles,ensure_ascii=False)+';\nconst STORE_LIST='+json.dumps(stores,ensure_ascii=False)+';\n')
