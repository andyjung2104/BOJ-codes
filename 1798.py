import math,sys
def ans(r,h,d1,A1,d2,A2):
    dB=min(abs(A1-A2),360-abs(A1-A2))*r/((r**2+h**2)**.5)
    return (d1**2+d2**2-2*d1*d2*math.cos(dB*math.pi/180))**.5

while True:
    try:
        s=input()
        r,h,d1,A1,d2,A2=map(float,s.split())
        print('%.2f' % ans(r,h,d1,A1,d2,A2))
    except:
        break
