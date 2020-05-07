a=int(input('enter lower range'))
b=int(input('enter upper range'))
sample_l=[]
def even():
    l_even=[]
    for i in sample_l:
        if i%2==0:
            l_even.append(i)
    return l_even
def odd():
    l_odd=[]
    for i in sample_l:
        if i%2!=0:
            l_odd.append(i)
    return l_odd
def sum_of_numbers(a):
    if str(type(a))=="<class 'list'>":
        print(a)
        return sum(a)
    elif str(type(a))=="<class 'function'>":
        c=a()
        print(c)
        
        return sum(c)
    else:
        print('invalid input')
        
for i in range(a,b+1):
    sample_l.append(i)

c=sum_of_numbers(odd())
print(c)
        
