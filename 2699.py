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
p=int(input())
for _ in range(p):
    points = []
    n=int(input())
    for __ in range((n+4)//5):
        l=list(map(int,input().split()))
        while len(l)>2:
            points.append(tuple(l[:2]))
            l=l[2:]
        points.append(tuple(l))
    minx=21
    maxy=-21
    st=(0,0)
    ch=convex_hull(points)
    for p in ch:
        if maxy<p[1]:
            st=p
            minx,maxy=p
        elif maxy==p[1]:
            if minx>p[0]:
                st=p
    ch=ch[::-1]
    print(len(ch))
    ind=ch.index(st)
    for i in range(ind,len(ch)):
        print(*ch[i])
    for i in range(ind):
        print(*ch[i])
    
