import sys,math
n=int(input())
def length(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)
for i in range(n):
    x1,y1,r1,x2,y2,r2=map(int,sys.stdin.readline().split())
    l=length(x1,y1,x2,y2)
    if l<abs(r1-r2):
        print(0)
        continue
    elif l==abs(r1-r2):
        if l==0:print(-1)
        else:print(1)
        continue
    elif abs(r1-r2)<l<(r1+r2):
        print(2)
        continue
    elif l==r1+r2:
        print(1)
        continue
    else:print(0)
