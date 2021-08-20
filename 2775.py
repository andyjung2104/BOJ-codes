import math
t=int(input())
for _ in range(t):
    k=int(input())
    n=int(input())
    print(math.factorial(n+k)//(math.factorial(k+1)*math.factorial(n-1)))
