N,r,c=map(int,input().split())
def num(N,r,c):
    count=0
    if N==0:return 0
    if r>=2**(N-1):
        count+=2**(2*N-1)
        r-=2**(N-1)
    if c>=2**(N-1):
        count+=2**(2*N-2)
        c-=2**(N-1)
    return count+num(N-1,r,c)
print(num(N,r,c))
