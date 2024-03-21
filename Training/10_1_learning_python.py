# Reading the entire file
print("Reading the entire file:")
with open('learning_python.txt') as file_object:
    contents = file_object.read()
    print(contents)

# Looping over the file object
print("\nLooping over the file object:")
with open('learning_python.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

# Storing the lines in a list
print("\nStoring the lines in a list:")
with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# Open the file for reading
with open('learning_python.txt') as file_object:
    # Read each line and replace 'Python' with 'C'
    for line in file_object:
        modified_line = line.replace('Python', 'C')
        # Print each modified line
        print(modified_line.rstrip())

