set_a = {1, 2, 3, 4, 5}
print(set_a)

# Sets do not allow duplicate values
set_duplicate = {1, 2, 3, 2, 5}
print(set_duplicate) # {1, 2, 3, 5}

# Set methods
# Adding values
set_a.add(6)
print(set_a)

# Removing values
set_a.remove(2)
print(set_a)

set_a.discard(3)
print(set_a)

# Math operations on sets
# Union
set_b = {1, 2, 3, 4, 5}
set_c = {4, 5, 6, 7, 8}

print(set_b.union(set_c)) # Joins the 2 sets together without the duplicate values
print(set_b | set_c) # Joins the 2 sets together as above

# Intersection
print(set_b.intersection(set_c)) # Values that match in set_b and set_c
print(set_b & set_c) # Values that match in set_b and set_c

# Set difference
print(set_b.difference(set_c)) # Outputs elements that are in set_b and not in set_c
print(set_b - set_c) # Outputs elements that are in set_b and not in set_c

# Symmetrical difference
print(set_b.symmetric_difference(set_c)) # Elements that are in set_b or set_c bit not in both sets
print(set_b ^ set_c)

# Elements in a set are unordered
# print(set_b[0]) # Gives an error