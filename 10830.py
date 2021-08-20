#10830
def matmul(A,B,n):
    return [[sum([(A[j][i]*B[i][k]) for i in range(n)])%1000 for k in range(n)] for j in range(n)]
def fast_mul(A,n,l):
    if n==1:return A
    else:
        y=fast_mul(A,n//2,l)
        if n%2==0:
            return matmul(y,y,l)
        else:
            return matmul(matmul(y,y,l),A,l)
n,b=map(int,input().split())
T=[[0 for i in range(n)] for j in range(n)]
for i in range(n):
    T[i]=list(map(int,input().split()))
if b==1:u=T
else:
    u=fast_mul(T,b,n)
for y in u:
    print(*[i%1000 for i in y])
