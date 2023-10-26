# Looping Constructs: Practical Examples

## For Loop
The `for` loop makes it easy to work with any type of sequence in Python.

```
cities = ["Nairobi", "Cape Town", "Cairo", "Casablanca", "Windhoek"]

for city in cities:
    print(f"One of my favorite cities is: {city}")
```

In the code snippet above, the for loop iterates over the contents of the favorites list and prints out a sentence with the dessert name for each item in the list.

The for loop is based on the size or length of the elements to iterate over.

## While Loop
A `while` loop is based upon a condition being true. Once the condition is true the loop stops. The amount of times the while loop is executed is not known ahead of time as it is with the for loop.

If you take the above for loop and convert that to the while loop alternative, you will end up with something like this:

```
favorites = ["Nairobi", "Cape Town", "Jo-burg", "Cairo", "Casablanca", "Windhoek"]

count = 0

while count < len(favorites):
    print(f"My favorite city is: {favorites[count]}")
    count += 1
```

You need to declare a counter variable. The counter variable is then compared to the length of the favorites list. As you loop through the counter is incremented. Once the condition `count < len(favorites)` is no longer true, the loop will stop.