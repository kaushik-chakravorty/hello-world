l=[2]
def palindrome(a):
    
    if len(a)==1 or len(a)==0:
        return 1
    else:
        if a[0]==a[-1]:
            del a[0]
            del a[-1]
            return 1
            palindrome(a)
        else:
            return 0
b=palindrome(l)
if b==1:
    print("palindrome")
else:
    print("no success")
        
    
        
        
        
    
