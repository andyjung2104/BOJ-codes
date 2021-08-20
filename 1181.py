n=int(input())
S=[]
for i in range(n):
    t=input()
    S.append((len(t),t))
K=[]
for length in range(1,51):
    K=[]
    for s in S:
        if s[0]==length:
            K.append(s[1])
    K.sort()
    for k in K:
        print(k)
