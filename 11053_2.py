N=int(input())
A=list(map(int,input().split()))
lislen=[1]
for i in range(1,len(A)):
    lens=set()
    a=A[i]
    for j in range(i):
        if A[j]<a:lens.add(lislen[j])
    if len(lens)>0:lislen.append(1+max(lens))
    else:lislen.append(1)
print(max(lislen))
