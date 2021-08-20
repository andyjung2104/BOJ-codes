N=10**6
isPrime=[True for i in range(N+1)]
isPrime[0]=False
isPrime[1]=False
for i in range(4,N+1,2):
    isPrime[i]=False
for i in range(3,int(N**.5)+1+2,2):
    j=i
    while j*i<1+N:
        isPrime[j*i]=False
        j+=1
m,n=map(int,input().split())
for p in range(m,n+1):
    if isPrime[p]:print(p)
