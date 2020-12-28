"""
lecture about list and set
"""

my_list = [1,2,3,4,5]

print(my_list)

my_nested_list = [1,2,3,my_list]

print(my_nested_list)

my_list[0]=6

print(my_list)
my_list.append(7)
print(my_list)
my_list.remove(7)
print(my_list)

my_list.sort()

print((my_list))

my_list.reverse()
print(my_list)

print(my_list+[8,9])
my_list.extend(['a','b'])
print(my_list)

print('c' in my_list)

print(len(my_list))

# print(my_list[:])

# x,y=['a','b']
# print(y)

print('hello world'[-1])

my_letters= ['a','a','b','b','c' ]
print(my_letters)


my_unique_letters = set(my_letters)
print(my_unique_letters)
print(len(my_unique_letters))
print('a' in my_unique_letters)
print(list(my_unique_letters)[0])