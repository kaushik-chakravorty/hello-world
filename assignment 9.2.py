def sum_checker(x):
    l=[]
    while x>0:
        l.append(x%10)
        x=x//10
        a=sum(l)
        return a
        




def validate_card_number(n):
    l1=[]
    l2=[]
    for i in range(len(n)):
        if i%2==0:
            l1.append(int(n[i]))
        else:
            l2.append(int(n[i]))
    for i in l1:
        i=i*2
    

    for i in range(len(l1)):
        if l1[i]>9:
            l1[i]=sum_checker(l1[i])
            
    print(sum(l1)+sum(l2))
    if (sum(l1)+sum(l2))%10==0:
        
        print('jaao paisa nikal lo')
    else:
        print('chori krta hai chetibod')
        
            
        

n=input('enter 16 digit card number')
if len(n)==16:
    validate_card_number(n)
else:
    print('chutiya hai kya madarchod dikhta nai 16 digit ka no pucha hai!')
    
