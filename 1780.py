import math
n=int(input())
k=int(math.log(n,3))
L=[]
num=[0,0,0]
def f(k,L):
    if k==0:
        num[L[0][0]+1]+=1
        return 1
    if len(L)==L.count(L[0]):
        if len(set(L[0]))==1:
            num[L[0][0]+1]+=1
            return 1
    #print(L)
    L1=L[0:3**(k-1)]
    L2=L[3**(k-1):2*3**(k-1)]
    L3=L[2*3**(k-1):3**k]
    u1=[u[0:3**(k-1)] for u in L1]
    u2=[u[3**(k-1):2*3**(k-1)] for u in L1]
    u3=[u[2*3**(k-1):] for u in L1]
    
    u4=[u[0:3**(k-1)] for u in L2]
    u5=[u[3**(k-1):2*3**(k-1)] for u in L2]
    u6=[u[2*3**(k-1):] for u in L2]
    
    u7=[u[0:3**(k-1)] for u in L3]
    u8=[u[3**(k-1):2*3**(k-1)] for u in L3]
    u9=[u[2*3**(k-1):] for u in L3]
    return (f(k-1,u1)+f(k-1,u2)+f(k-1,u3)+f(k-1,u4)+f(k-1,u5)+f(k-1,u6)+f(k-1,u7)+f(k-1,u8)+f(k-1,u9))
for i in range(n):
    l=list(map(int,input().split()))
    L.append(l)
a=f(k,L)
for uu in num:
    print(uu)
