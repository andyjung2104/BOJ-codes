l=[0,0]
N=int(input())
for i in range(2,N+1):
    s={l[i-1]}
    if i%3==0:
        s.add(l[i//3])
    if i%2==0:
        s.add(l[i//2])
    l.append(1+min(s))
print(l[N])
