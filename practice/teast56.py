value=['823','863']
num=value[0][0:]
for i in range(len(value)):
    for j in range(len(value[i])):
        if num>value[i][j:]:
            print(num)
            print(value[i][j:])
            num=value[i][j:]
print(num)
