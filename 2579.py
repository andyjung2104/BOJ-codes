N=int(input())
X=[0]
for n in range(N):
    X.append(int(input()))
if N==0:print(0)
elif N>=2:
    A=[0,X[1],X[1]+X[2]]
    B=[0,0,X[2]]
    for i in range(3,N+1):
        A.append(X[i]+B[i-1])
        B.append(X[i]+max(A[i-2],B[i-2]))
    print(max(A[N],B[N]))
else:print(X[1])
    
