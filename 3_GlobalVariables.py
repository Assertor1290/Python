# Create variable outside of function, and use
# it inside a function
x = "Kush"


def myfunc():
    print('Hello ' + x)


myfunc()

# Local variable with same name as global variable
y = 'awesome'


def myfunc2():
    y = 'fantastic'
    print('Python is ' + y)


myfunc2()
print('Python is ' + y)


# global keyword

def myfunc3():
    global z
    z = 'brilliant'


myfunc3()
print('Python is ' + z)
