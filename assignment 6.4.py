l=[]
n=int(input('enter no'))
if n<=12:
    for i in range(1,101):
        for j in range(1,i+1):
            if i%j==0:
                l.append(j)
        if len(l)==n:
            print(i)
            break;
        l=[]

else:
    for i in range(101,10001):
        for j in range(1,i+1):
            if i%j==0:
                l.append(j)
        if len(l)==n:
            print(i)
            break;
        l=[]
        

    
