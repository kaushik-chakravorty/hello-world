Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as num
>>> a=num()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a=num()
TypeError: 'module' object is not callable
>>> num
<module 'numpy' from 'C:\\Users\\KAUSHIK\\AppData\\Local\\Programs\\Python\\Python38-32\\lib\\site-packages\\numpy\\__init__.py'>
>>> num=2
>>> num
2
>>> num
2
>>> type(num)
<class 'int'>
>>> 
>>> 
>>> 
>>> 
>>> 
>>> import numpy as num
>>> num
<module 'numpy' from 'C:\\Users\\KAUSHIK\\AppData\\Local\\Programs\\Python\\Python38-32\\lib\\site-packages\\numpy\\__init__.py'>
>>> num()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    num()
TypeError: 'module' object is not callable
>>> import numpy
>>> import numpy as no
>>> a=no.array([1,2,3,4,5])
>>> print(a)
[1 2 3 4 5]
>>> print(no.__version__)
1.18.2
>>> type(a)
<class 'numpy.ndarray'>
>>> b=no.array(23)
>>> b
array(23)
>>> print(b)
23
>>> type(b)
<class 'numpy.ndarray'>
>>> c=no.array([1,2,3,4],[5,4,3,6])
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    c=no.array([1,2,3,4],[5,4,3,6])
TypeError: data type not understood
>>> c=no.array([[1,2,3,4],[5,4,3,6]])
>>> 
>>> c
array([[1, 2, 3, 4],
       [5, 4, 3, 6]])
>>> print(c)
[[1 2 3 4]
 [5 4 3 6]]
>>> d=no.array([[[1,2],[3,4]],[[5,6],[7,8]]])
>>> 
>>> print(d)
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
>>> d
array([[[1, 2],
        [3, 4]],

       [[5, 6],
        [7, 8]]])
>>> print(d)
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
>>> print(b.ndim)
0
>>> print(a.ndim)
1
>>> print(d.ndim)
3
>>> d.ndim()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    d.ndim()
TypeError: 'int' object is not callable
>>> a=no.array([1,2,3,4],ndim=5)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a=no.array([1,2,3,4],ndim=5)
TypeError: 'ndim' is an invalid keyword argument for array()
>>> a=no.array([1,2,3,4],ndmin=5)
>>> 
>>> print(a)
[[[[[1 2 3 4]]]]]
>>> print(a.ndim)
5
>>> print(c)
[[1 2 3 4]
 [5 4 3 6]]
>>> print(c[1,4])
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    print(c[1,4])
IndexError: index 4 is out of bounds for axis 1 with size 4
>>> print(c[1,3])
6
>>> print(d)
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
>>> print(d[0,0,0])
1
>>> print(d[1,1,1])
8
>>> l=[]
>>> for i in range(0,2):
	for \

	    
SyntaxError: invalid syntax
>>> 
>>> print(d[-1,-1,-1])
8
>>> print(a)
[[[[[1 2 3 4]]]]]
>>> a=no.array([1,2,3,4,5])
>>> a[1:3]
array([2, 3])
>>> print(a[1:4])
[2 3 4]
>>> l=[1,2,3,4,5]
>>> l[1:4]
[2, 3, 4]
>>> print(a[1:])
[2 3 4 5]
>>> print(a[-3:-1])
[3 4]
>>> print(a[-3:])
[3 4 5]
>>> print(a[-3:-3])
[]
>>> print(a[0::2])
[1 3 5]
>>> print(a[0::2])
[1 3 5]
>>> len(a)
5
>>> print(a)
[1 2 3 4 5]
>>> type(a)
<class 'numpy.ndarray'>
>>> print(a[::2])
[1 3 5]
>>> print(c)
[[1 2 3 4]
 [5 4 3 6]]
>>> print(a[1,1:3])
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    print(a[1,1:3])
IndexError: too many indices for array
>>> print(c[1,1:3])
[4 3]
>>> print(c[1:3,1])
[4]
>>> 
>>> print(c[1:2,1])
[4]
>>> print(c[0:2,1])
[2 4]
>>> x=c[0:2,1]
>>> x
array([2, 4])
>>> print(x)
[2 4]
>>> x=list(c[0:2,1])
>>> x
[2, 4]
>>> type(x)
<class 'list'>
>>> y=no.array(['1','2',3])
>>> type(y)
<class 'numpy.ndarray'>
>>> print(y.dtype)
<U1
>>> print(y)
['1' '2' '3']
>>> print(type(y[2]))
<class 'numpy.str_'>
>>> type(y[2])
<class 'numpy.str_'>
>>> y=no.array(['1',2,3])
>>> type(y[2])
<class 'numpy.str_'>
>>> type(y[0])
<class 'numpy.str_'>
>>> print(y.dtype)
<U1
>>> y=no.array(['1','2','3'])
>>> print(y.dtype)
<U1
>>> f=no.array([2.3,4.5,6.7])
>>> print(f.dtype)
float64
>>> fnew=f.astype('c')
>>> print(fnew)
[b'2' b'4' b'6']
>>> print(f)
[2.3 4.5 6.7]
>>> fnew1=f.astype('i')
>>> print(fnew1)
[2 4 6]
>>> fnew2=f.astype('S')
>>> print(fnew2)
[b'2.3' b'4.5' b'6.7']
>>> fnew2=f.astype('b')
>>> print(fnew2)
[2 4 6]
>>> fnew2=f.astype(bool)
>>> print(fnew2)
[ True  True  True]
>>> fnew2=f.astype(complex)
>>> print(fnew2)
[2.3+0.j 4.5+0.j 6.7+0.j]
>>> 