def create_largest_number(l):
    x=''
    l.sort(reverse=True)
    for i in l:
        x=x+'{}'.format(i)

    print(x)
l=[23,34,55]
create_largest_number(l)
    
