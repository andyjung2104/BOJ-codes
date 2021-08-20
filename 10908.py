#10908
mod=10**9+7
def matmul(A,B):
    return [[sum([(A[j][i]*B[i][k]) for i in range(2)])%mod for k in range(2)] for j in range(2)]
def fast_mul(A,n):
    if n==1:return A
    else:
        y=fast_mul(A,n//2)
        if n%2==0:
            return matmul(y,y)
        else:
            return matmul(matmul(y,y),A)
n,k=map(int,input().split())
T=((1,1),(1,0))
if k==1:
    A,B=1,0
else:
    u=fast_mul(T,k-1)
    #print(u)
    A,B=u[0][0],u[1][0]
#print(A,B)
X=((A+2*B,1),(A*(A-B)-B**2,0))
if n==1:
    C,D=1,0
elif n==0:
    C,D=0,1
else:
    v=fast_mul(X,n-1)
    #print(v)
    C,D=v[0][0],v[1][0]
print(C%mod,D%mod)
