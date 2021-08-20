n=int(input())
L=[[0]*(2+i) for i in range(1,n+1)]
for i in range(1,1+n):
    l=list(map(int,input().split()))# 길이 i
    if i==1:
        L[i-1]=[0]+l+[0]
    else:
        L[i-1]=[0]+[l[j]+max(L[i-2][j],L[i-2][j+1]) for j in range(i)]+[0]
print(max(L[-1]))
