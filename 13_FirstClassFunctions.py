# Everything is an object in Python

# 1. Functions are objects
def shout(text):
    return text.upper()


print(shout('Hello'))
print(shout.__name__)
yell = shout
print(yell('Hello'))
print(yell.__name__)


# 2. Functions can be passed as arguments
def shout_2(text):
    return text.upper()


def whisper_2(text):
    return text.lower()


def greet(func):
    greeting = func('Hi, Created using function as an argument')
    print(greeting)


greet(shout_2)
greet(whisper_2)


# 3. Functions can return another function
# 4. Functions can be nested
def create_adder(x):
    def adder(y):
        return x + y
    return adder


add_sum = create_adder(15)
print(add_sum(10))


# 5. Functions can be stored in data structures
def yell(text):
    return text.upper() + '!'


# yell function, lower method, integer, string in list data structure
ds = [yell, str.lower, 1, 'a']
print(ds)