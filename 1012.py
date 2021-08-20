import sys
T=int(input())
for t in range(T):
    m,n,k=map(int,sys.stdin.readline().split())
    L=[[0 for i in range(n+2)] for j in range(m+2)]
    for i in range(k):
        a,b=map(int,sys.stdin.readline().split())
        L[a+1][b+1]=1
    cnt=0
    for a in range(1,m+1):
        for b in range(1,n+1):
            if L[a][b]==1:
                if L[a-1][b]+L[a+1][b]+L[a][b-1]+L[a][b+1]==0:
                    cnt+=1
                L[a][b]=0
    print(cnt)
