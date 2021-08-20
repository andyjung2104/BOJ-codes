import sys
N,M=map(int,input().split())
d=set()
b=set()
for n in range(N):
    d.add(sys.stdin.readline().strip())
for m in range(M):
    b.add(sys.stdin.readline().strip())
names=sorted(list(b&d))
print(len(names))
for name in names:
    print(name)
