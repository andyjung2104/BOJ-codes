#5430
import sys

T=int(input())
for t in range(T):
    p=sys.stdin.readline().rstrip()
    n=int(input())
    x=sys.stdin.readline().strip()
    if n==0:X=[]
    else:X=list(map(int,x[1:-1].split(',')))
    
    rev=False
    printed=False
    for f in p:
        if f=='R':
            rev=not rev
        else:
            if len(X)==0:
                print('error')
                printed=True
                break
            if rev:
                del X[-1]
            else:
                del X[0]
    if not printed:print(X[::-1] if rev else X)
