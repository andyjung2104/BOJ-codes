n=int(input())
s=map(int,input().split())
s=list(s)
s.sort()

if n>=2:
    print(int(s[0])*int(s[-1]))
else:
    print(int(s[0])**2)
