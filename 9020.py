def pri(n):
    sieve=[True]*n
    m=int(n**.5)
    for j in range(4,n,2):
        sieve[j]=False
    for i in range(3,m+1,2):
        if sieve[i]:
            for j in range(2*i,n,i):
                sieve[j]=False
    sieve[0]=False
    sieve[1]=False
    return sieve
t=int(input())
s=pri(10000+1)
for _ in range(t):
    u=int(input())
    if u==4:
        print('2 2')
        continue
    ans=0
    for i in range(3,u//2+1,2):
        if s[i] and s[u-i]:
            ans=i
    print(ans,u-ans)
