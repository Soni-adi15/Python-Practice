import os

# Specify the directory path
directory_path = "/"

# List and print contents of the directory
contents = os.listdir(directory_path)

print("Contents of the directory:")
for item in contents:
    print(item)
