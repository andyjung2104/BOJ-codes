#9158
from itertools import combinations
from numpy.linalg import det

def dis(p1,p2):
    return sum([(p1[i]-p2[i])**2 for i in range(3)])**.5

def sphere(st1,st2,st3,st4):
    #a(x^2+y^2+z^2)+bx+cy+dz+e=0
    #O(-b/2a,-c/2a,-d/2a), R=sqrt((b^2+c^2+d^2)/4a^2-e/a)
    Q=[]
    Q.append([sum([st1[i]**2 for i in range(3)]),st1[0],st1[1],st1[2],1])
    Q.append([sum([st2[i]**2 for i in range(3)]),st2[0],st2[1],st2[2],1])
    Q.append([sum([st3[i]**2 for i in range(3)]),st3[0],st3[1],st3[2],1]) 
    Q.append([sum([st4[i]**2 for i in range(3)]),st4[0],st4[1],st4[2],1]) 
    a=det([r[1:] for r in Q])
    b=-det([r[:1]+r[2:] for r in Q])
    c=det([r[:2]+r[3:] for r in Q])
    d=-det([r[:3]+r[4:] for r in Q])
    e=det([r[:4] for r in Q])
    O=(-b/(2*a),-c/(2*a),-d/(2*a))
    return O,((b**2+c**2+d**2)/(4*a**2)-e/a)**.5,dis(O,st1),dis(O,st2),dis(O,st3),dis(O,st4)
    
    
while True:
    n=int(input())
    if n==0:break
    stars=[]
    for i in range(n):
        x,y,z=map(float,input().split())
        stars.append((x,y,z))
    print(sphere(*stars))
