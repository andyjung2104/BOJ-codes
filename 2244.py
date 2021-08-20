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
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]
n,m=map(int,input().split())
p1=[]
p2=[]
points=[]
for _ in range(n):
    p1.append(tuple(map(int,input().split())))
for _ in range(m):
    p2.append(tuple(map(int,input().split())))
minx=10**9
miny=10**9
for u in p1:
    for v in p2:
        points.append((u[0]+v[0],u[1]+v[1]))
        if minx>u[0]+v[0]:
            minx=u[0]+v[0]
            miny=u[1]+v[1]
        elif minx==u[0]+v[0]:
            if miny>u[1]+v[1]:
                miny=u[1]+v[1]
ch=convex_hull(points)
print(len(ch))
st=(minx,miny)
st=ch.index(st)
for i in range(st,len(ch)):
    print(*ch[i])
for i in range(st):
    print(*ch[i])
