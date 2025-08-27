# #print("File Structure")

# x = 120
# y = 200
# z = 300

# def add(x, y, z):
#     return x + y + z

# print(add(x, y, z))

# with open("readme.md", "r", encoding="utf-8", errors="ignore") as file:
#     print(file.read())

  # Open 'readme.md' in write mode and write text

# text = "Hello, Welcome to PLP Academy!"
# with open("readme.md", "r", encoding="utf-8") as file:
#     print(file.read())


#   # Append text to the file
# with open("readme.md", "a", encoding="utf-8", errors="ignore") as file:
#     file.write("\nWelcome to PLP")

# # Now read the file content and print
# with open("readme.md", "r", encoding="utf-8", errors="ignore") as f:  # use a different variable name
#     print(f.read())

try:
    with open("Book1.xlsx", "rb") as f:
        content = f.read()
        print("Excel file opened successfully")
except Exception as e:
    print("Error:", e)



 


