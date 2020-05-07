
def calculator():
    
    
    

    
    x=float(input("enter the distance in km"))
    n=input("enter no of passengers? enter Y for yes and N for no")
    ticket=0
    
    
    l=[]
    if n=='Y':

        c=int(input("enter no. of passengers"))
        for i in range(c):
            ticket=ticket+c*80
            minus=(x/10)*70
        if ticket-minus<0:
            print (-1)
        else:
            print( "a profit of {}".format(ticket-minus))




calculator()
        
            
        
