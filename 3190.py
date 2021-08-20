#3190
N=int(input())
k=int(input())
L=[[-1 for i in range(0,N+2)] for j in range(0,N+2)]
for i in range(1,N+1):
    for j in range(1,N+1):
        L[i][j]=0
dx=[1,0,-1,0]
dy=[0,1,0,-1]
S=[(1,1)]
for i in range(k):
    a,b=map(int,input().split())
    L[a][b]=1

    
l=int(input())
time=0
direction=0
ended=False
CHNG=[]
for i in range(l):
    x,c=input().split()
    x=int(x)
    while time<x:
        print(S,time)
        time+=1
        nexthead=list(S[-1])
        nexthead[0]+=dx[direction]
        nexthead[1]+=dy[direction]
        if tuple(nexthead) in S:
            ended=True
            break
        S.append(tuple(nexthead))
        u=L[nexthead[0]][nexthead[1]]
        if u==0:
            del S[0]
        elif u<0:
            ended=True
            break
    if c=='D':
        direction+=1
        direction%=4
    elif c=='L':
        direction+=3
        direction%=4
    if ended:
        print(time)
        break
while not ended:
    time+=1
    nexthead=list(S[-1])
    nexthead[0]+=dx[direction]
    nexthead[1]+=dy[direction]
    u=L[nexthead[0]][nexthead[1]]
    if tuple(nexthead) in S:
        ended=True
        print(time)
    elif u==0:
        del S[0]
    elif u<0:
        ended=True
        print(time)
        
