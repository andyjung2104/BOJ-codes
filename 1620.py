import sys
digits={'1','2','3','4','5','6','7','8','9'}
N,M=map(int,input().split())
pokemon1=[0]
pokemon2={}
for n in range(N):
    e=sys.stdin.readline().strip()
    pokemon1.append(e)
    pokemon2[e]=(n+1)
for m in range(M):
    s=input()
    if s[0] in digits:
        print(pokemon1[int(s)])
    else:
        print(pokemon2[s])
