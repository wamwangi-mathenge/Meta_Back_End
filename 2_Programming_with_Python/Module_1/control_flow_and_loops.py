# if else

# In many cases, you may need to search for a particular item in a list.
# Once the item is found, there is no need to continue looping over the other results.

favorites = ["Nairobi", "Cape Town", "Cairo", "Casablanca", "Windhoek"]

# for city in favorites:
#     if city == "Nairobi":
#         print(f"My favorite city is {city}")
        
        
# What happens if you look for a city and that city is not on the list?
# We add an else statement to handle the case of when it is not found

# for city in favorites:
#     if city == "Nairobi":
#         print(f"Kenya's capital is {city}")
#     else:
#         print("Kenya's capital does not exist")
        

# -----BREAK-------
# Flaw in the above logic
# Change the search term to something that is on the list eg. Nairobi
# The city is on the list, but it still printed out the else condition
# To fix this use a control statement called "BREAK"

for city in favorites:
    if city == "Nairobi":
        print(f"Kenya's capital is {city}")
        break
    else:
        print(f"Kenya's capital does not exist")
        
        
# Running the above code will resolve the issue.
# The BREAK statement is used to stop the loop, which in turn stops the condition.
# Without the break, the loop will continue even after the `if` condition is met


# ------CONTINUE-------
# Similar to break, continue can be used to control the iteration of the loop.
# The key difference is that it can allow you to skip over a section of the loop but then continue on with the rest


for city in favorites:
    if city == "Cairo":
        continue
    print(f"Other cities in Africa are {city}")
    
# The outcome of the above code snippet will print everything except the Cairo city
