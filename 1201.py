#1201
n,m,k=map(int,input().split())
if n<m+k-1:
    print(-1)
elif n>m*k:
    print(-1)
else:
    L=list(range(1,n+1))
    if m!=1:
        num=(n-k)//(m-1)
        r=(n-k)%(m-1)
    else:
        num=1
        r=0
    S=[k]
    for n in range(m-1):
        if n<r:S.append(num+1)
        else:S.append(num)
    #print(S)
    SS=[]
    tmp=1
    temp=[]
    for s in S:
        for t in range(s):
            temp.append(tmp+t)
        tmp+=s
        print(*temp[::-1],end=' ')
        temp=[]
