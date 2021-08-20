def issq(n):
    if int(n**.5)**2==n:
        return True
    return False
n=int(input())
if issq(n):
    print(1)
else:
    a=[0,1]
    for i in range(2,n+1):
        tmp=1
        add=i
        while tmp**2<=i:
            #print(tmp)
            if add>1+a[i-tmp**2]:
                add=1+a[i-tmp**2]
            tmp+=1
        a.append(add)
    print(a)
