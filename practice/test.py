Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=lambda x,y:x if x>y else y
>>> a(3,4)
4
>>> a=lambda x,y,z:if x>z+y or z>x+Y or y>z+x print("triangle")
SyntaxError: invalid syntax
>>> a=lambda x,y:x if x>y else y
>>> list(map(a,[1,2,3,4,5,6]))
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    list(map(a,[1,2,3,4,5,6]))
TypeError: <lambda>() missing 1 required positional argument: 'y'
>>> #filter
>>> c=lambda x:x>5
>>> list((filter(c,[1,2,3,4,5,6,7,8,9])))
[6, 7, 8, 9]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> from fuctools import reduce
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    from fuctools import reduce
ModuleNotFoundError: No module named 'fuctools'
>>> from functools import reduce
>>> d=lambda x,y:x+y
>>> 
>>> reduce(d,[1,2,3,4,5])
15
>>> a=lambda x,y,z:  print("triangle") if x>z+y or z>x+Y or y>z+x else print("wrong satement")
>>> a=[3,4,5]
>>> a=lambda x,y,z:print("triangle") if x>z+y or z>x+Y or y>z+x else print("wrong satement")
>>> a=[3,4,5]
>>> a
[3, 4, 5]
>>> a=lambda x,y,z:  print("triangle") if x>z+y or z>x+Y or y>z+x else print("wrong satement")