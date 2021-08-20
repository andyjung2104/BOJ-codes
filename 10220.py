#10220
def f(n):
    
    if n in {1,2,3,6}:
        return 0
    elif n==4:return 2
    elif n==5:return 1
    
    return 1
t=int(input())

for i in range(t):
    print(f(int(input())))
