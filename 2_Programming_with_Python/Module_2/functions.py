# Functions are a set of instructions that take an inout and return an output
# A python function is a modular piece of code that can be re-used repeatedly

# Declaring a function
# A function is declared using the 'def' keyword followed by the NAME and TASK to complete
# Optional parameters can also be added after the function name within a pair of parentheses

# def <function name>(<params>):
#     <task to complete>

# Function Example: A function to determine the sum of 2 numbers
# def sum(x, y):
#     return x + y

# Calculate the tac amount for a customer

# bill = 175.00
# tax_rate = 15

# total_tax = (bill * tax_rate) / 100.00

# print(f"Total tax: {total_tax}")

# To create a re-usable function
def calculate_tax(bill, tax_rate):
    return round((bill * tax_rate) / 100.00, 2)

print("Total tax:", calculate_tax(175.00, 15))
print("Total tax:", calculate_tax(164.33, 22))