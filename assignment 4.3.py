l=[3, 4, 1, 8, 5, 9, 0, 6]
n=9
l1=[]
l2=[]
for i in l:
    for j in l:
        if i!=j and i+j==n and i!=j:
            x=(i,j)
            l1.append(x)


    

print("no. of pairs available are ", (len(l1)//2))
