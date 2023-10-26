# Match statements are used when checking for multiple conditions
# Using if/else statements when having multiple conditions can get messy.
# To simplify this process, match statements can be used.

# Write code to print http error messages according to error_codes

# status_code = 409
status_code = int(input("Enter the status code: "))

match status_code:
    case 200 | 201:
        print("Success")
    case 400:
        print("Bad Request")
    case 404:
        print("Not Found")
    case 666:
        print("You're the Devil Mate :(")
    case _:
        print("Unknown Status Code")