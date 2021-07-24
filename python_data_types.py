'''s = "Hello World"
print(s[2:4])

print(type(s))
list1 = [1,2,3,4,5,5,5,5,5,5,5,6,6,6,7,7,7]

myset = set(list1)
print(myset)
print(set('Mississippi'))
count = [1,2,3,4]

while count:
	print(count)
	count.pop()'''


#With open(filename) as placeholder:
	#read write here
	#no need to "close the file again"

print('My name is {y} {x} {x} {x}'.format(x = "Mahesh", y = "Chadalavada"))

mylist = [(1,2), (3,4), (5,6)]
#Tuple unpacking
for a,b in mylist:
	print(a)

'''list1 = [1,2,3,4,5,6,7,8,9,10]
for num in list1:
	if num % 2 == 0:
		pass
	else:
		print(num)
		
'''
mynums = [1,2,3,4,5,5,6,6,7]

mylist2 = [_ if _%2 == 0 else _**2 for _ in mynums ]
print(mylist2)