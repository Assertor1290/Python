# 1. TUPLE INTRODUCTION

# tuples are ordered
hello_tuple = ('apple', 'banana', 'guava')
print(hello_tuple)

# tuples are indexed
print(hello_tuple[1])

# tuples are unchangeable or immutable
# hello_tuple[1] = 'orange' :
# Error: Tuples don't support item assignment

# tuples allow duplicate values
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Length of tuple
print(len(thistuple))

# tuple creation using tuple keyword
key_tuple = tuple(("apple", "banana", "cherry", "apple", "cherry"))
print(key_tuple)

# 2. ACCESS TUPLE ITEMS
# Negative indexing
hello_tuple = ('apple', 'banana', 'mango', 'guava')
print(hello_tuple[-1])

# range of index
print(hello_tuple[1:3])

# Check if item exists
if 'apple' in hello_tuple:
    print('yes')

# 4. CHANGE TUPLE ITEMS
# Since tuple is immutable, have to adopt different method
# convert the tuple into a list, change the list,
# and convert the list back into a tuple.
x = ('apple', 'banana', 'mango')
y = list(x)
y[1] = 'grapes'
x = tuple(y)
print(x)

# Similar procedure to add items, remove items

# del deletes entire tuple
del x
# print(x)  NameError: name 'x' is not defined

# 5. UNPACK TUPLES: extract the values back into variables
fruits = ("apple", "banana", "cherry")
a, b, c = fruits
print(a)
print(b)
print(c)

# d, e = fruits # ValueError: too many values to unpack

# can add an * to the variable name and the values
# will be assigned to the variable as a list
e, *f = fruits
print(e)
print(type(e))
print(f)
print(type(f))

# If the asterix is added to another variable name than the last,
# Python will assign values to the variable until the number of
# values left matches the number of variables left.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

# 6. LOOP TUPLES
# loop using items
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# loop using index number
for i in range(len(thistuple)):
  print(thistuple[i])

# 7. JOIN TUPLES
# Method 1
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# NOTE:Can't use extend keyword as that would attempt
# to modify tuple, but tuple is immutable

# Multiply tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)