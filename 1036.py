#O=[0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
OO='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def num_to_k(n):
    S=''
    if n==0:return 0
    while n>0:
        S=OO[n%36]+S
        n//=36
    return S
N=int(input())
nums=[]
for n in range(N):
    nums.append(input().strip())
k=int(input())
osum=0
#nums에는 문자열 존재
#각 문자를 Z로 바꾸었을 때 증가량을 inc에 저장
inc=[0 for i in range(36)]
for num in nums:
    osum+=int(num,36)
    u=num[::-1]
    for i in range(len(u)):
        y=u[i]
        inc[int(y,36)]+=(35-int(y,36))*(36**i)
inc.sort(reverse=True)
print(num_to_k(osum+sum(inc[:k])))
