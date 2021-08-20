#9735
N=int(input())
for n in range(N):
    a,b,c,d=map(int,input().split())
    ans=[]
    for x in range(1000000+1):
        if a*x**3+b*x**2+c*x+d==0:
            ans.append(x)
            break
    if len(ans)==0:
        for y in range(-1,-1000000-1,-1):
            if a*y**3+b*y**2+c*y+d==0:
                ans.append(y)
                break
    print('정수근: %d' % ans[0])
    A=a*ans[0]
    B=(a*ans[0]+b)*ans[0]
    C=-d
    D=B**2-4*A*C
    if D>0:
        ans.append((-B+D**.5)/(A*2))
        ans.append((-B-D**.5)/(A*2))
    elif D==0:
        ans.append(-B/(2*A))
    ans.sort()
    print(*ans)
