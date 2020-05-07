l=[1,2,3,4,5,6]
l1=[]
for i in range(0,len(l)):
     for j in range(i+1,len(l)):
            if (l[i]+l[j])%4==0:
                l1.append((l[i],l[j]))
        
        
if l1==[]:
    print("no such pairs")
else:
    print(l1)
    
