#3905
import sys,math

def ok(star,tel):
    inner=star[0]*tel[0]+star[1]*tel[1]+star[2]*tel[2]
    S=(star[0]**2+star[1]**2+star[2]**2)**.5
    T=(tel[0]**2+tel[1]**2+tel[2]**2)**.5
    theta=math.acos(inner/(S*T))
    return tel[3]>theta
while True:
    n=int(input())
    if n==0:break
    stars=[]
    for i in range(n):
        x,y,z=map(float,sys.stdin.readline().split())
        stars.append((x,y,z))
    m=int(input())
    tels=[]
    for j in range(m):
        x,y,z,phi=map(float,sys.stdin.readline().split())
        tels.append((x,y,z,phi))
    starcnt=0
    for star in stars:
        for tel in tels:
            if ok(star,tel):
                starcnt+=1
                break
    print(starcnt)
