a=input('enter text')
l=a.split()
d={}
l1=[]
l2=[]
for i in l:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
for i in d.values():
    l1.append(i)

b=max(l1)

for i in d:
    if d[i]==b:
        l2.append(i)



if len(l2)==1:
    print("word with maximum frequency is {} {}".format(l2[0],b))
else:

    c=l2[0]
    x=1
    for i in range(1,len(l2)):
        
        if len(c)<len(l2[i]):
            
            c=l2[i]
            
        else:
            pass
    print("word with maximum frequency is {} {}".format(c,b))
        
    

        
