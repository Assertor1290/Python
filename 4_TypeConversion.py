# Type Conversion: convert one type to another

# 1. Implicit Type Conversion: Automatic
# Converts lower type to higher type to avoid data loss
int_num = 3
float_num = 3.5

new_num = int_num + float_num
print('{} : {}'.format(type(new_num),new_num))

complex_num = 3 + 5j
new_num = int_num + complex_num
print('{} : {}'.format(type(new_num),new_num))

# str = 'Hello'
# print(str + int_num) :Can only concatenate str to str

# 2. Explicit Type Conversion/Type Casting
# User does this conversion
num_int = 123
num_str = "456"

num_str = int(num_str)
print("Data type of num_str after Type Casting:",type(num_str))

num_sum = num_int + num_str
print('{} : {}'.format(type(num_sum),num_sum))

numb_int = 5
numb_int = str(numb_int)
print("Data type of num_int after Type Casting:",type(numb_int))
