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
n=int(input())
points = []
for _ in range(n):
    points.append(tuple(map(int,input().split())))
ch=convex_hull(points)
S=0
for i in range(-1,len(ch)-1):
    S+=ch[i][0]*ch[i+1][1]-ch[i+1][0]*ch[i][1]
S=abs(S)/2
print(int(S/50))
