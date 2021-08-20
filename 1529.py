def matmul(A,B):
    return [[sum([(A[j][i]*B[i][k]) for i in range(2)])%1234567891 for k in range(2)] for j in range(2)]
def fast_mul(A,n):
    if n==1:return A
    else:
        y=fast_mul(A,n//2)
        if n%2==0:
            return matmul(y,y)
        else:
            return matmul(matmul(y,y),A)
n,l=map(int,input().split())
a,b,c,d=[0]*4
numbers = list(input().split())
for num in numbers:
    good=True
    for i in num:
        if i not in ['4','7']:
            good=False
            break
    if not good:
        continue
    if num[0]=='4':
        if num[-1]=='7':
            b+=1
        elif num[-1]=='4':
            a+=1
    elif num[0]=='7':
        if num[-1]=='4':
            c+=1
        elif num[-1]=='7':
            d+=1
            
T=((a,b),(c,d))
TT=fast_mul(T,l)
print((sum(TT[0])+sum(TT[1]))%1234567891)
