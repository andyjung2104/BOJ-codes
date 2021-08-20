s=input()
s=s.upper()
maxx=0
maxalphabet=s[0]
isOne=True
for g in set(s):
    t=s.count(g)
    if maxx<t:
        maxx=t
        maxalphabet=g
for g in set(s):
    if g!=maxalphabet:
        if s.count(g)==maxx:
            isOne=False
if isOne:
    print(maxalphabet)
else:
    print('?')
