#selection sort#complexity is n^2
l=[1,2,34,65,23,12,54,67,43,90,32,56,]
def selection(l):
    for i in range(len(l)):
        bigindex=0
        
        for j in range(len(l)-i):
            if l[bigindex]<l[j]:
                bigindex=j
        l[j],l[bigindex]=l[bigindex],l[j]
        print("largest element gets sent to the last position and bigindex is initialised to 0\n",l)
    print(l)

selection(l)

        
