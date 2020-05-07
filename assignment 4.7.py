def check_double(n):
    z=n*2
    l1=[]
    l2=[]
    count=0
    count1=0
    i=0
    j=0
    while z%(10**i)!=z:
        count+=1
        l1.append((z//(10**i))%10)
        i=i+1

    
    while n%(10**j)!=n:
        count1+=1
        l2.append((n//(10**j))%10)
        j=j+1

    l1=sorted(l1)
    l2=sorted(l2)


    
    if count==count1 and l1==l2:
        print("True")
    else:
        print("False")


x=int(input("enter desired no"))
check_double(x)
        
