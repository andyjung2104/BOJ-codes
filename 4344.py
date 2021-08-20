import sys
C=int(input())
for i in range(C):
    A=list(map(int,sys.stdin.readline().split()))
    num=A.pop(0)
    mean=sum(A)/num
    count=0
    for a in A:
        if a>mean:count+=1
    print('%.3f%%' % (100*count/num))
