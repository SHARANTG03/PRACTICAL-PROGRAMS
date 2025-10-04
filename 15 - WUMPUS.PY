import random
class Wumpus:
    def __init__(s,n=4):
        s.n=n; s.p={(random.randrange(n),random.randrange(n)) for _ in range(3)}-{(0,0)}
        s.w=s._pl(s.p|{(0,0)}); s.g=s._pl(s.p|{s.w,(0,0)}); s.a=(0,0); s.alive=1; s.gold=0
    def _pl(s,e):
        p=(random.randrange(s.n),random.randrange(s.n))
        while p in e: p=(random.randrange(s.n),random.randrange(s.n))
        return p
    def adj(s,pos):
        x,y=pos
        return [(x+dx,y+dy) for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)] if 0<=x+dx<s.n and 0<=y+dy<s.n]
    def perc(s,p):
        r=[]
        if p==s.g:r+=['glitter']
        if s.w in s.adj(p):r+=['stench']
        if any(a in s.p for a in s.adj(p)):r+=['breeze']
        return r
    def move(s,p):
        s.a=p
        if p in s.p or p==s.w:s.alive=0;print("☠ Died",p)
        if p==s.g:s.gold=1;print("💰 Gold",p)
def agent(w):
    f,vis=[(0,0)],set()
    while f and w.alive and not w.gold:
        p=f.pop(0);w.move(p);vis|={p};print("At",p,"→",w.perc(p))
        if not any(x in w.perc(p)for x in['stench','breeze']):f+=[n for n in w.adj(p)if n not in vis and n not in f]
w=Wumpus();agent(w)