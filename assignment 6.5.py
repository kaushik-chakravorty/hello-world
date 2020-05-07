l=[12,54,68,759,24,15,987,758,25,69]
d={}
l1=[]
for i in l:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1

for i in d:
    if d[i]>1:
        l1.append(i)
print(l1)
