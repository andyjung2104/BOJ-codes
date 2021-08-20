count=0
N=int(input())
def isHan(n):
    if n<100:return True
    S=str(n)
    d=int(S[1])-int(S[0])
    for i in range(2,len(S)):
        if int(S[i])-int(S[i-1])==d:continue
        return False
    return True
for i in range(1,N+1):
    if isHan(i):count+=1
print(count)
