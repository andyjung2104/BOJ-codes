def a(n):
    if n==1:return 0
    A=[]
    if n%3==0:
        A.append(1+a(n//3))
    if n%2==0:
        A.append(1+a(n//2))
    A.append(1+a(n-1))
    return min(A)
n=int(input())
print(a(n))
