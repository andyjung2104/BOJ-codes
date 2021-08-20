import sys
N,M=map(int,input().split())
T=list(map(int,sys.stdin.readline().split()))
maxx=-1
for i in range(N):
    a=T[i]
    for j in range(i+1,N):
        b=T[j]
        for k in range(j+1,N):
            c=T[k]
            if a+b+c>M:continue
            maxx=max(a+b+c,maxx)
print(maxx)
