n=int(input("enter number"))
#z=int(input("digits"))
l=[]
c=1

def digit_calculator(a):
    c=1
    while a//10!=0:
        a=a/10
        c+=1
        
    return c
    
    
    
        
def no_seperator(n,z):
    for i in range(0,z):
        if i==0:
            l.append(n%10)
        else: 
            l.append((n%(10**(i+1))-(n%(10**i)))//(10**i))
    L=l[::-1]
    return L

def armstrong(n,l):
    sums=0
    for i in l:
        sums=sums+i**3
    if sums==n:
        print("armstrong number")
    else:
        print("no pussy dude")
                 
        
    
a=no_seperator(n,digit_calculator(n))
armstrong(n,a)

