#2470

import sys

N=int(input())
l=list(map(int,sys.stdin.readline().split()))
l.sort()
st=0
end=N-1
min_pH=l[-1]+l[0]
min1=l[0]
min2=l[-1]
while st<end:
    pH=l[end]+l[st]
    if abs(pH)<abs(min_pH):
        min_pH=pH
        min1=l[st]
        min2=l[end]
    if pH>0:
        end-=1
    elif pH<0:
        st+=1
    else:
        min1=l[st]
        min2=l[end]
        break
print(min1,min2)
