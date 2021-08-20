
import sys
l=[]
N=int(input())
for n in range(N):
    x=int(sys.stdin.readline().strip())
    if x==0:
        if len(l)!=0:print(l.pop())
        else:print(0)
    else:
        if len(l)==0:l=[x]
        else:
            if x<l[0]:
                l=[x]+l
            elif x>=l[-1]:
                l.append(x)
            else:
                for i in range(len(l)-1):
                    if l[i]<=x<l[i+1]:
                        l=l[:(i+1)]+[x]+l[(i+1):]
                        break
                
