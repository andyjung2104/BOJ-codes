import sys
input=sys.stdin.readline


def convex_hull(points):
    points = sorted(set(points))
    if len(points) <= 1:return points
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def dis(a,b,c,x,y):
    return abs(a*x+b*y+c)/((a**2+b**2)**.5)


c = int(input())
points = []
for i in range(c):
    x, y=map(int,input().split())
    points.append((x, y))
ch = convex_hull(points)
n = len(ch)
ans = 0
#ch[0],ch[1]의 최대거리 찾기:ch[st]
if n==2:
    ans=(ch[0][0]-ch[1][0])**2+(ch[1][1]-ch[0][1])**2
    print(ans**.5)
    sys.exit()
st=2; maxlen=0
for i in range(2,n):
    x,y=ch[i]
    if maxlen<abs((ch[0][1]-ch[1][1])*x+(ch[0][0]-ch[1][0])*y+ch[0][0]*ch[1][1]-ch[0][1]*ch[1][0]):
        st=i
        maxlen=abs((ch[0][1]-ch[1][1])*x+(ch[0][0]-ch[1][0])*y+ch[0][0]*ch[1][1]-ch[0][1]*ch[1][0])
j=st
for i in range(n-1):
    x1,y1=ch[i]
    x2,y2=ch[i+1]
    while dis(y1-y2,x1-x2,x1*y2-x2*y1,ch[j][0],ch[j][1])<=dis(y1-y2,x1-x2,x1*y2-x2*y1,ch[(j+1)%n][0],ch[(j+1)%n][1]):
        j+=1; j%=n
    ans=max(ans,dis(y1-y2,x1-x2,x1*y2-x2*y1,ch[j][0],ch[j][1]))
print(ans)
