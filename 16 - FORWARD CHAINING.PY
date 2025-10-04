facts = {"American(John)", "Missile(M1)", "Enemy(Nono,America)", "Owns(Nono,M1)"}
rules = [
    (["Missile(x)"], ["Weapon(x)"]),
    (["Enemy(x,America)", "American(y)", "Weapon(z)", "Sells(y,z,x)"], ["Criminal(y)"])
]

def unify(p, f):
    if p.split("(")[0]!=f.split("(")[0]: return None
    vars=f[f.find("(")+1:-1].split(",")
    return {"x":vars[0]} if "x" in p else None

def forward():
    added=True
    while added:
        added=False
        for conds, concls in rules:
            for fact in list(facts):
                sub=unify(conds[0], fact)
                if sub:
                    for c in concls:
                        nf=c.replace("x",sub["x"])
                        if nf not in facts: facts.add(nf); added=True

forward()
print("Derived facts:",facts)
for q in ["Criminal(John)","Weapon(M1)"]:
    print(q,"→",q in facts)
