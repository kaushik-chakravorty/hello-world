
n=input("enter string")
l=[]
l2=[]
for i in range(len(n)):
    l.append(int(n[i]))




for i in range(len(l)):
    sums=l[i]
    l1=[l[i]]
    for j in range(i+1,len(l)):
        sums=sums+l[j]
        if sums<10:
            l1.append(l[j])
        elif sums==10:
            l1.append(l[j])
            l2.append(l1)
            exit
        else:
            
            l1=[]
            exit
            
print(l2)
            

            
