#recursive function to check if a string is a a palindrome or not
def palindrome(l):
    if len(l)<=1:
        print('palindrome')
    elif l[0]==l[-1]:
        del l[0],l[-1]
        palindrome(l)
    else:
        print( 'not palindrome')
l=[]
n=input('string')
for i in range(len(n)):
    l.append(n[i])
#l=n.split()
#print(l)
palindrome(l)
