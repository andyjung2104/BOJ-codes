w,h=map(int,input().split())
p,q=map(int,input().split())
t=int(input())
x=p+t
y=q+t
ans_x,ans_y=0,0
if x%(2*w)>w:
    ans_x=2*w-(x%(2*w))
else:
    ans_x=x%(2*w)
if y%(2*h)>h:
    ans_y=2*h-(y%(2*h))
else:
    ans_y=y%(2*h)

print(ans_x,ans_y)
