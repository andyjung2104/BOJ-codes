#1520a
T=int(input())
for _ in range(T):
    n=int(input())
    s=input()
    al={s[0]}
    num=1
    for i in range(1,n):
        if s[i-1]!=s[i]:
            num+=1
            al.add(s[i])
    if num!=len(al):
        print('NO')
    else:
        print('YES')
