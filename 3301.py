def lcs(s1,s2):
    LCS=[['' for j in range(len(s1)+1)] for i in range(len(s2)+1)]
    ans=''
    ret=[]
    for j in range(1,len(s2)+1):
        for i in range(1,len(s1)+1):
            if s1[i-1]==s2[j-1]:
                LCS[j][i]=LCS[j-1][i-1]+s1[i-1]
                if len(ans)<len(LCS[j][i]):
                    ans=LCS[j][i]
                    ret=[ans]
                elif len(ans)==len(LCS[j][i]):
                    ret.append(LCS[j][i])
            else:
                if len(LCS[j-1][i])<len(LCS[j][i-1]):
                    LCS[j][i]=LCS[j][i-1]
                else:
                    LCS[j][i]=LCS[j-1][i]
    return ret
a=input()
b=input()
c=input()
l1=lcs(a,b)
print(l1)
m=0
ans=''
for s in l1:
    y=lcs(s,c)
    if len(y[0])>m:
        m=len(y[0])
        ans=y[0]
    
print(y[0])
