import random
#t=int(input("enter no to be checked"))

#n=int(input("enter digits of no"))
t=random.randint(1000,9999)
l=[]
while l is not ['M','M','M','M']:
    
    for i in range(0,4):
        h=int(input("enter random no"))
        if (h%(10**(i+1))-h%(10**i))==(t%(10**(i+1))-t%(10**i)):
            l.append("M")
        else:
            l.append("P")
            print(l)
            #if l==['M','M','M','M']:
                    #print("you are right")

    
