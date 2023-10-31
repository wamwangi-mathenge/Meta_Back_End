drinks = {
    1: "Coffee",
    2: "Tea",
    3: "Juice"
}

print(drinks)
print(drinks[1])

# Accessing a dictionary
drinks[2] = "Strong tea"
print(drinks)

# Deleting an item in a dictionary
del drinks[2]
print(drinks)

my_dict = {
    1: "Test",
    "Name": "Brian"
}

print(type(my_dict))
print(my_dict)

# Accessing a key
print(my_dict[1])
my_dict["Name"] = "Pam"
print(my_dict)

# Adding a key
my_dict["Job"] = "Cloud engineer"
print(my_dict)

# Updating a key
my_dict[1] = "Not a test"
print(my_dict)

# Removing a key
del my_dict[1]
print(my_dict)

# Iterating over a dictionary
for x in my_dict:
    print(f"{x}") # Only prints out the keys
    

# To gain access to both the keys and values
for x, y in my_dict.items():
    print(f"{x}: {y}")