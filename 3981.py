import sys
T=int(input())
for t in range(T):
    
    X=list(map(int,sys.stdin.readline().split()))
    n=X[0]
    if n<=4:print('YES')
    else:
        a=X[4]-3*X[3]+3*X[2]-X[1]
        b=3*X[1]-8*X[2]+7*X[3]-2*X[4]
        c=6*X[2]-6*X[1]-7*a-9*b
        d=6*X[1]-a-3*b-c
        ok=True
        for i in range(5,n+1):
            if a*i**3+3*b*i**2+c*i+d != 6*X[i]:
                ok=False
                break
        if ok:
            print('YES')
        else:print('NO')
