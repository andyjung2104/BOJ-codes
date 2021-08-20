import math
T=int(input())
for t in range(T):
    a,b=map(int,input().split())
    print(math.factorial(b)//(math.factorial(a)*math.factorial(b-a)))
