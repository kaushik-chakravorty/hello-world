a=input('enter first string')
b=input('enter second string')
l1=[]
l2=[]

def check_anagram(l1,l2):
    
    for i in range(len(l1)):
        if l1[i]==l2[i]:
            return 'not anagram'
    s1=set(l1)
    s2=set(l2)
    
    if s1.issubset(s2) and s2.issubset(s1):
        return 'anagram'
    else:
        return 'not anagram'
    




if len(a)!=len(b):
    print('not anagram')
else:
    for i in a:
        l1.append(i)
    for i in b:
        l2.append(i)
    c=check_anagram(l1,l2)
    print(c)
