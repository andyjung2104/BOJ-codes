#2916
import math
n,k=map(int,input().split())
l=math.gcd(*([360]+list(map(int,input().split()))))
y=list(map(int,input().split()))
for i in y:
    if i%l==0:
        print('YES')
    else:print('NO')
