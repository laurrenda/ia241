'''
lec 6 for loop and range function
'''

# demo_str = 'this is my string'

# for word_item in demo_str.split():
#     print(word_item)

# for i in range(1,5):
#     print(i)

num_list= [213,321,123,312]

max_item = num_list[0]

for num in num_list:
    if max_item <= num:
        max_item = num
        
print(max_item)

