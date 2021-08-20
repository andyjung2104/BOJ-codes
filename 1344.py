from math import factorial
primes={2,3,5,7,11,13,17}
a=int(input())/100
b=int(input())/100
ap,bp=0,0
for p in primes:
    ap+=(a**p)*((1-a)**(18-p))*factorial(18)/(factorial(p)*factorial(18-p))
    bp+=(b**p)*((a-b)**(18-p))*factorial(18)/(factorial(p)*factorial(18-p))
print(1-ap-bp)
