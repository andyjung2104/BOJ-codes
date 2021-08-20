VOWEL={'a','e','i','o','u','y'}
def first_cluster(word):
    s=''
    for b in word:
        if b in VOWEL:break
        else:
            s=s+b
            word=word[1:]
    return s,word
def topiglatin(word):
    if word[0] in VOWEL:
        return word+'yay'
    else:
        f=first_cluster(word)
        return f[1]+f[0]+'ay'
T=int(input())
for i in range(T):
    s=input()
    for word in s.split():
        print(topiglatin(word),end=' ')

    print('')
