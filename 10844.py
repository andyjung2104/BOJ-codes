#10844
#a[n-1][digit]
n=int(input())
a=[[1]*10 for k in range(n)]
a[0][0]=0
for k in range(1,n):
    a[k][0]=a[k-1][1]
    for digit in range(1,9):
        a[k][digit]=a[k-1][digit-1]+a[k-1][digit+1]
    a[k][9]=a[k-1][8]
print(sum(a[n-1])%(10**9))
