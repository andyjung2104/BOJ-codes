import sys
for __ in range(int(input())):
    a,b,c,d=map(int,sys.stdin.readline().split())
    i=-1
    for x in range(0,2*10**6+1):
        if a*x**3+b*x**2+c*x+d==0:
            i=x
            break
    if i==-1:
        for x in range(1,2*10**6+1):
            if a*x**3-b*x**2+c*x-d==0:
                i=-x
                break
    #ax^3+bx^2+cx+d=(x-integer)(ax^2+(b+a*integer)x+
    #(c+integer*(b+a*integer)))
    if a*i**2+(b+a*i)*i+(c+i*(b+a*i))==0:
        print(*sorted(list(set([i,-i-(b+a*i)/a]))))
    else:
        D=(b+a*i)**2-4*a*(c+i*(b+a*i))
        if D==0:
            print(*sorted([i,-(b+a*i)/(2*a)]))
        elif D<0:
            print(i)
        else:
            A,B,C=a,b+a*i,c+i*(b+a*i)
            x1=(-B+(B**2-4*A*C)**.5)/(2*A)
            x2=(-B-(B**2-4*A*C)**.5)/(2*A)
            print(*sorted([x1,x2,i]))
