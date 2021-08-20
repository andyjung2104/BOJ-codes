s=input()
isminus=False
nums=[]
p_m=[]
num=''
for i in range(len(s)):

    if s[i] in {'+','-'}:
        nums.append(int(num))
        p_m.append(s[i])
        num=''
    else:
        num=num+s[i]
nums.append(int(num))

if '-' not in p_m:
    print(sum(nums))
else:
    x=p_m.index('-')
    print(sum(nums[:(x+1)])-sum(nums[(x+1):]))
