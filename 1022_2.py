r1,c1,r2,c2=map(int,input().split())
#r1,c1<=0 r2,c2>=0
m=max(abs(r1),abs(c1),abs(r2),abs(c2))
#1~(2m+1)^2
L=[[-1 for i in range(2*m+3)] for j in range(2*m+3)]
for x in range(1,2*m+2):
    for y in range(1,2*m+2):
        L[x][y]=0
x,y=2*m+1,2*m+1
dx=[0,-1,0,1]
dy=[-1,0,1,0]

#direction
drc=0

#length
maxlen=0

for num in range((2*m+1)**2,0,-1):
    if r1<=(x-m-1)<=r2 and c1<=(y-m-1)<=c2:
        L[x][y]=num
        maxlen=max(maxlen,len(str(num)))
    else:L[x][y]=1
    #turncnt=0
    if L[x+dx[drc]][y+dy[drc]]!=0:
        drc=(drc+1)%4
    x+=dx[drc]
    y+=dy[drc]



for x in range(1+r1+m,r2+m+2):
    for y in range(c1+m+1,c2+m+2):
        print(str(L[x][y]).rjust(maxlen),end=' ')
    print()
