#ERROR HANDLING IN PYTHON
try:
    with open("readme.md", "r", encoding="utf-8") as file:
        data = file.read()  # <- this line must be indented
        print(data)         # <- also indented inside the with block
except FileNotFoundError:
    print("File not found, please check file path.")
