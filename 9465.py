#9465
#a_1, a_2, a_3, ...
#b_1, b_2, b_3, ...
import sys
t=int(input())
for _ in range(t):
    n=int(sys.stdin.readline())
    a=list(map(int,sys.stdin.readline().split()))
    b=list(map(int,sys.stdin.readline().split()))
    if n==1:
        print(max(a[0],b[0]))
    else:
        A=[a[0],b[0]+a[1]]
        B=[b[0],b[1]+a[0]]
        m=max(A+B)
        for i in range(2,n):
            pa=max(B[i-1],B[i-2])+a[i]
            pb=max(A[i-1],A[i-2])+b[i]
            m=max(m,pa,pb)
            A.append(pa)
            B.append(pb)
        print(m)
