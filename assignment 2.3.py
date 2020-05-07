l=[]
def chutiya():
    n=int(input("enter number"))
    
    l.append(n)
    s=sum(l)
    if s%4==0:
        c=input("enter more numbers?enter y for yes and N for no")
        if c=="Y":
        
            chutiya()
        else:
            print("final sum is",sum(l))
    
       
    else:
        print("not done nigga")
        
        
        
b=chutiya()
     
