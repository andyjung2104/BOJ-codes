def quad(x1,y1,x2,y2,x3,y3,x4,y4):
    return .5*abs(x1*y2+x2*y3+x3*y4+x4*y1-x2*y1-x3*y2-x4*y3-x1*y4)
def tri(x1,y1,x2,y2,x3,y3):
    return .5*abs(x1*y2+x2*y3+x3*y1-x2*y1-x3*y2-x1*y3)
x1,y1,x2,y2,x3,y3,x4,y4=map(int,input().split())
x=[0,x1,x2,x3,x4,x1,x2,x3,x4]
y=[0,y1,y2,y3,y4,y1,y2,y3,y4]
m1=(x1+x2)/2,(y1+y2)/2
m2=(x2+x3)/2,(y2+y3)/2
m3=(x3+x4)/2,(y3+y4)/2
m4=(x4+x1)/2,(y4+y1)/2
m=[0,m1,m2,m3,m4,m1,m2,m3,m4]
halfS=quad(x1,y1,x2,y2,x3,y3,x4,y4)*.5
minn=halfS+1-1
for i in range(0,4):
    minn=min(minn,abs(tri(x[1+i],y[1+i],x[4+i],y[4+i],m[3+i][0],m[3+i][1])-halfS),abs(tri(x[1+i],y[1+i],x[2+i],y[2+i],x[3+i],y[3+i])-halfS),abs(tri(x[1+i],y[1+i],m[2+i][0],m[2+i][1],x[2+i],y[2+i])-halfS))
for i in range(1,5):
    for j in range(i+1,5):
        if (j-i)==2:
            minn=min(minn,abs(quad(x[j],y[j],x[i+1],y[i+1],m[i][0],m[i][1],m[j][0],m[j][1])-halfS))
        elif (j-i)==1:
            minn=min(minn,abs(tri(x[j],y[j],m[i][0],m[i][1],m[j][0],m[j][1])-halfS))
        elif j==4 and i==1:
            minn=min(minn,abs(tri(x[1],y[1],m[1][0],m[1][1],m[4][0],m[4][1])-halfS))
print(halfS-minn,halfS+minn)
