a=[1,2,3,4]
sets=[]
S=6
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==S:
            print(sets.append([a[i],a[j]]))

for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        for k in range(j+1,len(a)):
            if a[i]+a[j]+a[k]==S:
                print (sets.append([a[i],a[j],a[k]]))

print(sets)
