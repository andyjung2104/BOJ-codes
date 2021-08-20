import sys
while True:
    N=int(sys.stdin.readline().strip())
    if N==0:break
    k=int((2*N)**.5)
    NN=N
    while True:
        if NN%2!=0:break
        NN//=2
    
    cnt=0
    for i in range(1,int(NN**.5)+2,2):
        if NN%i==0:
            cnt+=2
    if NN==int(NN**.5)**2:
        cnt-=1
    if 2*N==k*(k+1):cnt-=1
    print(cnt)
