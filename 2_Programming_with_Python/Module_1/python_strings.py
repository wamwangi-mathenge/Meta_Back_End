# A string is a sequence of characters enclosed in single or double quotes.
# Python uses a type of encoding known as unicode

# Ways to declare strings
# 1. Single Line
varA = "Hello World"

# 2. Multi Line
my_variable = "This is \
to big to fit \
on a single line \
so we multi-lined it"

print(my_variable)

'This is too big to fit on a single line so you multi-lined it'


# Reassigning a String Value
# name variable is assigned with the value of John
name = "John"
print(name) # John

# name is reassigned the value of Paul
name = 'Paul'
print(name) # Paul


# Each character in a String can be accessed based on its index
name = "John"
print(name[0])
print(name[1])
print(name[-1])

# Checking the length of a string
print(len(name))

# Concatenating strings
first_name = "Brian"
second_name = "Mathenge"

print(first_name + second_name)
print(f"{first_name} {second_name}") # F-string concatenation - Takes care of the spaces in between and gets rid of + symbol