import sys
def mlr_rbn(n,primeset={2,7,61}):#n<2**32
    #n<2**(40.96):{2,3,5,7,11}
    #n<2**(41.66):{2,3,5,7,11,13}
    #n<2**(48.27):{2,3,5,7,11,13,17}
    #n<2**64:{2,3,5,7,11,13,17,19,23,29,31,37}
    if n in primeset:
        return True
    
    if n==1 or n%2==0:
        return False


    #maybeprime=False
    #n-1=d*2^s
    N=n-1
    S=0
    while N%2==0:
        N//=2
        S+=1
    d=N
    ok=False
    for a in primeset:
        ok=False
        N=n-1
        maybeprime=False
        num=pow(a,d,n)
        if num==1:ok=True
        if num==n-1:
            maybeprime=True
        else:
            for s in range(S-1):
                num=(num*num)%n
                if num==n-1:
                    maybeprime=True
                    break
        if not maybeprime:
            if ok:
                maybeprime=True
            else:return False
                
        
    return maybeprime
ans=0
for i in range(int(input())):
    k=int(sys.stdin.readline())
    if mlr_rbn(2*k+1):ans+=1
print(ans)
