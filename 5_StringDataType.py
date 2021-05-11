# 1. String Declaration
single_quote = ' String in "single" quote '
double_quote = " String in 'double' quotes "
triple_quote = ''' String in triple single quotes '''
triple_quote_2 = """ String in triple double quotes """
func_quote = str('String using function')

# 2. Looping through string
for x in 'Hello World':
    print(x, end=' ')  # Print without newline

# 3. String length
print('\n{}'.format(len("Hello")))

# 4. Check if phrase or character in string: in keyword
text = "Learing Python data types in Python"
print("data" in text)
print("Check" in text)
if "Python" in text:
    print("Python word is present")

# 5. Check if phrase or character is not in string: not in keyword
if "Java" not in text:
    print("Java is not present in text")

# 6. Slicing
print(text[8:14])  # first character has index 0
print(text[:7])  # slice from start
print(text[15:])  # slice to end
print(text[-6:-1])  # prints 'Pytho' as slicing is exclusive

# 7. Upper case
print('Hello World'.upper())

# 8. Lower case
print('Hello World'.lower())

# 9. Remove whitespace
print(' Hello '.strip())

# 10. Replace string or character
print('Hello'.replace('H', 'J'))
print('Hello'.replace('H', ' '))
print('Hello'.replace('He', 'Jo'))

# 11. Split string: Returns a list
print("Hello World in Python".split(' '))
print("Hello World in Python".split(','))
print("Hello World, in Python".split(','))

# 12. String concatenation
print("Hello" + ' ' + "World")

# 13. String format
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# 14. Capitalize: only first character of string is Capital
text = "this Is capitalize Function"
print(text.capitalize())

# 15. Count method
text = 'abcdef abcdef abcdef abcdef'
print(text.count('a'))
print(text.count(' '))
print(text.count('abc'))
print(text.count('ae'))
print(text.count('a', 3, 15))  # exclusive

# 16. endswith() method
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

# 17. find() method: Returns -1 if value not found
# returns first occurrence
x = txt.find("welcome")
print(x)
print(txt.find("globe"))
print(txt.find("m", 6, 14))  # find in range [start,end]

# 18. index() method: Throws exception if value not found
# rindex(): returns index of last occurrence
x = txt.index("welcome")
print(x)
# print(txt.index("globe")) # ValueError: substring not found

# 19. isalnum() method: True if all characters are alnum
# (letter/number)
print('Hello456'.isalnum())
print('Hello4%6'.isalnum())
print('Hello 456'.isalnum())

# 20. isalpha(): True if all characters are alphabets
print('Hello'.isalpha())
print('Hello456'.isalpha())
print('Hello World'.isalpha())
print('\n')

# By definition, isdecimal() ⊆ isdigit() ⊆ isnumeric().
# That is, if a string is decimal, then it'll also be digit and numeric.

# 21. isdecimal()
# The superscript, subscript, fractions, and roman
# numerals are not considered as decimal characters.
# Hence, returns False.
print('\nisDecimal()  Function')
my_string = ''  # Space
print('" " : {}'.format(my_string.isdecimal()))     # False

my_string = '123abc'  # Alnum
print('123abc : {}'.format(my_string.isdecimal()))  # False

my_string = '123'  # Number
print('123 : {}'.format(my_string.isdecimal()))     # True

my_string = '\u00BD'  # Fraction (1/2)
print('\u00BD : {}'.format(my_string.isdecimal()))  # False

my_string = '\u2168'  # Roman numeral (IX)
print('\u2168 : {}'.format(my_string.isdecimal()))  # False

my_string = '\u2077'  # Superscript
print('\u2077 : {}'.format(my_string.isdecimal()))  # False

my_string = '\u2087'  # Subscript
print('\u2087 : {}'.format(my_string.isdecimal()))  # False
print('\n')

# 22. isdigit()
# Roman numerals, fractions are not considered as digits.
# The subscript, superscript and decimal characters
# are considered to be digits.
print('\nisDigit()  Function')
my_string = ''  # Space
print('" " : {}'.format(my_string.isdigit()))     # False

my_string = '123abc'  # Alnum
print('123abc : {}'.format(my_string.isdigit()))  # False

my_string = '123'  # Number
print('123 : {}'.format(my_string.isdigit()))     # True

my_string = '\u00BD'  # Fraction (1/2)
print('\u00BD : {}'.format(my_string.isdigit()))  # False

my_string = '\u2168'  # Roman numeral (IX)
print('\u2168 : {}'.format(my_string.isdigit()))  # False

my_string = '\u2077'  # Superscript
print('\u2077 : {}'.format(my_string.isdigit()))  # True

my_string = '\u2087'  # Subscript
print('\u2087 : {}'.format(my_string.isdigit()))  # True
print('\n')

# 23. isnumeric():
# The integers, subscript, superscript, fractions,
# and roman numerals in Unicode are considered to be numerics.
# Hence, returns True.

print('\nisnumeric()  Function')
my_string = ''  # Space
print('" " : {}'.format(my_string.isnumeric()))     # False

my_string = '123abc'  # Alnum
print('123abc : {}'.format(my_string.isnumeric()))  # False

my_string = '123'  # Number
print('123 : {}'.format(my_string.isnumeric()))     # True

my_string = '\u00BD'  # Fraction (1/2)
print('\u00BD : {}'.format(my_string.isnumeric()))  # True

my_string = '\u2168'  # Roman numeral (IX)
print('\u2168 : {}'.format(my_string.isnumeric()))  # True

my_string = '\u2077'  # Superscript
print('\u2077 : {}'.format(my_string.isnumeric()))  # True

my_string = '\u2087'  # Subscript
print('\u2087 : {}'.format(my_string.isnumeric()))  # True
print('\n')

# 24. islower()
txt = "hello world!"
print(txt.islower())

# 25. isupper()
txt = "HELLO WORLD!"
print(txt.isupper())

# 26. istitle(): returns True if all words in a text start
# with a upper case letter, AND the rest of the word are
# lower case letters, otherwise False.
# Symbols and numbers are ignored.
txt = "Hello, And Welcome To My World!"
print(txt.istitle())

# 27. join(): returns a string by joining all the
# elements of an iterable, separated by a string separator.
# Syntax: string.join(iterable)

# .join() with lists
numList = ['1', '2', '3', '4']
print(','.join(numList))

# .join() with tuples
numTuple = ('abc', 'def', 'ghi', 'jkl')
print('#'.join(numTuple))

# .join() with strings
s1 = 'abc'
s2 = '123'

# each element of s2 is separated by s1
print('s1.join(s2):', s1.join(s2))

# each element of s1 is separated by s2
print('s2.join(s1):', s2.join(s1))

# .join() with sets
# A set is an unordered collection of items,
# so you may get different output (order is random).
test = {'Python', 'Java', 'Ruby'}
s = '->->'
print(s.join(test))

# .join() with dictionaries. The join() method tries
# to join the keys (not values) of the dictionary
# with the string separator.
test = {'a': 1, 'b': 2}

# joins the keys only
print('@'.join(test))

# test = {1: 'mat', 2: 'that'}
# s = ', '
# this gives Type error since key isn't string
# print(s.join(test))

# 28. swapcase()
txt = "Hello My Name Is KUSH"
x = txt.swapcase()
print(x)