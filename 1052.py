def suminbinary(n):
    return bin(n).count('1')
n,k=map(int,input().split())
cnt=0
while suminbinary(n)>k:
    n+=1
    cnt+=1
print(cnt)
