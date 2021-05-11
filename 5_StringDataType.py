# 1. String Declaration
single_quote = ' String in "single" quote '
double_quote = " String in 'double' quotes "
triple_quote = ''' String in triple single quotes '''
triple_quote_2 = """ String in triple double quotes """
func_quote = str('String using function')

# 2. Looping through string
for x in 'Hello World':
    print(x, end=' ')   # Print without newline


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
print(text[:7])    # slice from start
print(text[15:])   # slice to end
print(text[-6:-1]) # prints 'Pytho' as slicing is exclusive

# 7. Upper case
print('Hello World'.upper())

# 8. Lower case
print('Hello World'.lower())

# 9. Remove whitespace
print(' Hello '.strip())

# 10. Replace string or character
print('Hello'.replace('H','J'))
print('Hello'.replace('H',' '))
print('Hello'.replace('He','Jo'))

# 11. Split string: Returns a list
print("Hello World in Python".split(' '))
print("Hello World in Python".split(','))
print("Hello World, in Python".split(','))

# 12. String concatenation
print("Hello" +' '+ "World")

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
print(text.count('a',3,15))  # exclusive

# 16. endswith() method
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

# 17. find() method: Returns -1 if value not found
# returns first occurence
x = txt.find("welcome")
print(x)
print(txt.find("globe"))
print(txt.find("m",6,14)) # find in range [start,end]

# 18. index() method: Throws exception if value not found
x = txt.index("welcome")
print(x)
# print(txt.index("globe")) # ValueError: substring not found

# 19. isalnum() method



