def f(x,T,D):
    u=x//D
    return min(u*T+x%D,(u+1)*T+(u+1)*D-x)
x,y,D,T=map(int,input().split())
print(f(x,T,D)+f(y,T,D))
