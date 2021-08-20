#1931
import sys
n=int(input())
L=[]
for _ in range(n):
    i,j=map(int,sys.stdin.readline().split())
    L.append((j,i))
L.sort()
for l in range(n):
    L[l]=L[l][::-1]
end=0
ans=0
for i in range(n):
    if L[i][0]>=end:
        ans+=1
        end=L[i][1]
print(ans)
