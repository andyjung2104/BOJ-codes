import sys

w=[[[1 for i in range(21)] for j in range(21)] for k in range(21)]
for a in range(1,20+1):
    for b in range(1,20+1):
        for c in range(1,20+1):
            if a<b<c:
                w[a][b][c]=w[a][b][c-1]+w[a][b-1][c-1]-w[a][b-1][c]
            else:
                w[a][b][c]=w[a-1][b][c]+w[a-1][b-1][c]+w[a-1][b][c-1]-w[a-1][b-1][c-1]
#w(a,b,c)=w[a][b][c]
while True:
    a,b,c=map(int,sys.stdin.readline().split())
    if a==b==c==-1:
        break
    print('w(%d, %d, %d) = ' % (a,b,c),end='')
    
    if a<=0 or b<=0 or c<=0:
        print(1)
    else:
        if a>20 or b>20 or c>20:
            print(w[20][20][20])
        else:
            print(w[a][b][c])
