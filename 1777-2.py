import sys
N=int(input())
L=list(map(int,sys.stdin.readline().split()))
revANS=[0 for i in range(N)]
for k in range(N,0,-1):
    count=0
    for a in range(len(revANS)):
        if count==L[k-1] and (not revANS[a]):
            break
        if (not revANS[a]):
            count+=1
    revANS[a]=k
for i in revANS[::-1]:
    print(i,end=' ')

