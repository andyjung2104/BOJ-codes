import math,sys
def numofDivisors(n):
    cnt=0
    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0:
            cnt+=1
    if n==int(math.sqrt(n))**2:
        cnt-=0.5
    return int(2*cnt)
d,m=map(int,input().split())
D=list(map(int,sys.stdin.readline().split()))
M=list(map(int,sys.stdin.readline().split()))
L1=math.lcm(*D)
G1=math.gcd(*M)
if G1%L1!=0:
    print(0)
else:
    print(numofDivisors(G1//L1))
