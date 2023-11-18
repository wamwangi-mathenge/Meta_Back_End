# File Handling

There are 2 file handling functions in Python
1. Open Functions
2. Close Functions

## Open Function
The open function is used for reading, writing and creating files.
The open function accepts 2 arguments.
1. FILE_NAME / FILE_LOCATION
2. MODE => Indicates what action is required such as reading, writing or creating. Also specifies if you want the file output in text or binary format.

### Mode Sets
`r` => Opens and reads a file in text format
`rb` => Opens and reads a file in binary format.
`r+` => Opens a file for reading and writing
`w` => Opens a file for writing
`a` => Opens file for editing or appending data

## Close Function
Used for closing the open file connection.\
It does not take any arguments.

There is one more way to open and close a function. This is with the `with open` function.
```
with open('testing.txt', r) as file:
```

The advantage of using it is that it closes the file automatically.


Python uses text as the default format in file handling.\
To set the file format to binary, you need to pass the letter `b` along with either the read or write option
