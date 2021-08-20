N=int(input())
for n in range(N):
    a,b,c,d=map(int,input().split())
    DD=(b*c)**2-4*b**3*d-4*c**3*a+18*a*b*c*d-27*(a*d)**2
    ans=0
    if DD>0:
        ans=3
    elif DD==0:
        ans=2
    else:
        ans=1
    B=b/(3*a)
    C=c/a
    D=d/a
    P=(C-3*B**2)/3
    Q=(D-B*C+2*B**3)/2
    w=[1,complex(-1/2,(3**.5)/2),complex(-1/2,-(3**.5)/2)]
    x=[]
    for k in range(3):
        x.append(-B+w[k]*(Q+(Q**2+P**3)**.5)**(1/3)+w[(3-k)%3]*(Q-(Q**2+P**3)**.5)**(1/3))
    if ans==3:
        print(*[t.real for t in x])
    elif ans==2:
        print(x[0].real)
    else:
        for y in x:
            if y.imag<10**-4:
                print(y.real)
                break
