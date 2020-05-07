#program to integrate functions correctly upto 3 places of decimal
def integrate_final():
    a=float(input('enter lower limit'))
    b=float(input('enter upper limit'))
    x=[]
    s=[]
    y=[]
    i=a
    h=0.00001#step length
    #for i in range(a,b,0.000000001):
    while i<b:
        i+=h
        x.append(i)

    for i in range(0,len(x)):
        y.append(x[i]**2)
    for i in range(0,len(y)):
        s.append(y[i]*h)
        
        
    sums=sum(s)

    print('the integration value is',sums)

def function():
    
