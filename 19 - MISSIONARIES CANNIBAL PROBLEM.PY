from collections import deque
start = (3,3,'L',0,0)
goal  = (0,0,'R',3,3)
def valid(m,c): 
    return (m==0 or m>=c) and 0<=m<=3 and 0<=c<=3
def successors(state):
    mL,cL,boat,mR,cR = state
    moves=[(1,0),(2,0),(0,1),(0,2),(1,1)]  
    result=[]
    for m,c in moves:
        if boat=='L':
            nmL,ncL,nb,nmR,ncR=mL-m,cL-c,'R',mR+m,cR+c
        else:
            nmL,ncL,nb,nmR,ncR=mL+m,cL+c,'L',mR-m,cR-c
        if valid(nmL,ncL) and valid(nmR,ncR):
            result.append((nmL,ncL,nb,nmR,ncR))
    return result
def bfs(start,goal):
    q=deque([[start]])
    visited={start}
    while q:
        path=q.popleft(); state=path[-1]
        if state==goal: return path
        for nxt in successors(state):
            if nxt not in visited:
                visited.add(nxt); q.append(path+[nxt])
    return None
solution=bfs(start,goal)
print("Solution path:")
for step in solution: print(step)