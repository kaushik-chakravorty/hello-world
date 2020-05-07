for i in range(1,50):
    if i%3==0:
        
        print(i,"zip\n")
    elif i%5==0:
        print(i,"zap\n")
    elif i%3==0 and i%5==0:
        print(i,"zoom\n")
    else:
        print(i,"invalid")
