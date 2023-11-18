# file = open('file.txt', mode="r")
with open('file.txt', mode='r') as file:
    data = file.readline()
    print(data)

# data = file.readline()

# print(data)

# file.close()