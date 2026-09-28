with open("sample.txt", "w") as file:
    file.write("Hello, Python Context Manager")

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)