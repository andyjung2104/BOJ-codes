N=int(input())
K=list(map(int,input().split()))
for i in range(len(K)):
    if i==0:K[0]=K[0]
    else:
        K[i]+=K[i-1]
a=0
minmin=0
maxes=[]
while a<N:
    maxes.append(K[a]-minmin)
    minmin=min(K[a],minmin)
    a+=1
print(max(maxes))
