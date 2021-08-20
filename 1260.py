import sys
N,M,V=map(int,input().split())
P=[[[0] for i in range(N)] for j in range(N)]
for i in range(M):
    a,b=map(int,sys.stdin.readline().split())
    P[a-1][b-1]=1
    P[b-1][a-1]=1
wentto=[V]
def nextDFS(i):
    p=P[i-1]
    for j in range(len(p)):
        if p[j]==1 and (j+1) not in wentto:
            wentto.append(j+1)
            return j
    return -1
wentto2=[V]
def connected(i):
    p=P[i-1]
    F=[]
    for j in range(len(p))
        if p[j]==1:F.append(j)
    return F
for i in range(N):
    
s=V-1
while s>=0:
    print(s+1)
    s=nextDFS(s+1)
    
