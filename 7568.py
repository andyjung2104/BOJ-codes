#7568
n=int(input())
def isbig(p1,p2):
    #1:p1>p2, 0:nothing, -1:p1<p2
    if p1[0]>p2[0] and p1[1]>p2[1]:
        return 1
    if p1[0]<p2[0] and p1[1]<p2[1]:return -1
    return 0
l=[]
for i in range(n):
    x,y=map(int,input().split())
    l.append((x,y))
for p in l:
    cnt=1
    for pp in l:
        if isbig(p,pp)==-1:
            cnt+=1
    print(cnt,end=' ')
    
