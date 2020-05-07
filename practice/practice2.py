#recursion
#gives sum of digits for n digit number
l=[]
n=int(input("digits btao"))
b=int(input("number?"))

for i in range(0,n):
    l.append(1)

def suma(a):
    sum1=0
    for i in a:
        sum1=sum1+i
    return sum1

    
def convert(x):
    for i in range(0,n):
        if i==0:
            l[-1]=(x%10)

        else:
            l[-(i+1)]=(x%(10**(i+1))-(x%(10**(i))))//(10**i)

convert(b)
print("sum of digits= ",suma(l))
    
