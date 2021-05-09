name = input('Enter your name: ')
print('Your name is '+name)

# Python 3 vs Python 2

# Brackets required in Python 3
print('Hello') # --Python 3
# print 'Hello'  --Python 2

# When divide two int values, get float value in Python 3
print(7/5) # = 1.4
print(6/3) # = 2.0
# print(7/5) = 1  --Python 2

# range() function used in Python 3
for i in range(1,5):
    print(i)
# for i in xrange(1,5):  --Python 2
#   print(i)

# Error handling requires 'as' keyword in Python 3
try:
    name_check
except NameError as err:
    print(err, 'Error Caused')

"""
try:                        Python 2
    name_check
except NameError as err:
    print(err, 'Error Caused')
"""

# Comments:
# Single line comments: #
# Multi line comments: """   """
