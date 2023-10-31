# Scoping in Python allows for greater control of elements in your code.
# This reduces the chances of accidental or unwanted changes

# The 4 scopes are:
# 1. Local Scope
# 2. Enclosing Scope
# 3. Global Scope
# 4. Built-in Scope

# Variables within the built-in and global scope are accessible from anywhere in the code.

# Global Scope is generally discouraged in applications as it increases the possibility of mistakes in outputs

# Global Scope
my_global = 10

def fn1():
    enclosed_variable = 8
    def enclosing_scope():
        local_variable = 5
        print(f"Access to Global: {my_global}") # Global scope is accessible from anywhere
        print(f"Access to Enclosed Scope: {enclosed_variable}")
    enclosing_scope()
    
    
fn1()
# print(f"Cannot access local {local_variable}")
# Only available from within the local scope of the function fn1()
