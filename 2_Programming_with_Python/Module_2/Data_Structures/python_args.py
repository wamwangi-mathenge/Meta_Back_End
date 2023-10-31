# def sum_of(a, b):
#     return a + b

# print(sum_of(2, 3)) # Adding a 3rd parameter will result in an error

def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(sum_of(2, 3, 4, 10))