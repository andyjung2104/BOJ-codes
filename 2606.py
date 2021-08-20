n=int(input())
k=int(input())
K=[]
for _ in range(k):
    i,j=map(int,input().split())
    K.append((i,j))


vir={1}
while True:
    #변화
    q=0
    for k in K:
        if k[0] in vir and k[1] not in vir:
            vir.add(k[1])
            q+=1
        elif k[1] in vir and k[0] not in vir:
            vir.add(k[0])
            q+=1
    if q==0:
        break
#print(vir)
print(len(vir)-1)
    
