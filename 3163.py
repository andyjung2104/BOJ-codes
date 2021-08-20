#3163

import sys

T=int(input())
for _ in range(T):
    N,L,k=map(int,sys.stdin.readline().split())
    Id=[]
    tleft=set()
    tright=set()
    
    for i in range(N):
        p,a=map(int,sys.stdin.readline().split())
        Id.append(a)
        if a>0:
            t=L-p
            tright.add(t)
        else:
            tleft.add(p)
    fell=0
    list_t=list(tleft|tright)
    list_t.sort()
    tindex=0
    st=0
    end=N-1
    fall=0
    while True:
        fall=[]
        time=list_t[tindex]
        if time in tleft:
            fell+=1
            fall.append(st)
            #print(Id[fall])
            st+=1
        if time in tright:
            fell+=1
            fall.append(end)
            #print(Id[fall])
            end-=1
        if fell>=k:
            break
        tindex+=1
    if fell>k:print(min(Id[i] for i in fall))
    elif fell==k:print(max(Id[i] for i in fall))
