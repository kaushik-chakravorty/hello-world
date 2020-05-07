def greatest():
    num1=int(input("enter lower limit"))
    if num1>9:
        num2=int(input("enter upper limit"))
        
        i=num1
        l=[]
        while i<=num2:
        
            if i%100==i:
                if ((i%10)+(i//10))%3==0 and i%5==0:
                    l.append(i)
                #elif i%5==0:
                    #l.append(i)
                else:
                    pass
            else:
                print(-1)
                return
            i+=1
        if l==[]:
            print(-1)
        else:
            n=max(l)
            print(n)
    else:
        print("-1\ninput musgt be of double digits")

greatest()
        

                
                
                
            
