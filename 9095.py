X=[1,1,2]
T=int(input())
n=11
if n<=2:
    print(X[n])
else:
    for i in range(3,n+1):
        X.append(X[i-1]+X[i-2]+X[i-3])
for i in range(T):
    print(X[int(input())])
