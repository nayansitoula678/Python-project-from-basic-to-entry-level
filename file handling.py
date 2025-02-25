import os

file_name = "example_file.txt"

# Create and write random text to the file
random_text = "This is some random text written to the file."
with open(file_name, "w") as file:
    file.write(random_text)

# Read the content from the file
with open(file_name, "r") as file:
    print("File content:", file.read())

# Delete the file after use
if os.path.exists(file_name):
    os.remove(file_name)
    print(f"{file_name} has been deleted.")
else:
    print(f"{file_name} does not exist.")
