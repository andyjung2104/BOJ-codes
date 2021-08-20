#7561
def det(A,n=3):
    if n==2:
        return A[0][0]*A[1][1]-A[1][0]*A[0][1]
    elif n==3:
        return A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])-A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])+A[0][2]*(A[1][0]*A[2][1]-A[2][0]*A[1][1])
#print(det([[1,4,5],[4,1,2],[4,8,1]]))

def matmul(A,B):
    return [[sum([(A[j][i]*B[i][k]) for i in range(3)]) for k in range(3)] for j in range(3)]
t=int(input())
#
for _ in range(t):
    A=[]
    b=[]
    x=[]
    detAi=[]
    for i in range(3):
        l=list(map(int,input().split()))
        A.append(l[:3])
        b.append(l[3])
    detA=det(A)
    #print(A)
    detAi.append(det([[b[i]]+A[i][1:] for i in range(3)]))
    detAi.append(det([[A[i][0],b[i],A[i][2]] for i in range(3)]))
    #print([[A[i][:2]+[b[i]]] for i in range(3)])
    detAi.append(det([A[i][:2]+[b[i]] for i in range(3)]))
    print(*(detAi+[detA]))
    if detA==0:
        print('No unique solution\n')
        continue
    else:
        print('Unique solution: ',end='')
    for dett in detAi:
        x.append(dett/detA)
    
    for e in x:
        if -0.0005<e<0.0005:print('0.000',end=' ')
        else:
            print('%.3f' % e, end=' ')
    print('\n')
    
