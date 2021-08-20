import sys
r,c=map(int,input().split())
words=['' for i in range(c)]
for j in range(r):
    s=input()
    for i in range(c):
        words[i]+=s[i]
print(words)
    
