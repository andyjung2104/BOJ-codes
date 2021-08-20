import math
def prime_list(n):
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
A,B=map(int,input().split())
isPrime=prime_list(10**7+5)
N=2
cnt=0
while N<=math.log(B,2):
    for i in range(math.ceil(A**(1/N))-3,4+math.floor(B**(1/N))):
        if isPrime[i]:
            if A<=i**N<=B:
                cnt+=1
    N+=1
print(cnt)
