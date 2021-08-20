import sys
N=int(input())
maxweights=list(map(int,sys.stdin.readline().split()))
maxweights.sort(reverse=True)
M=int(input())
boxes=list(map(int,sys.stdin.readline().split()))
boxes.sort(reverse=True)
if maxweights[0]<boxes[0]:
    print(-1)
else:
    time=0
    temp=0
    for b in boxes:
        time+=1
        if temp>=N:
            temp=0
        if b<=maxweights[temp]:
            temp+=1
            time-=1
        else:
            temp=0
            
    print(time)
