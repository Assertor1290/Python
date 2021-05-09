# 1. abs()
x = abs(-1)
print(x)
y = abs(1)
print(y)

print('\n')
# 2. bin()
b = bin(3)
print(b)

print('\n')
# 3. bool()
val = bool(1)
print(val)
val = bool(-3)
print(val)
val = bool(0)
print(val)

print('\n')
# 4. complex()
comp = complex(1, 3)
print(comp)
comp = complex(-1, 0)
print(comp)
comp = complex(0, 0)
print(comp)

print('\n')
# 5. dict()
dictionary = {"color": "red", "shape": "circle"}
print(dictionary)

print('\n')
# 6. float()
print(float(1))
print(float(-4.5))
print(float('3'))
print(float('Infinity'))
print(float('-inf'))
print(float('nan'))
print(float(1e-003))

print('\n')
# 7. set(): Distinct elements
mylist = [1, 2, 3, 4]
mylist2 = ['Orange', 'Red', 'Blue']

integer_set = set(mylist)
print(integer_set)
# integer_set[1] = 9
# 'set' object doesn't support item assignment

string_set = set(mylist2)
print(string_set)
# string_set[2] = 'Green'

# set removes duplicate elements
duplicate_set = set([1, 2, 3, 1])
print(duplicate_set)

# set is mutable
integer_set.add(6)
print(integer_set)
integer_set.remove(2)
print(integer_set)

print('\n')
# 8. frozenset()
int_set = frozenset([1, 2, 3])
print(int_set)
# int_set[1] = 3   Doesn't support item assignment
# frozenset has no add or remove, as it is immutable

print('\n')
# 9. round()
r_value = round(5.5)
print(r_value)

print('\n')
# 10. min()
minimum = min({1, 8, 9})
print(minimum)
minimum = min(1, 8, 9)
print(minimum)
minimum = min('a', 'c', 'z')
print(minimum)

print('\n')
# 10. max()
maximum = max({1, 8, 9})
print(maximum)
maximum = max(1, 8, 9)
print(maximum)
maximum = max('a', 'c', 'z')
print(maximum)

print('\n')
# 11. sorted()
test_list = [9, 4, 2, 8, 1]
sorted_list = sorted(test_list)
print(sorted_list)
sorted_list = sorted(test_list, reverse=True)
print(sorted_list)


def func(x):
    return x % 7


sorted_list = sorted(test_list, key=func)
print(sorted_list)

print('\n')
# 12. sum()
a = [2, 5, 4.3]
print(sum(a))
b = [4/3, 1/3, 1/3]
print(sum(b))

print('\n')
# 13. len()
print(len('Hello0!'))
print(len([1, 2, 6, 5]))
print(len((4, 5, 6, 7)))
print(len({"color": "red", "shape": "square"}))

print('\n')
# 14. type()
print(type([1, 2, 3]))
print(type((7, 8, 9)))
print(type({4, 7, 1}))
print(type('Hello'))
print(type(list((4, 8, 9))))
print(type(tuple((4, 8, 9))))
print(type(set(('a' ,'b', 'c'))))
print(type(frozenset(('h', 'i', 'k'))))

print('\n')
# 15. int()
print(int(34))
print(int(6.8))

print('\n')
# 16. str()
string_test = str("Hello")
print(string_test)

print('\n')
# 17. isinstance()
numbers = [1, 2, 3, 4, 5]
print(isinstance(numbers, list))           # True
print(isinstance(numbers, float))          # False
print(isinstance(numbers, (list, float)))  # True

print('\n')
# 18. map(): used to apply a function to each element of iterable
numbers = [1, 2, 3, 4, 5]
# add 1
print(list(map(lambda x: x + 1, numbers)))

# multiply by 2
print(list(map(lambda x: x * 2, numbers)))


# add 1 function - regular function
def add_one(element):
    return element + 1


print(list(map(add_one, numbers)))
numbers_1 = [1, 2, 3, 4, 5]
numbers_2 = [6, 7, 8, 9, 10]

# multiply the elements of both lists
print(list(map(lambda x, y: x * y, numbers_1, numbers_2)))
# [6, 14, 24, 36, 50]

print('\n')
# 19. id
numbers = [1, 2, 3, 4, 5]
# new list of numbers
new_numbers = numbers

# both list have the same id number
print('numbers id: {}, new_numbers id: {}'.format(id(numbers), id(new_numbers)))
# numbers id: 2021106827080, new_numbers id: 2021106827080

# we can also check that they refer to the same object with the identity operator is
print(numbers is new_numbers)  # True

print('\n')
# 20. hex()
hex_num = hex(6)
print(hex_num)
# hex_num = hex(6.0) accepts only integer arguments
print(hex(255))

print('\n')
# 21. format()
age = 23
txt = "I am {} years old"
print(txt.format(age))

# can take multiple arguments
quantity = 3
item_no = 200
price = 50
order = 'I want {} pieces of item {} for {} dollars'
print(order.format(quantity, item_no, price))

# specify index
order = 'I want to pay {2} dollars for {0} pieces of item {1}'
print(order.format(quantity, item_no, price))

# fixed-point notation rounded off to two decimal places
print(format(123.45789, '.2f'))

print('\n')
# 22. pow()
print(pow(4, 3))
print(pow(4, 3, 5))

print('\n')
# 23. slice()
slice_list = [0,1,2,3,4,5,6]
x = slice(2)
print(slice_list[x])

y = slice(2,4)
print(slice_list[y])

z = slice(0, 8, 2)
print(slice_list[z])

# 24. zip()
first = ('a', 'b', 'c')
second = (1, 2, 3)
c = zip(first, second)
print(c)
print(type(c))

e = list(c)
print(e)

# list of products
products = ['table', 'chair', 'sofa', 'bed', 'lamp']
# list of prices
prices = [50, 20, 200, 150, 10]

for product, price in zip(products, prices):
    print('Product: {}, Price: {}'.format(product, price))

