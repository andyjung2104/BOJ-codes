from itertools import combinations
import sys
while True:
    a=list(map(int,sys.stdin.readline().split()))
    if a[0]==0:break
    n=a.pop(0)
    y=combinations(a,6)
    for i in y:print(*i)
    print()
