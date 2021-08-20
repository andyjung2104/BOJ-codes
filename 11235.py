n=int(input())
l=[]
for _ in range(n):
    l.append(input())
s=set(l)
maxx=0
m=[]
for name in s:
    if l.count(name)>maxx:
        m=[name]
        maxx=l.count(name)
    elif l.count(name)==maxx:
        m.append(name)
for i in m:
    print(i)
