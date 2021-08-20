import sys,math
input=sys.stdin.readline

def leng(p1,p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**.5

def convex_hull(points):
    points = sorted(set(points))
    if len(points) <= 1:return points
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]
n=int(input())
num=0
points = []
minx=10**9
miny=10**9
st=(0,0)
for i in range(n):
    x,y,c=input().split()
    if c=='Y':
        num+=1
        x=int(x); y=int(y)
        points.append((x,y))
        if minx>x:
            minx=x
            miny=y
            st=(x,y)
        elif minx==x:
            if miny>y:
                miny=y
                st=(x,y)

ch=convex_hull(points)
print(len(ch))
if num==1:
    print(*ch[0])
    sys.exit()
ind=ch.index(st)
for i in range(ind,len(ch)):
    print(*ch[i])
for i in range(ind):
    print(*ch[i])
