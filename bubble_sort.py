def bubble(l):
    print(l,"l before starting")
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                #temp=l[j]
                #l[j]=l[j+1]
                #l[j+1]=temp
                l[j],l[j+1]=l[j+1],l[j]
            else:
                pass



l=[32,12,45,65,34,76,98,36,72]
bubble(l)
