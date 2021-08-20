import sys
N=int(input())
maxweights=list(map(int,sys.stdin.readline().split()))
maxweights.sort()
M=int(input())
boxweights=list(map(int,sys.stdin.readline().split()))
boxweights.sort()
def nextlist(maxweights,boxweights):#these are sorted
    for b in maxweights:
        if len(boxweights)==0:
            break
        cc=max(boxweights)
        for c in range(len(boxweights)):
            if boxweights[c]>b:
                cc=boxweights[c-1]
                break
        boxweights.remove(cc)
    return maxweights,boxweights
def nextlist2(maxweights,boxweights):
    maxweightss=maxweights[::-1]
    for b in boxweights[::-1]:
        if len(maxweightss)==0:break
        if maxweightss[0]>b:
            del maxweightss[0]
            boxweights.remove(b)
        else:break
    return maxweights,boxweights
if max(maxweights)<max(boxweights):
    print(-1)
else:
    t=0
    while len(boxweights)!=0:
        maxweights,boxweights=nextlist2(maxweights,boxweights)
        t+=1
    print(t)

    
