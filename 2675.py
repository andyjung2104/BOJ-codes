def o(s,num):
    st=''
    for u in s:
        st=st+u*num
    return st
t=int(input())
for i in range(t):
    a,b=input().split()
    print(o(b,int(a)))
