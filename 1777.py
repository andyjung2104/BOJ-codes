#1777
import sys
n=int(input())
INV=list(map(int,sys.stdin.readline().split()))
revseq=''
for i in range(1,1+n):
    revseq=revseq[:INV[i-1]]+str(i)+revseq[INV[i-1]:]
for s in revseq[::-1]:
    print(s,end=' ')
