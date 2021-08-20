n,k=map(int,input().split())
remainingnums=k
printed=False
for i in range(1,n+1):
    s=len(str(i))
    if s<remainingnums:
        remainingnums-=s
    else:
        print(str(i)[remainingnums-1])
        printed=True
        break
if not printed:
    print(-1)
