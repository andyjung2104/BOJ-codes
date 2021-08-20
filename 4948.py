import sys
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
a=[]
while True:
    n=int(sys.stdin.readline())
    if n==0:break
    a.append(n)
    
s=pri(2*max(a)+1)
for u in a:
    print(s[(u+1):(2*u+1)].count(True))
