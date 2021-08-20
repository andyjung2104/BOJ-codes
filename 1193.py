x=int(input())
#합 n
n=int(((1+8*(x-1))**.5+1)/2)+1
#print(n)
if n%2==0:
    #u/d
    d=x-(n*n-3*n+2)//2
    u=n-d
else:
    u=x-(n*n-3*n+2)//2
    d=n-u
print("%d/%d" % (u,d))
