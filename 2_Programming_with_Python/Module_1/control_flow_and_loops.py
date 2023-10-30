# if else

# In many cases, you may need to search for a particular item in a list.
# Once the item is found, there is no need to continue looping over the other results.

favorites = ["Nairobi", "Cape Town", "Cairo", "Casablanca", "Windhoek"]

for city in favorites:
    if city == "Nairobi":
        print(f"My favorite city is {city}")
        
        
# What happens if you look for a city and that city is not on the list?
# We add an else statement to handle the case of when it is not found

for city in favorites:
    if city == "Kigali":
        print(f"Rwanda's capital is {city}")
    else:
        print("Rwanda's capital does not exist")