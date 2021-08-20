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
n,r=map(int,input().split())
points = []
for i in range(n):
    x,y=map(int,input().split())
    points.append((x,y))
ans=0
ch=convex_hull(points)
for j in range(len(ch)):
    ans+=leng(ch[j-1],ch[j])
ans+=2*math.pi*r
print(int(0.5+ans))
