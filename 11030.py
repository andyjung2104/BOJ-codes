#11030


def primes(n,p0=0):
    N=n
    if n%2==0:
        n//=2
        while n%2==0:
            n//=2
        ans=primes(n,1)
        ans.add(2)
        return ans
    for i in range(p0+2,int(N**.5)+1,2):
        if n%i==0:
            n//=i
            while n%i==0:
                n//=i
            ans=primes(n,i)
            ans.add(i)
            return ans
    if N>1:return {N}
    return set()
def eulerphi(n):
    N=n
    factors=primes(n)
    for f in factors:
        N//=f
        N*=(f-1)
    return N

a,b=map(int,input().split())
phi_a=eulerphi(a)
m1=1
m2=1
for i in range(b-1):
    m1%=phi_a
    m1=pow(a,m1,phi_a)
print(a**m1)
