L=int(input())
S=list(map(int,input().split()))
n=int(input())
if n in S:
    print(0)
else:
    #n 이전, 이후 원소 찾기
    a,b=0,0
    S.sort()
    if n<S[0]:
        print(n-1+S[0]-n-1+(n-1)*(S[0]-n-1))
    else:
        for i in range(L-1):
            if S[i]<n<S[i+1]:
                a,b=S[i],S[i+1]
                break
        print((n-a-1)*(b-n-1)+b-a-2)
