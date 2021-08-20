#2156
import sys
n=int(input())
x=[]
a=[0]*n
for i in range(n):
    tmp=int(sys.stdin.readline())
    x.append(tmp)
a[0]=x[0]
a[1]=x[0]+x[1]
M=[a[0],a[1]]
#a[n]=x[n]+max(a[n-2],a[n-3]+x[n-1])
for i in range(2,n):
    if i>2:a[i]=x[i]+max(M[-3],a[i-2],a[i-3]+x[i-1])
    else:a[i]=x[i]+max(a[i-2],a[i-3]+x[i-1])
    M.append(max(M[-1],a[i]))
print(max(a))
