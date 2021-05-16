# 1. SET INTRODUCTION

# set is unordered: each time different output
set1 = {'a', 'b', 'c', 'd', 'e'}
print(set1)

# set is unindexed
# print(set[1]) # TypeError: 'type' object is not subscriptable

# set is unchangeable
# Cannot change items, but can add or remove items
# Every set element is immutable (cannot be changed).
# However, a set itself is mutable.

# set doesn't allow duplicate values
# Duplicate values will be ignored
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# 2. ACCESS ITEMS
# Can't index, hence use loop
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

# 3. ADD ITEMS
thisset.add('grapes')
print(thisset)

# add items from one set to another
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# update method can add items from any iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# 4. REMOVE ITEMS
# 1. remove() method
thisset = {"apple", "banana", "cherry"}
thisset.remove('apple')
print(thisset)

# if item doesn't exist, raises error
# thisset.remove('apple') KeyError: 'apple'

# 2. discard() method
thisset = {"apple", "banana", "cherry"}
thisset.discard('apple')
print(thisset)

# If item doesn't exist, doesn't raise an error
thisset.discard('apple')
print(thisset)

# 3. pop() method: removes last item, but set is unordered,
# so random element is removed
thisset = {"apple", "banana", "cherry"}
thisset.pop()
print(thisset)

# 4. clear()
thisset.clear()
print(thisset)

# 5. del
del thisset
# print(thisset) NameError: name 'thisset' is not defined

# 5. JOIN SETS
set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}
# set3 = set1 + set2 TypeError: unsupported operand type(s) for +: 'set' and 'set'
# print(set3)

# union() method
set3 = set2.union(set1)
print(set3)

# update() method
set1.update(set2)
print(set1)
# Note: Both union() and update() will exclude any duplicate items.

# Keep similar items from both sets
# intersection_update() doesn't return any value
x = {"apple", "banana", "cherry", "guava"}
y = {"google", "guava", "microsoft", "apple"}
x.intersection_update(y)
print(x)

# Keep similar items from both sets
# intersection() returns a new set
x = {"apple", "banana", "cherry", "guava"}
y = {"google", "guava", "microsoft", "apple"}
z = x.intersection(y)
print(z)

# keep different items only
x = {"apple", "banana", "cherry", "guava"}
y = {"google", "guava", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

# keep different items only, returns new set
x = {"apple", "banana", "cherry", "guava"}
y = {"google", "guava", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

# 6. COPY SETS
set1 = {'a', 1, 'b', 2, 'c', 3}
set2 = set1.copy()
print(set2)

# 7. CHECK IF SETS ARE DISJOINT
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
# returns True if none of the items are present
# in both sets, otherwise it returns False.
z = x.isdisjoint(y)
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.isdisjoint(y)
print(z)

# NOTE : Empty curly braces create a dictionary, not set
# eg: x = {} i
x = set()
y = set()
z = x.isdisjoint(y)
print(z)

# 7. CHECK SUBSET
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

# empty set is subset of every set
x = set()
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

# 8. CHECK SUPERSET
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)


