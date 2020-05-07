#n=input('enter sentence')
n='kaushik chakravorty is a fool'
l=n.split()
l1=[]
print(l)
for i in range(len(l)):
    if i%2==0:
        x=l[i]
        x=x[::-1]
        l[i]=x

    else:
        x=l[i]
        for j in x:
            l1.append(j)
        n=len(l1)
        for a in range(n):
            for j in range(n):
                
            
            
                if l1[j] in {'A','E','I','O','U','a','e','i','o','u'}:
                    
                    l1.append(l1[j])
                    print(l1)
                    
                    
                    
                    
                    del l1[j]
                    print(l1)
                    n=n-1
            
        l[i]=''.join(l1)
        l1=[]

            
        
        
print('{}'.format(' '.join(l)))

