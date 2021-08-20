#자물쇠 열기
#M개의 번호 있는 N개의 회전판 존재(M은 2에서 10000, N은 1에서 500)
#S는 초기상태들의 집합
def moveModulo(m,k,S):# mod m으로 k만큼 늘린다 
    for i in range(len(S)):
        S[i]=(S[i]+k)%m
    return S
def find(S,minn):#S안의 minn의 위치를 모두 찾음
    t=[]
    for i in range(len(S)):
        if S[i]==minn:
            t.append(i)
    return t
def countLumps(S):#정수리스트 S에서 붙어있는덩어리 개수(예를들어 [1,2,4,5,6,8]에서는 3개)
    S.sort()
    for i in range(len(S)):
        S[i]-=i
    return len(set(S))
def plusMin(m,S):
    count=0
    miin=find(S,min(S))
    count+=countLumps(miin)
    for i in miin:
        S[i]=(S[i]+1)%m
    return S,count
def solveLock(m,n,S):
    TIMES=[]
    #Original S를 O에 저장
    O=S
    if len(S)!=n:return 'djkfdjkf'
    else:
        for i in range(0,m):
            S=moveModulo(m,i,O)
            count=0
            print(S)
            while min(S)!=max(S):
                x=plusMin(m,S)
                print(x)
                S=x[0]
                count+=x[1]
            TIMES.append(count)
    return TIMES
n,m=map(int,input().split())
ss=input()
S=[int(i) for i in ss.split()]
print(S)
print(solveLock(m,n,S))
        
                
            
            
