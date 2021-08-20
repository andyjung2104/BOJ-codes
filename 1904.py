#a_1=1,a_2=2,a_3=3
X=[1,2]
n=int(input())
for i in range(n-2):
    X.append(X[i]+X[i+1])
if n!=1:print(X[-1])
elif n==1:print(1)
elif n==2:print(2)
