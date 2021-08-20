def mod_inv(a,mod):
    return pow(a,mod-2,mod)

def C(n,r,mod=10**9+7):
    r=min(r,n-r)
    ans=1
    for i in range(n-r+1,n+1):
        ans*=i
        ans%=mod
    #print(ans)
    rfac=1
    for u in range(1,r+1):
        rfac*=u
        rfac%=mod
        #print(rfac)
    #print(ans,rfac)
    return (ans*mod_inv(rfac,mod))%mod
n,k=map(int,input().split())
MOD=10**9+7
S=[n,(n*n+n)//2]


for j in range(2,k+1):
    ans=pow(n+1,j+1,MOD)-1
    for i in range(j):
        ans-=S[i]*C(j+1,i)
        ans%=MOD
    S.append(mod_inv(j+1,MOD)*ans)
print(S[-1]%MOD)
#print(C(4,2))
