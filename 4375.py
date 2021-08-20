import math
while True:
    try:
        
        n=int(input())
        tmp=1
        while True:
            
            if pow(10,tmp,n)==1:
                print(tmp)
                if n%3!=0:
                    print(tmp)
                elif n%9==0:
                    print(math.lcm(9,tmp))
                else:
                    print(math.lcm(3,tmp))
                break
            else:
                tmp+=1
    except EOFError:
        break
    
