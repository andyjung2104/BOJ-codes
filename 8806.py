#8806
z=int(input())
for _ in range(z):
    
    x1,y1,z1=map(float,input().split())
    x2,y2,z2=map(float,input().split())
    adam=x1*y2+y1*z2+z1*x2
    gos=x2*y1+y2*z1+z2*x1
    if adam>gos:
        print('ADAM')
    elif adam==gos:
        print('=')
    else:print('GOSIA')
