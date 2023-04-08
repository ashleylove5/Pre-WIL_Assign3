#TASK 1

s = 'fullstackslp'

# 1. 'f'
print(s[0])

# 2. 'p'
print(s[-1])

# 3. 'stack'
print(s[4:9])

# 4. 'slp'
print(s[-3:])

# 5. 'csk'
print(s[2] + s[5] + s[9])

# reverse string
print(s[::-1])

#TASK 2

d1= {'simple_key':'hello'}
d2= {'k1':{'k2':'hello'}}
d3={'k1':[{'nest_key':['this is deep',['hello']]}]}

# Grab 'hello' from d1
hello_d1 = d1['simple_key']
print(hello_d1)  # Output: hello

# Grab 'hello' from d2
hello_d2 = d2['k1']['k2']
print(hello_d2)  # Output: hello

# Grab 'hello' from d3
hello_d3 = d3['k1'][0]['nest_key'][1]
print(hello_d3)  # Output: hello

#TASK 3

mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]

unique_values = set(mylist)

print(unique_values)

#TASK 4
age = 45
name = "Kyle"
dog_name = "Spot"

# Using f-string formatting
print(f"Hello my dog's name is {name} and he looks {age} years old")