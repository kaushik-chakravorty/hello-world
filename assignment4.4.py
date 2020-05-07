l= (12,18,25,24,2,5,18,20,20,21)

def mta(l):
    sums=0
    count=0
    for i in l:
        sums=sum(l)
    avg=sums//len(l)
    for i in l:
        if i>avg:
            count+=1
    print("% of students who scored more than average marks will be",(count/len(l))*100)


def generate_frequency(l):
    l1=[]
    
    for i in range(25):
        count=0
        for j in range(len(l)):
            if l[j]==i:
                count+=1

            
            

        if count==0:
            l1.append(0)

        else:
            l1.append(count)

    count=0
    for i in l:
        
        if i==25:
            count+=1
    l1.append(count)
    

    print(l1)
    print(len(l1))
n=input("enter 1 for mta and 2 for generate frequency")

if n=='1':
    mta(l)

elif n=='2':
    generate_frequency(l)
else:
    print("wrong input")
    
    


        
            
        
