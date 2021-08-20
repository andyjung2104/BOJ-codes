N=int(input())
X=list(map(int,input().split()))

Y=[]
par=[]
for i in range(N):
    Y.append(1)
    par.append(-1)
    for k in range(i):
        if X[k]<X[i] and Y[k]+1>Y[-1]:
            Y[-1] = Y[k]+1
            par[-1] = k
cur = 0
val = 1
for i in range(1, N):
    if val<Y[i]:
        cur = i
        val = Y[i]
ans = []
while cur != -1:
    ans.append(X[cur])
    cur = par[cur]
ans = ans[::-1]
print(val)
for i in ans:
    print(i, end=' ')
