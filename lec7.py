'''
lec 7 while loop
'''

i = 5
while i >=0:
    
    try:
        print(1/(i-3))
    except:
        continue
    i = i -1

    
# try:
#     print(1/0)
# except ZeroDivisionError:
#     print('zero division error')

# except:
#     print('other errors')
