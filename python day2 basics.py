>>> ##strings##
>>> str1='good morning'
>>> str1
'good morning'
>>> print(str1)
good morning

>>> print(str1[2])
o
>>> l=len(str1)
>>> l
12
>>> print(str1[0:len(str1):1])
good morning
>>> print(str1[::1])
good morning
>>> print(str1[len(str1):0:-1])
gninrom doo
>>> print(str1[::-1])
gninrom doog
>>> str1="hello"
>>> str2="hello"
>>> str3="hii"
>>> print(str1==str2)
True
>>> print(str1==str3)
False
>>> str1==str2
True
>>> print(str3*5)
hiihiihiihiihii
>>> ##formatting of strings##
>>> #the format() method formats the specifies values and inserts them in the string placeholder.
>>> #the place holder is defined using the curly brackets {}.the format() method returns the formatted sring...syntax: string.format(val1,val2,...)
>>> txt = "For only {price:.2f} dollars!"
>>> print(txt.format(price = 49))
For only 49.00 dollars!
>>> txt = "For only {price=.2f} dollars!"
>>> m=1.22
>>> print("%d"%m)
1
>>> print("%f"%m)
1.220000
>>> print("%d",%m)
SyntaxError: invalid syntax
>>> print("%d",m)
%d 1.22
>>> print("there are {0} books".format(10))
there are 10 books
>>> print("there are {price:.2f} books".format(price=10))
there are 10.00 books
>>> m=1.21
>>> n=12
>>> print("the  value of m is {0} and the value of n is {1}".format(m,n))
the  value of m is 1.21 and the value of n is 12
>>> str="hello"
>>> print(str.startswith('h'))
True
>>> print(str.startswith("he"))
True
>>> print(str.endswith("o"))
True
>>> print(str.startswith('e'))
False
>>> print(str.startswith('e',1))
True
>>> print(str.startswith('ell',1,4))
True
>>> print(str.startswith('ell',1,3))
False
>>> #print(str.starswith('ell',1,5)) gives error
>>> ##user input##
>>> n=int(input("enter n value"))
enter n value10
>>> print(n)
10
>>> n=type(input("enter n value"))
enter n value10
>>> print(n)
<class 'str'>
>>> n
<class 'str'>
>>> str1="book,pen,pencil,table,fan,lamp,papers"
>>> str1
'book,pen,pencil,table,fan,lamp,papers'
>>> type(str1)
<class 'str'>
>>> name=str.split(',')
>>> name
['hello']
>>> name=str1.split(',')
>>> name
['book', 'pen', 'pencil', 'table', 'fan', 'lamp', 'papers']
>>> type(name)
<class 'list'>
>>> name=str1.split(",",2)
>>> print(name)
['book', 'pen', 'pencil,table,fan,lamp,papers']
>>> name=str1.split(",",-2)
>>> name
['book', 'pen', 'pencil', 'table', 'fan', 'lamp', 'papers']
>>> name=str1.split(",",3)
>>> name
['book', 'pen', 'pencil', 'table,fan,lamp,papers']
>>> name=str1.split(",",6)
>>> name
['book', 'pen', 'pencil', 'table', 'fan', 'lamp', 'papers']
>>> name.append('chocolate')
>>> name
['book', 'pen', 'pencil', 'table', 'fan', 'lamp', 'papers', 'chocolate']
>>> str1
'book,pen,pencil,table,fan,lamp,papers'
>>> sep="-"
>>> date=sep.join('20','8','2020')
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    date=sep.join('20','8','2020')
TypeError: join() takes exactly one argument (3 given)
>>> date=sep.join(('20','8','2020'))
>>> date
'20-8-2020'
>>> #join() takes exactly one argument
>>> type(date)
<class 'str'>
>>> date=sep.join(['20','8','2020'])
>>> date
'20-8-2020'
>>> type(date)
<class 'str'>
>>> n=-2
>>> if(n<0):
	print("negative")
else:
	print("positive")

	
negative
>>> ##loops##
>>> print(list(range(5)))
[0, 1, 2, 3, 4]
>>> a=list((range(5)))
>>> a
[0, 1, 2, 3, 4]
>>> a=list(range(10))
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a=list(range(5,10,2))
>>> print(a)
[5, 7, 9]
>>> for i in range(2,8,2):
	print(i)

