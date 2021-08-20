#5582
s1=input()
s2=input()
LCS=[[0 for j in range(len(s1)+1)] for i in range(len(s2)+1)]
ans=0
for j in range(1,len(s2)+1):
    for i in range(1,len(s1)+1):
        if s1[i-1]==s2[j-1]:
            LCS[j][i]=LCS[j-1][i-1]+1
            ans=max(ans,LCS[j][i])
print(ans)
