# Created using def keyword
def my_func():
    print('Hello World!')


my_func()


# Parameter vs argument
# parameter inside function definition
def hello_name(name, age):
    print('Hello ' + name + '. My age is {}'.format(age))


# argument inside function call statement
hello_name('Kush', 24)


# Arbitrary number of arguments
# *args, This way function will receive a tuple of arguments
def arb_func(*bgroup):
    print('The blood group is ' + bgroup[1])


arb_func('A', 'B', 'O')


# Order of arguments
# Keyword arguments with key = value
def order_func(child3, child2, child1):
    print('The youngest child is ' + child3)
    print('The second child is ' + child2)
    print('The eldest child is ' + child1)


order_func(child1="Emil", child2="Tobias", child3="Linus")


# Arbitrary Keyword argument, **kwargs
def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")


# Default parameter value
def def_myfunc(country='India'):
    print('Country: ' + country)


def_myfunc()


# Passing list as argument
def list_funct(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]
list_funct(fruits)


# Return value
def ret_func(x):
    return x * x


square = ret_func(5)
print(square)


# Recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(5))

