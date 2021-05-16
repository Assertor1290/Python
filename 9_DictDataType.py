# 1. DICTIONARY INTRODUCTION

# As of Python version 3.7, dictionaries are ordered.
# In Python 3.6 and earlier, dictionaries are unordered.
thisdict = {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
print(thisdict)

# Dictionary are indexable using key value
print(thisdict['brand'])

# Dictionary is changeable
thisdict['year'] = 1965
print(thisdict)

# Dictionary doesn't allow duplicate keys, allows duplicate values
# No error is raised, the last key value is assigned
dup_dict = {'a': 1, 'b': 2, 'c': 3, 'a': 4}
print(dup_dict)

dup_dict = {'a': 4, 'b': 2, 'c': 3, 'a': 4}
print(dup_dict)

dup_dict = {'a': 4, 'b': 2, 'c': 3, 'd': 4}
print(dup_dict)

# 2. ACCESS ITEMS
# method 1: using key as index
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["model"])

# using get() method
print(thisdict.get('brand'))

# get list of keys
keys = thisdict.keys()
print(keys)

# get list of values
values = thisdict.values()
print(values)

# get items: will return each item in a dictionary, as tuples in a list.
item = thisdict.items()
print(item)

# check if key exists
if 'brand' in thisdict:
    print("Brand")

# 3. CHANGE ITEMS
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1963}
thisdict["year"] = 2018
print(thisdict)

# update
thisdict.update({'year':1963})
print(thisdict)

# 4. ADD ITEMS
# using new key
thisdict['color'] = 'Red'
print(thisdict)

# using update method
# if value doesn't exist, it adds it
thisdict['speed'] = 45
print(thisdict)

# 5. REMOVE ITEMS
# removes item with specified key
thisdict.pop('speed')
print(thisdict)

# removes last item (from 3.7)
# before that random element is removed
thisdict.popitem()
print(thisdict)

del thisdict['model']
print(thisdict)

# deletes all items from list
thisdict.clear()
print(thisdict)

# deletes the dictionary itself
del thisdict
# print(thisdict) # NameError: name 'thisdict' is not defined

# 6. LOOP THROUGH ITEMS
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1963}
# print keys
for x in thisdict:
    print(x)

for x in thisdict.keys():
  print(x)

# print values
for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
  print(x)

for x, y in thisdict.items():
  print(x, y)

# 6. COPY DICTIONARY
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
# m1: using copy method
mydict = thisdict.copy()
print(mydict)

# using dict()
mydict2 = dict(thisdict)
print(mydict2)

# 7. NESTED DICTIONARY
shape = {
  'figure1' : {
    "name" : "square",
    "color" : 'red'
  },
  'figure2' : {
    "name" : "circle",
    "color" : 'blue'
  },
  'figure3' : {
    "name" : "triangle",
    "color" : 'green'
  }
}
print(shape)

# OR
figure1 = {
    "name": "square",
    "color": 'red'
}
figure2 = {
    "name": "circle",
    "color": 'blue'
}
figure3 = {
    "name": "triangle",
    "color": 'green'
}
shape2 = {
    'figure1' : figure1,
    'figure2' : figure2,
    'figure3' : figure3
}
print(shape2)