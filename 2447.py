#2447

import math
N=int(input())
k=int(.5+math.log(N,3))
def f(k):
    if k==1:
        return ['***','* *','***']
    else:
        y=f(k-1)
        a=[y[i]*3 for i in range(3**(k-1))]
        b=[y[i]+' '*3**(k-1)+y[i] for i in range(3**(k-1))]
        return a+b+a
t=f(k)
for u in t:
    print(u+' ')
