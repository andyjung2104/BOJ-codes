N=int(input())
a,b,c,d,e,f=map(int,input().split())
min1=min(a,b,c,d,e,f)
min2=min(a+b,a+c,a+d,a+e,b+c,c+e,d+e,b+d,f+b,f+c,f+d,f+e)
min3=min(a+b+c,a+c+e,a+d+e,a+b+d,f+b+c,f+c+e,f+d+e,f+b+d)
if N!=1:
    print((N-2)*(N-1)*4*min1+min1*(N-2)**2+4*(N-1)*min2+4*(N-2)*min2+4*min3)
else:
    print(a+b+c+d+e+f-max(a,b,c,d,e,f))
