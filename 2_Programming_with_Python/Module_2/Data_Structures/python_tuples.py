my_tuple = (1, 'strings', 4.5, True, 4.5)

# Accessing items in a tuple
print(my_tuple[1])

# Determining the data type
print(type(my_tuple))

# Counting the number of occurrences of an item
print(my_tuple.count('strings'))
print(my_tuple.count(4.5))

# Determining the index of an element
print(my_tuple.index('strings'))
print(my_tuple.index(4.5))

# Iterating over the elements in a tuple
for x in my_tuple:
    print(f"Tuple item: {x}")
    
    
# Tuple items are IMMUTABLE - CANNOT BE CHANGED
# my_tuple[0] = 5
# print(my_tuple)