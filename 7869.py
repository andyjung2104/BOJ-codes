#7869
#c1=(x1,y1,r)
import math
def S(a,b,c):
    x=[a,b,c]
    s=(a+b+c)/2
    ans=s
    for i in x:
        ans*=(s-i)
    return ans**.5

def isok(a,b,c):
    r=max(a,b,c)
    if 2*r**2>a*a+b*b+c*c:
        return 2
    elif 2*r**2<a*a+b*b+c*c:
        return 0
    else:return 1
    
def f(c1,c2):
    x1,y1,r1=c1
    x2,y2,r2=c2
    l=((x1-x2)**2+(y1-y2)**2)**.5
    if l<abs(r1-r2):
        return 0
    elif l==abs(r1-r2):
        return 1
    elif abs(r1-r2)<l<r1+r2:
        return 2
    elif l==r1+r2:
        return 3
    else:return 4
inp=list(map(float,input().split()))
c1=inp[:3]
c2=inp[3:]
e=f(c1,c2)
if e<=1:
    r=min(c1[2],c2[2])
    print('%.3f' % (math.pi*r*r))
elif e>=3:
    print('0.000')
else:
    x1,y1,r1=c1
    x2,y2,r2=c2
    l=((x1-x2)**2+(y1-y2)**2)**.5
    ang_1=math.acos((l*l-r2*r2+r1*r1)/(2*r1*l))
    ang_2=math.acos((l*l+r2*r2-r1*r1)/(2*l*r2))
    S1=r1*r1*ang_1
    S2=r2*r2*ang_2
    print('%.3f' % (S1+S2-S(l,r1,r2)*2))
    
