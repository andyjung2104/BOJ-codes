LIST=['c=','c-','dz=','d-','lj','nj','s=','z=']
S=input()
count=0
while len(S)>0:
    if S[:3] in LIST:
        if len(S)>3:S=S[3:]
        else:S=''
        count+=1
    elif S[:2] in LIST:
        if len(S)>2:S=S[2:]
        else:S=''
        count+=1
    else:
        count+=1
        S=S[1:]
print(count)
