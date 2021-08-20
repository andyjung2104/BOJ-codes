#1043
#무조건 참을 듣는 사람들
n,m=map(int,input().split())
t=list(map(int,input().split()))
num_true=t.pop(0)
t=set(t)
partys=[]
for i in range(m):
    pty=list(map(int,input().split()))
    if pty[0]!=0:
        partys.append(set(pty[1:]))
ori=0
while True:
    ori=len(t)
    for party in partys:
        if len(set(party)&t)>0:
            t|=party
    if len(t)-ori==0:
        break
ans=0
for party in partys:
    ok=True
    for person in party:
        if person in t:
            ok=False
            break
    if ok:ans+=1
print(ans)
