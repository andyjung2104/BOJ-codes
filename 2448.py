import math
n=int(input())
k=int(.5+math.log(n/3,2))
def f(n):
    if n==0:
        return ['  *  ',' * * ','*****']
    else:
        y=f(n-1)
        return [' '*(3*(2**(n-1)))+y[i]+' '*(3*(2**(n-1))) for i in range(3*2**(n-1))]+[y[i]+' '+y[i] for i in range(3*2**(n-1))]
r=f(k)
for e in r:
    print(e)
