#1806
import sys

N,S=map(int,input().split())
li=list(map(int,sys.stdin.readline().split()))
start=0
end=0
tmp=0
minlen=N+1
while end<=N:
    if tmp<S:
        if end>=N:break
        end+=1
        tmp+=li[end-1]
    else:
        minlen=min(minlen,end-start)
        tmp-=li[start]
        start+=1
if minlen==1+N:print(0)
else:print(minlen)
