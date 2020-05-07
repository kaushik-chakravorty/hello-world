l=input("enter string")
#x=len(l)
#print(x)
def check(a):
    if len(a)<=1:
      print("palindrome")
        
    else:
        if a[0]==a[-1]:
            check(a[1:-1])

        else:
             print("not palindrome")
check(l)
        
            

            
    