2
4
6
>>> for i in list(range(2,8,2):
	      
SyntaxError: invalid syntax
>>> for i in list(range(2,8,2)):
	print(i)

	
2
4
6
>>> print("monica","priya",sep="_",end=".")
monica_priya.
>>> print("monica","priya",sep="_",end="."),print("me")
monica_priya.me
(None, None)
>>> list
<class 'list'>
>>> list=[1,2,3,4,5]
>>> for i in list:
	print(i,end="#")

	
1#2#3#4#5#
>>> ##while loop##
>>> while(len(list)>0):
	print(list)
	del list[-1]

	
[1, 2, 3, 4, 5]
[1, 2, 3, 4]
[1, 2, 3]
[1, 2]
[1]
>>> n=0
>>> add=0
>>> while(n<=5):
	add+=n
	n+=1

	
>>> print(n),print(add)
6
15
(None, None)
>>> ##dictionary##
>>> s=dict()
>>> s[1]=10
>>> s[10]=8
>>> print(s)
{1: 10, 10: 8}
>>> print(s[10])
8
>>> dic={"jan":1,"feb":2}
>>> print(dic)
{'jan': 1, 'feb': 2}
>>> print(dic["jan"])
1
>>> dic["march"]=3
>>> dic
{'jan': 1, 'feb': 2, 'march': 3}
>>> del s[1]
>>> s
{10: 8}
>>> dic={'a':1,'b':2,'b':3,'c':2}
>>> dic
{'a': 1, 'b': 3, 'c': 2}
>>> len(dic)
3
>>> dic={'a':1,'b':2,'c':2}
>>> dic
{'a': 1, 'b': 2, 'c': 2}
>>> dic={'a':1,'b':2,'b':3}
>>> dic
{'a': 1, 'b': 3}
>>> #in a dictionary values can be duplicated but keys are unique,the value of a duplicated key is replaced with the new value
>>> len(dic)
2
>>> #syntax of get() method for dictionary....dicname.get(key,value)....value is Optional. It is a value to return if the specified key does not exist.
##Default value is None
>>> dic.get('a')
1
>>> dic.get('a',None)
1
>>> dic.get('c')
>>> dic.get('c',None)
>>> print(dic.get('c',None))
None
>>> print(dic.get('c',1))
1
>>> dic
{'a': 1, 'b': 3}
>>> print(dic.items())
dict_items([('a', 1), ('b', 3)])
>>> print(type(dic.items()))
<class 'dict_items'>
>>> print(list(dic.items()))
Traceback (most recent call last):
  File "<pyshell#211>", line 1, in <module>
    print(list(dic.items()))
TypeError: 'list' object is not callable
>>> 
====================================================================================== RESTART: Shell ======================================================================================
>>> print(list(dic.items()))
Traceback (most recent call last):
  File "<pyshell#213>", line 1, in <module>
    print(list(dic.items()))
NameError: name 'dic' is not defined
>>> dic={'a':1,'b':2,'b':3}
>>> print(list(dic.items()))
[('a', 1), ('b', 3)]
>>> print(type(list(dic.items())))
<class 'list'>
>>> print(dic.keys())
dict_keys(['a', 'b'])
>>> print(dic.values())
dict_values([1, 3])
>>> print(list(dic.keys()))
['a', 'b']
>>> print(list(dic.values()))
[1, 3]
>>> print(type(dic.keys())),print(type(dic.values()))
<class 'dict_keys'>
<class 'dict_values'>
(None, None)
>>> print(type(list(dic.keys()))),print(type(list(dic.values())))
<class 'list'>
<class 'list'>
(None, None)
>>> list=[1,2]
>>> print(list)
[1, 2]
>>> listtodic=dict.fromkeys(list,1)
>>> print(listtodic)
{1: 1, 2: 1}
>>> listtodic={i:'a' for i in list}
>>> print(listtodic)
{1: 'a', 2: 'a'}
>>> list1=['a','b']
>>> listtodic=dict(zip(list,list1))
>>> listtodic
{1: 'a', 2: 'b'}
>>> ##tuples##
>>> tuple1=(1,2,3,'abc')
>>> print(tuple1)
(1, 2, 3, 'abc')
>>> print(tuple1[::1])
(1, 2, 3, 'abc')
>>> print(tuple1[1::2])
(2, 'abc')
>>> print(tuple1[::-1])
('abc', 3, 2, 1)
>>> tuple[1]='a'
Traceback (most recent call last):
  File "<pyshell#240>", line 1, in <module>
    tuple[1]='a'
TypeError: 'type' object does not support item assignment
>>> #lists are mutable objects whereas tuples are immutable