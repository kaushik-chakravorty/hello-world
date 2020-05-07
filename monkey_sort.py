import random

def  is_sorted(l):
    for i in range(0,len(l)-1):
        if l[i]<l[i+1]:
            return False
    return True







def monkey_sort(l):
    random.shuffle(l)
    if is_sorted(l):
        print(l)
    else:
        print(l)
        monkey_sort(l)


monkey_sort([1,34,21,56,12])
