#3955
def eed(a,b):
    if a>=b:
        if a==0:return [0,-1]
        elif b==0:
            return [1,0]
        else:
            u=eed(a%b,b)
            return [u[0],u[1]-(a//b)*u[0]]
    else:
        if b==0:return [-1,0]
        if a==0:
            return [0,1]
        else:
            v=eed(a,b%a)
            return [v[0]-(b//a)*v[1],v[1]]
t=int(input())
for _ in range(t):
    ok=True
    ans=0
    k,c=map(int,input().split())
    v=eed(c,k)
    if abs(c*v[0]+k*v[1])>=2:
        ok=False
    else:
        ans=v[0]%k
        x=(ans*c-1)//k
        if x==0:
            ans+=k
            x+=c
            if ans>10**9:
                ok=False
        elif ans==0:
            if c==1:ans=2
            else:ok=False
        
        
    print(ans if ok else 'IMPOSSIBLE')
