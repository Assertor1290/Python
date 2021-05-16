# 1. LIST INTRODUCTION
# List items are ordered
hello_list = ['apple', 'banana', 'mango']
print(hello_list)

# List items are indexed
print(hello_list[1])

# List items are changeable
hello_list[1] = 'guava'
print(hello_list)

# List allows duplicate values
dup_list = ['apple', 'banana', 'mango', 'apple']
print(dup_list)

# Length of list
print(len(dup_list))

# List can contain different data types
mixed_list = [1, 'a', 2, 'abc', True]
print(mixed_list)

# List creation using list keyword
list_meth = list((1,2,3,4))
print(list_meth)

# 2. ACCESS LIST ITEMS
# Negative indexing
hello_list = ['apple', 'banana', 'mango', 'guava']
print(hello_list[-1])

# range of index
print(hello_list[1:3])

# Check if item exists
if 'apple' in hello_list:
    print('yes')

# 3. CHANGE LIST ITEMS
# Change multiple items
change_list = ['apple', 'banana', 'mango', 'guava', 'strawberry']
change_list[1:3] = ['orange', 'grapes']  # 3 is exclusive
print(change_list)

# If you insert more items than you replace,
# the new items will be inserted where you specified,
# and the remaining items will move accordingly
change_list = ['apple', 'banana', 'mango', 'guava', 'strawberry']
change_list[1:2] = ['orange', 'grapes']  # adding two items at one location
print(change_list)

# If you insert less items than you replace,
# the new items will be inserted where you specified,
# and the remaining items will move accordingly
this_list = ["apple", "banana", "cherry"]
this_list[1:3] = ["watermelon"]
print(this_list)

# 4. ADD LIST ITEMS
add_list = ['a', 'b', 'c']
# Append adds element to end of list
add_list.append('d')
print(add_list)

# Insert items at specific position
this_list.insert(2, 'orange')
print(this_list)
# inserting at -1 adds to second last position
this_list.insert(-1, 'papaya')
print(this_list)
# to add element to last position
this_list.insert(len(this_list), 'last')
print(this_list)

# Extend list
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

# can extend using any other iterable object
dict_item = {'key1' : 'value1', 'key2': 'value2'}
list2.extend(dict_item)
print(list2)

# 5. REMOVE LIST ITEMS
remove_list = ['a', 'b' , 1, 'c', 'd', 'e', 2]
# remove method removes specified item
remove_list.remove(1)
remove_list.remove('c')
print(remove_list)

# pop method used to remove from specified index
remove_list.pop(0)
print(remove_list)

# If no index is specified pop() method removes last item
remove_list.pop()
print(remove_list)

# del method also deletes item from specific index
del remove_list[1]
print(remove_list)

# del is also used to delete entire list
del remove_list
# print(remove_list) # NameError: name 'remove_list' is not defined

# clear method empties the list, but not deletes it
new_list = ['a', 'b']
new_list.clear()
print(new_list)

# 6. LOOP THROUGH LIST
loop_list = ['a', 'b', 'c', 'd', 'e']
# Here, we are looping through list items, not indexes
for i in loop_list:
    print(i, end=' ')

print('\n')
# To loop through indexes
for i in range(len(loop_list)):
    print(loop_list[i])

# 7. LIST COMPREHENSION
# newlist = [expression for item in iterable if condition == True]

# Example:
# Based on a list of fruits, you want a new list,
# containing only the fruits with the letter "a" in the name.

# Without list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for i in fruits:
    if 'a' in i:
        newlist.append(i)
print(newlist)

# With list comprehension
new_list = [x for x in fruits if 'a' in x]
print(new_list)
# condition is optional
new_list = [x for x in fruits]
print(new_list)
# iterable can be list, tuple, set etc
newlist = [x for x in range(10) if x < 5]
print(newlist)
newlist = [x.upper() for x in fruits]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

# 8. SORT LIST
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist.sort(reverse=True)
print(thislist)

# 9. COPY LIST
ori_list = ['a', 'b', 'c']
copy_list = ori_list.copy()
print(copy_list)

copy_list_2 = list(ori_list)
print(copy_list_2)

# 10. JOIN LIST
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

# method 1
list3 = list1 + list2
print(list3)
# method 2
# for x in list2:
#  list1.append(x)

# method 3
# list1.extend(list2)

