import sys
N=int(input())
M=int(input())
S=sys.stdin.readline().strip()
cnt=0
tmp=0
for i in range(M-1):
    if tmp>=1:
        if S[i]!=S[i+1]:
            #print('ㄱ')
            tmp+=1
        else:
            #print('ㄴ')
            cnt+=max(0,tmp//2+1-N)
            tmp=0
    else:
        #print('ㄷ')
        if S[i]=='I' and S[i+1]=='O':
            #print('ㄹ')
            tmp+=1
cnt+=max(0,tmp//2+1-N)
print(cnt)
