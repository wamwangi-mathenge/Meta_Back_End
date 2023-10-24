# Naming conventions of variables

# Camel Case eg. myName (commonly used in JS)
# Snake case eg. my_name

x = 5 # Declared a variable
print(x) # Print out the value of the variable.

# You can declare any type of variable in terms of value
x = "Hello"
print(x)

a = b = c = 10
print(a)
print(b)
print(c)

x,y,z = 1,2,3
print(x)
print(y)
print(z)

# Variables are subject to change.
i = 10
print(i)

i = 5
print(i) # The value of the variable will change to 5 because it was re-assigned

# Deleting a variable
del i
print(i) # Shows undefined because the variable was deleted