# IndexError
items = [1, 2, 3, 4, 5]


try:
    item = items[6]
    print(item)
except:
    print("item does not exist in the list")
    
    
# ZeroDivisionError
def divide_by(a, b):
    return a / b

try:
    ans = divide_by(40, 0)
    print(ans)
except:
    print(0)
    
    
# FileNotFoundError


try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except:
    print("The file could not be found")