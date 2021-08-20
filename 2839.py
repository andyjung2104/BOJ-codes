N=int(input())
if N%5==0:
    print(N//5)
elif N%5==1:
    if N>=6:print((N-6)//5+2)
    else:print(-1)
elif N%5==2:
    if N>=12:print((N-12)//5+4)
    else:print(-1)
elif N%5==3:
    if N>=3:print((N-3)//5+1)
    else:print(-1)
elif N%5==4:
    if N>=9:print((N-9)//5+3)
    else:print(-1)
