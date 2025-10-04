facts={"American(John)","Missile(M1)","Enemy(Nono,America)","Owns(Nono,M1)"}
rules={
    "Weapon(x)":[["Missile(x)"]],
    "Criminal(y)":[["Enemy(x,America)","American(y)","Weapon(z)","Sells(y,z,x)"]]
}

def match(p,f):
    if p.split("(")[0]!=f.split("(")[0]:return None
    pv=p[p.find("(")+1:-1].split(","); fv=f[f.find("(")+1:-1].split(",")
    return dict(zip(pv,fv)) if len(pv)==len(fv) else None

def sub(e,s):
    for k,v in s.items():e=e.replace(k,v)
    return e

def prove(g,seen=set()):
    if g in facts:return True
    if g in seen:return False
    seen.add(g)
    for h,bs in rules.items():
        s=match(h,g)
        if s and any(all(prove(sub(b,s),seen) for b in body) for body in bs):
            return True
    return False

for q in ["Criminal(John)","Weapon(M1)"]:
    print(q,"→",prove(q))