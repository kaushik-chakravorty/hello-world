#recursion
#b=[1,2,3,4,5]
#for 5 digit numbers
b=int(input("number?"))
l=[1,1,1,1,1]
def suma(a):
    sum1=0
    for i in a:
        sum1=sum1+i
    return sum1    


def convert(x):
    for i in range(0,5):
        if i==0:
            l[-1]=(x%10)

        else:
            l[-(i+1)]=(x%(10**(i+1))-(x%(10**(i))))//(10**i)

convert(b)
print("sum of digits= ",suma(l))
    
