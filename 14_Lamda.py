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

