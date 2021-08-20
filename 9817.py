import sys,math
c=3
while True:
    s=int(sys.stdin.readline().strip())
    if s==-1:break
    ans=0
    ans+=c**s
    num=1
    #i칸 돌리기
    for i in range(1,s):
        ans+=c**math.gcd(s,i)
        num+=1
    #뒤집기
    if s%2==0:
        ans+=(s//2)*(c**2+c)*(c**(s//2-1))
        num+=s
    else:
        ans+=s*c**(1+s//2)
        num+=s
    print(ans//num)
