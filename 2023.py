def isPrime(p):
    isPrime=True
    if p==1:
        return False
    if p>2 and p%2==0:
        return False
    if p>3 and p%3==0:
        return False
    else:
        if p>5:
            for i in range(5,int(p**.5)+1,6):
                if p%i==0:return False
        if p>7:
            for i in range(7,int(p**.5)+1,6):
                if p%i==0:return False
    return True
P=[[]]
P[0]=[2,3,5,7]
n=int(input())
for i in range(1,n):
    nextP=[]
    for p in P[i-1]:
        tryy=[10*p+1,10*p+3,10*p+5,10*p+7,10*p+9]
        for t in tryy:
            if isPrime(t):
                nextP.append(t)
    P.append(nextP)

y=P[n-1]
for i in y:
    print(i)
