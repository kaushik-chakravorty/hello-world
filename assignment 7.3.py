l1=['their,business,windows,were,sample']
print(l1)
d={}
count1=0
count2=0
count3=0
counterror=0
l2=[]

l=["THEIR","BUSINESS" ,"WINDOWS","WERE","SAMPLE"]

for i in l:
    d[i]=input('enter spellings in CAPS')


print(d)

for i in d:
    a=i
    b=d[i]
    print(a,b)
   
        
        
    if len(a)!=len(b):
        count3+=1
        
    else:
        counterror=0
        for j in range(len(a)):
            if a[j]!=b[j]:
                counterror+=1
        if counterror==0:
            count1+=1
        elif counterror<=2:
            count2+=1
        else:
             count3+=1
l2.append(count1)
l2.append(count2)
l2.append(count3)




