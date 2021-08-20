#7516

#n^2의 약수개수
def primes(n):
    N=n
    u=0
    for i in range(2,int(N**.5)+1):
        if n%i==0:
            u=0
            while n%i==0:
                n//=i
                u+=1
            #print(n)
            return primes(n)*(2*u+1)
    if N>1:return 3
    else:return 1

t=int(input())
for i in range(1,1+t):
    print('Scenario #%d:' % i)
    ans=1
    n=int(input())
    if n==1:print(1)
    else:
        y=primes(n)
        print((y+1)//2)
    print()
