list1 = [1, 2, 3, 4, 5] # List of integers

print(list1)
print(*list1)
print(list1[2]) # Accessing list elements

# Adding to the list
list1.append(6) # Adds an element to the end of the list
print(list1)

list1.extend([7, 8, 9]) # Adds to the end of the list
print(list1)


# Removing from a list
list1.pop(2) # Removes an element at the specified index
print(list1)

del list1[3]
print(list1)

# Iterating through a list
for element in list1:
    print(f"Value: {element}")

list2 = ['A', 'B', 'C', 'D'] # List of strings

list3 = ["Hello", 1, True, 40.22] # Mixed data types

list4 = [1, [2, 3, 4], 5, 6] # Nested lists

