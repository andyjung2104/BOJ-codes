P=[1,1,1]
t=int(input())
for i in range(3,101):
    P.append(P[i-2]+P[i-3])
for _ in range(t):
    print(P[int(input())-1])
