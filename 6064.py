T=int(input())
for _ in range(T):
    printed=False
    m,n,x,y=map(int,input().split())
    #<a,b>
    a,b=1,1
    time=0
    while time<m*n:
        if (a+time-1)%m+1==x:
            if (b+time-1)%n+1==y:
                print(time+1)
                printed=True
                break
        time+=1
    if not printed:print(-1)
