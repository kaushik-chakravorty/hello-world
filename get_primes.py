#prime number
def get_primes(n):
    l=[]
    for i in range(2,n+9):
        count=0
        
        for j in range(2,i):
            if i%j==0:
                count+=1


        if count==0:
            l.append(i)
            
        else:

            pass

    return l


def largest_prime(n,count,l2):
    if count<=8:
        l1=[]
        for i in range(0,len(l)):
            if n%l[i]==0:
                l1.append(l[i])
            else:
                pass

        l2.append(max(l1))
        
        
    
        largest_prime(n+1,count+1,l2)

    else:
        x=sum(l2)
        print(x)
           
            
l2=[]
n=int(input("enter the base number"))
l=get_primes(n)
largest_prime(n,0,l2)

