import math,sys
T=int(input())
def num(X):
    t=math.ceil(math.sqrt(X))
    if X<=t*(t-1):
        return(2*(t-1))
    else:return(2*t-1)
for i in range(T):
    a,b=map(int,sys.stdin.readline().split())
    X=b-a
    print(num(X))
