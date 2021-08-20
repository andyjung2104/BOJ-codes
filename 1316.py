#1316
def isGroup(str):
    if len(str)==0:return True
    state=0
    k=str[0]
    while True:
        if len(str)==0:break
        if str[0]!=k:break
        str=str[1:]
    if str.count(k)!=0:
        return False
    return isGroup(str)
