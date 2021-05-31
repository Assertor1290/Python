# Anonymous function: no name
# Can take any number of arguments, but only one expression
# lambda arguments : expression
# The expression is executed and result is returned.

square = lambda x: x * x
print(square(5))

# Lambda functions can take any number of arguments
sum = lambda x, y : x + y
print(sum(5,6))

# Immediately Invoked Function Expression (IIFE, pronounced “iffy”)
print((lambda x, y: x + y)(2, 3))

# Lambda with higher order functions

# 1. FILTER: Filter out elements from iterable
# according to condition
my_list = [2, 3, 4, 5, 6, 7, 8, 9]
# function to filter even numbers
new_list_filter = filter(lambda x: (x % 2 == 0), my_list)
# <filter object at 0x00000254DEDB94A8>
print(new_list_filter)
# class 'filter'
print(type(new_list_filter))
new_list = list(filter(lambda x: (x % 2 == 0), my_list))
print(new_list)

# 2. MAP: Applies function to all elements of iterables
my_list = [2, 3, 4, 5, 6, 7, 8, 9]
new_list = list(map(lambda x: x * x, my_list))
print(new_list)

my_list = [2,3,4,5,6,7,8]
new_list = list(map(lambda a: (a/3 != 2), my_list))
print(new_list)
