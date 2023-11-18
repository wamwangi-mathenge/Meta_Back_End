def divide(a, b):
    return a / b

# print(divide(40, 4))
# print(divide(40, 0)) # Division by zero error


# How to deal with errors
# Wrap your code using try and except statements
# Optimize the message that the user sees.
try:
    ans = divide(40, 0)
except ZeroDivisionError as e:
    print(e, "We cannot divide by zero")
    print(e.__class__)
except Exception as e:
    print(e, "Something went wrong!")