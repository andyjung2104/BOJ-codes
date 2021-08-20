#회전판 N개, 각 회전판에 숫자 0~(M-1)

def countLumps(T):
    T.sort()
    for i in range(len(T)):
        T[i]-=i
    return len(set(T))

def locateMin(S):
    minn=min(S)
    t=[]
    for i in range(len(S)):
        if S[i]==minn:
            t.append(i)
    return t
def solveLock(N,M,S):
    P=S[:]
    TIMES=0
    for i in P:
        S=P[:]
        count=0
        for j in range(len(S)):
            S[j]-=i
            if S[j]<0:S[j]+=M
        while min(S)!=max(S):
            x1=locateMin(S)
            
            for h in x1:
                S[h]=S[h]+1
            count+=countLumps(x1)
            #print(count)
        if i==P[0]:TIMES=count
        else:TIMES=min(TIMES,count)
        #print('----------------')
    return TIMES
N,M=map(int,input().split())
ss=input()
S=[int(i) for i in ss.split()]
print(solveLock(N,M,S))
