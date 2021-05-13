# open the file
file = open("my_file.txt")
# get contents
contents = file.read()
print(contents)
# close file and release resources
file.close()

# convention:
with open("my_file.txt") as f:
    content = f.read()
    print(content)

# writing mode="w" or mode="a"
with open("my_file.txt", mode="a") as f2:
    f2.write("\nnew line")

with open("new_file.txt", mode="w") as f3:
    f3.write("this is a brand new file")

    

