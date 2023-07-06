with open("my_file.txt") as file:
    contents = file.read()
    print(contents) # prints "Hello, world!" to the console
   
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.!")