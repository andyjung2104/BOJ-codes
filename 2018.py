N=int(input())
while True:
    if N%2!=0:break
    N//=2
cnt=0
for i in range(1,int(N**0.5)+2,2):
    if N%i==0:
        cnt+=2
if N==int(N**.5)**2:cnt-=1
print(cnt)
