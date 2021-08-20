#2108
import sys

def r(x):
    if x==int(x):return int(x)
    if x>=0:
        b=x-int(x)
        if b<0.5:
            return int(x)
        else:return int(x)+1
    else:
        b=1-int(x)+x
        if b<0.5:
            return int(x)-1
        else:
            return int(x)
        
    

n=int(input())
x=[]
y=[0]*8001
summ=0
#i의 개수=y[i+4000]
for i in range(n):
    tmp=int(sys.stdin.readline())
    x.append(tmp)
    y[tmp+4000]+=1
    summ+=tmp
x.sort()
cnt=0
M=0
ans=0
for i in range(8001):
    if y[i]>M:
        cnt=0
        M=y[i]
        ans=i
    elif y[i]==M:
        cnt+=1
        if cnt==1:
            ans=i
    
print(r(summ/n))
print(x[n//2])
print(ans-4000)
print(x[-1]-x[0])
