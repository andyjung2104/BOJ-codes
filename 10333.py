#10333


d,n,b=map(int,input().split())
rods=[]
for i in range(n):
    p,h=map(int,input().split())
    rods.append((p,h))
ans=10**12
for bounce in range(b+1):
    w=d/(2*(bounce+1))
    vx,vy=0,0
    minv=0
    is45=True
    for rod in rods:
        x=rod[0]
        h=rod[1]
        while x-2*w>=0:
            x-=(2*w)
        if x==0:
            minv=10**12
            break
        vy=(2*h*w*w/(2*w*x-x*x))**.5
        vx=((2*w*x-x*x)/(2*h))**.5
        v=2*h*w*w/(2*w*x-x*x)+(2*w*x-x*x)/(2*h)
        if is45:
            if not 2*h*w<2*w*x-x*x:
                is45=False
        minv=max(minv,v)
    if is45:
        ans=2*w
    else:
        ans=min(ans,minv)
print(ans**.5)
