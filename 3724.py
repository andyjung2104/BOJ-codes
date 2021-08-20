import sys
T=int(input())
for t in range(1,1+T):
    M,N=map(int,sys.stdin.readline().split())
    products=[1 for i in range(M)]
    for i in range(N):
        lst=list(map(int,sys.stdin.readline().split()))
        for j in range(M):
            products[j]*=lst[j]
    maxx=0
    for k in range(1,M):
        if products[k]>=products[maxx]:
            maxx=k
    print(maxx+1)
