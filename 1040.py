#1040
n=input()
k=int(input())

#def make(n,k):
zero_to_nine={0,1,2,3,4,5,6,7,8,9}

if len(n)<k:
    #k=2:10
    print('10',end='')
    for t in range(2,k):
        print(t,end='')
else:
    ind=0
    enough=False
    digits=set()
    for i in range(len(n)):
        digits.add(int(n[i]))
        if len(digits)==k:
            enough=True
            break
    if enough:
        if int(n[i+1])<=max(digits):
            #n[i+1]=n[i+2]=...=n[len(n)-1]=min(digits)
            for j in range(i+1):
                print(n[j],end='')
            for j in range(i+1,len(n)):
                print(min(digits),end='')
        if int(n[i+1])>max(digits):
            #n[i]+1 if n[i]<9, else n[i+1]+1 else
            n[i]+=1
