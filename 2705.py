a=[1,1,2]
for i in range(3,1001):
    a.append(sum(a[k] for k in range(i//2+1)))
t=int(input())
for _ in range(t):
    print(a[int(input())])
