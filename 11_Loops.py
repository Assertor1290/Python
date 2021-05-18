# 1. While loops
i = 1
while i < 6:
    print(i, end=' ')
    i += 1
print('\n')

i = 1
while i < 6:
    print(i, end=' ')
    if i == 3:
        break
    i += 1
print('\n')

# 2. For Loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x, end=' ')
print('\n')

for x in "banana":
    print(x, end=' ')
print('\n')

# else  in for loop
for x in range(6):
    print(x, end=' ')
else:
    print("Finally finished!")
