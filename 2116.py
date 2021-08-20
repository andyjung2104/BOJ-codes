import sys
N=int(input())#number of dice
dices=[]
for i in range(N):
    a,b,c,d,e,f=map(int,sys.stdin.readline().split())
    l=[a,b,c,e,d,f]
    dices.append(l)
maxx=[]
count=0
for j in range(6):
    maxsum=max(set(dices[0])-{dices[0][j]}.union({dices[0][5-j]}))
    for count in range(1,N):
        j=dices[count].index(dices[count-1][5-j])
        maxsum+=max(set(dices[count])-{dices[count][j]}.union({dices[count][5-j]}))
    maxx.append(maxsum)
print(max(maxx))
