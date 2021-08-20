w,p=map(int,input().split())
P=[0]+list(map(int,input().split()))+[w]
s=set()
for i in range(1,p+2):
    s=s.union(set(P[i]-P[j] for j in range(i)))

ss=list(s)
ss.sort()
print(*ss)
