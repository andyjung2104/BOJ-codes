#1195
a=input().strip()
s1=a[:]
b=input().strip()
s2=b[:]
def isokay(list1,list2):
    for i in range(min(len(list1),len(list2))):
        if int(list1[i])+int(list2[i])>=4:return False
    return True
minlen=len(s1+s2)
for i in range(len(s2)+1):
    
    if isokay(s1,s2):
        minlen=min(minlen,max(len(s2),len(s1)))
    s1='0'*i+a
s1=a
for j in range(1,len(s1)+1):
    if isokay(s1,s2):
        minlen=min(minlen,max(len(s1),len(s2)))
    s2='0'*j+b
print(minlen)
