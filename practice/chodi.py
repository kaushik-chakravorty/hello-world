#recursion
#gives sum of digits for n digit number
l=[1]
#n=int(input("digits btao"))
b=int(input("number?"))

#for i in range(0,n):
    #l.append(1)

def suma(a):
    sum1=0
    for i in a:
        sum1=sum1+i
    return sum1

    
def convert(x):
    
    for i in l:
        if l==[1]:
            l.append(x%10)

        else:
            l.append((x%(10**(i+1))-(x%(10**(i))))//(10**i))
            l.append(1)

convert(b)
del l[0]
print("sum of digits= ",suma(l))
print(l)
    
