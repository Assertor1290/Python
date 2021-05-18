# 1. If...elif...else
# a = input()
# print(type(a))  # class<'str'>

# Case 1: if..else
a = int(input())  # print(type(a))  # class<'int'>
b = int(input())
if a > b:
    print('a is greater')
else:
    print('b is greater')

# Case 2: if..elif
c = int(input())
d = int(input())
if c > d:
    print('c is greater')
elif c == d:
    print('c is equal to d')

# Case 3: if..elif..else
e = int(input())
f = int(input())
if e > f:
    print('e is greater than f')
elif e == f:
    print('e is equal to f')
else:
    print('e is less than f')

# 2. Short Hand if
if a > b: print('a is greater than b')

# 3. Short hand if..else
# [on_true] if [expression] else [on_false]
print('A') if a > b else print('B')
# This technique is known as Ternary Operators,
# or Conditional Expressions.

# Can have multiple else statement on same line
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# 4. And, or in if condition
a = 200
b = 33
c = 500
# if b < a < c:
#  print("Both conditions are True")
if a > b and c > a:
    print("Both conditions are True")
if a > b or a > c:
    print("At least one of the conditions is True")

# 5.Nested if
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# 6. pass statement
# the pass statement is a null statement.
# nothing happens when the pass is executed.
a = 33
b = 200

if b > a:
    pass