#2096
import sys
n=int(input())
amin,bmin,cmin=0,0,0
amax,bmax,cmax=0,0,0
for i in range(n):
    a,b,c=map(int,sys.stdin.readline().split())
    amin,bmin,cmin=a+min(amin,bmin),b+min(amin,bmin,cmin),c+min(bmin,cmin)
    amax,bmax,cmax=a+max(amax,bmax),b+max(amax,bmax,cmax),c+max(bmax,cmax)
print(max(amax,bmax,cmax),min(amin,bmin,cmin))
