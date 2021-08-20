
a=[]
while True:
    a=a+list(map(int,input().split()))
    if a[-1]==0:break
def sums(n):
    ans=0
    for i in range(1,n):
        if n%i==0:
            ans+=i
    return ans
for i in a:
    if i==0:break
    t=sums(i)
    if t>i:
        print('%d ABUNDANT' % i)
    elif t==i:
        print('%d PERFECT' % i)
    else:
        print('%d DEFICIENT' % i)
