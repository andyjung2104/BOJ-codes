N=10**3
isPrime=[True for i in range(N+1)]
isPrime[0]=False
isPrime[1]=False
for i in range(4,N+1,2):
    isPrime[i]=False
for i in range(3,int(N**.5)+1+2,2):
    j=i
    while j*i<N+1:
        isPrime[j*i]=False
        j+=1
n=int(input())
L=list(map(int,input().split()))
cnt=0
for l in L:
    if isPrime[l]:cnt+=1
print(cnt)
