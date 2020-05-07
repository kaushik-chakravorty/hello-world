#code to create a function which returns the list minus all duplicates
l1=[1,1,2,3,4,4,5,6,7,7]
l2=[2,33,67,67,89,65,45]
l3=[]
def minus_duplicates(x):
    d={}
    for i in x :
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    for i in d:
        if d[i]>1:
            d[i]=1
        else:
            d[i]=1
    print(d)
    for i in d.keys():
        l3.append(i)
        
 
minus_duplicates(l1)

minus_duplicates(l2)


