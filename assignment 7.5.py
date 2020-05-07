n=input('enter string')
l=n.split()
l2=[]
def sms_encoder(x,n):
    l1=[]
    count=0
    for i in x:
        l1.append(i)
    

    for j in range(len(l1)):
        if l1[j] in {'A','E','I','O','U','a','e','i','o','u'}:
            count=count+1
    if count==0 or len(l1)==1:
        a=''.join(l1)
        
        l2.append(a)
    else:
        
        if l1[n] in {'A','E','I','O','U','a','e','i','o','u'}:
            del l1[n]
            sms_encoder(''.join(l1),n)
        else:
            n=n+1
            sms_encoder(''.join(l1),n)
for i in range(len(l)):
    sms_encoder(l[i],0)

print(type(l2))

print(' '.join(l2))



            
        
