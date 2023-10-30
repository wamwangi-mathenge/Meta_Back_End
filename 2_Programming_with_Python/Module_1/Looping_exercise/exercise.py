num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

# Under the num_list, create a new for loop and print out each value on the list in sequential order

count = 0

for idx, i in enumerate(num_list):
    # print(i)
    # Create a condition that will look for all numbers that are greater than 45
    if i == 36:
        print(f"Number found at position: {idx}")
        count +=1
        break
    else:
        print(f"Number not found")
        
        
        
print(count)