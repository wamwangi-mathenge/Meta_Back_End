# Type Casting is the process of converting one data type to another.
# There are 2 types of type casting: Implicit & Explicit

# IMPLICIT DATA CONVERSION
# Implicit data type conversion is performed automatically by Python's compiler to prevent data loss
# It will convert for example an INT to a FLOAT if it picks up that the inserted value is a decimal
# Python will only be able to convert values if the data types are compatible.
# INT and FLOAT = COMPATIBLE
# INT and STRING != COMPATIBLE => Python will throw a Type Error

# EXPLICIT DATA CONVERSION
# This is done by using the provided Python functions
# Some of the most common functions are string, integer and float


# str()
# Used to convert any data type into a string data type
print(str(11))

# int()
# Used to convert any data type into a integer data type
print(int(20.9))


# float()
# Used to convert any data type into a float data type
print(float(13))

# Some other type-casting functions that have a similar structure are:
# ord() => returns an integer representing the underlying unicode character
print(ord('B'))
print(ord('y'))
print(ord('m'))
# hex() => converts a given integer to a hexadecimal string
print(hex(9))
print(hex(1))
print(hex(3))
# oct() => takes an integer and returns a string representing an oct to a number
print(oct(2))
print(oct(4))
print(oct(8))
