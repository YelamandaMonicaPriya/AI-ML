>>> for i in range(10):
    print(i)

0
1
2
3
4
5
6
7
8
9
>>> print("hello monu")
hello monu
>>> print('hi')
hi
>>> a=-10
>>> b=10
>>> a+b
0
>>> a=20
>>> b=10
>>> print(a+b)
30
>>> print('a+b')
a+b
>>> a-b
10
>>> a/b
2.0
>>> a//b
2
>>> a**b
10240000000000
>>> a=5
>>> b=6.4
>>> print(a+b)
11.4
>>> for i in range(5):
	print(i)

0
1
2
3
4
>>> for i in range(12,1,-1):
	print(i)

	
12
11
10
9
8
7
6
5
4
3
2
>>> #range is 12 including and 1 excluding
>>> print("closer song")
closer song
>>> print(type("hey"))
<class 'str'>
>>> hey=10
>>> print(type(hey))
<class 'int'>
>>> print(3%2)
1
>>> print(3%2),print(3+2)
1
5
(None, None)
>>> list=[1,2,3,4,5]
>>> print(list)
[1, 2, 3, 4, 5]
>>> print(type(list))
<class 'list'>
>>> list
[1, 2, 3, 4, 5]
>>> list[-1]
5
>>> list[1]
2
>>> list[0]
1
>>> list[4]
5
>>> list1=['abc',10,20]
>>> list1
['abc', 10, 20]
>>> list[3]=list1
>>> print(list)
[1, 2, 3, ['abc', 10, 20], 5]
>>> for i in range(len(list)):
	print(list[i])
	print(type(list[i]))

	
1
<class 'int'>
2
<class 'int'>
3
<class 'int'>
['abc', 10, 20]
<class 'list'>
5
<class 'int'>
>>> print(type(3.5))
<class 'float'>
>>> print(type('abc'))
<class 'str'>
>>> a=str
>>> print(type(a))
<class 'type'>
>>> print(a)
<class 'str'>
>>> a='str1'
>>> b='str2'
>>> print(a+b)
str1str2
>>> print(a+" "+b)
str1 str2
>>> list
[1, 2, 3, ['abc', 10, 20], 5]
>>> list.append(2.0)
>>> list
[1, 2, 3, ['abc', 10, 20], 5, 2.0]
>>> len(list)
6
>>> list.append('hello')
>>> list
[1, 2, 3, ['abc', 10, 20], 5, 2.0, 'hello']
>>> len(list)
7
>>> list2=[0,1,2,3,4,5,6,7,8,9,10]
>>> len(list2)
11
>>> list[0:11:1]
[1, 2, 3, ['abc', 10, 20], 5, 2.0, 'hello']
>>> list2[0:11:1]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list2[0:10:1]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list2[0:11:2]
[0, 2, 4, 6, 8, 10]
>>> list2[1:11:2]
[1, 3, 5, 7, 9]
>>> list2[::2]
[0, 2, 4, 6, 8, 10]
>>> list2[:5:1]
[0, 1, 2, 3, 4]
>>> list2[0:11]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list2[4::5]
[4, 9]
>>> list2[4:5:5]
[4]
>>> list2[5:6]
[5]
>>> list2[-11]
0
>>> list2[-11:5:3]
[0, 3]
>>> list2[-4::2]
[7, 9]
>>> list2[4:11:1]
[4, 5, 6, 7, 8, 9, 10]
>>> list2[:-2:3]
[0, 3, 6]
>>> list2[0:-2]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> list2[-2]
9
>>> #list[a:b:r] both a and b included...list[a:-b:r] a included , -b excluded
>>> list2
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list2.append(11)
>>> list2
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
>>> list2.insert(3,'a')
>>> list2
[0, 1, 2, 'a', 3, 4, 5, 6, 7, 8, 9, 10, 11]
>>> for i in range(len(list2)):
	if(list2[i]=='a'):
		list2[i]='b'

>>> print(list2)
[0, 1, 2, 'b', 3, 4, 5, 6, 7, 8, 9, 10, 11]
>>> list2[3]=20
>>> list2
[0, 1, 2, 20, 3, 4, 5, 6, 7, 8, 9, 10, 11]
>>> list2.sort()
>>> list2
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 20]
>>> list2.sort(reverse=True)
>>> list2
[20, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> 