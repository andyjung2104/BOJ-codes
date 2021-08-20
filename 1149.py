#1149
import sys
n=int(input())
a,b,c=0,0,0
for i in range(n):
    x,y,z=map(int,sys.stdin.readline().split())
    a,b,c=x+min(c,b),min(a,c)+y,z+min(a,b)
print(min(a,b,c))
