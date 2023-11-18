# with open("newfile.txt", "w") as file:
#     file.writelines(["Hello Brian!!!", "\nThis is a new file!!!"])
    
    
try:
    with open("/sample/newfile.txt", "w") as file:
        file.writelines(["Hello Brian!!!", "\nThis is a new file!!!"])
except Exception as e:
    print(e, "File not found")