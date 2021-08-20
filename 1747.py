def prime_list(n):
    sieve=[True]*n
    m=int(n**.5)
    for j in range(4,n,2):
        sieve[j]=False
    for i in range(3,m+1,2):
        if sieve[i]:
            for j in range(2*i,n,i):
                sieve[j]=False
    sieve[0]=False
    sieve[1]=False
    return sieve
def isPrime(p):
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
def isPalindrome(i):
    s=str(i)
    return s==s[::-1]
def makePalindrome(length):
    l=[]
    if length%2==0:
        for i in range(10**(length//2-1),10**(length//2)):
            s=str(i)
            l.append(s+s[::-1])
        return l
    else:
        for i in range(10**(length//2-1),10**(length//2)):
            s=str(i)
            for j in range(0,10):
                l.append(s+str(j)+s[::-1])
        return l
t=[2,3,5,7]
for j in range(2,8):
    t=t+makePalindrome(j)
n=int(input())
for u in t:
    u=int(u)
    if u<n:
        continue
    if isPrime(u):
        print(u)
        break
