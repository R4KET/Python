import os
import shutil

def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
            print(f"Contents of {file_name}:")
            print(content)
    except FileNotFoundError:
        pass  # Fail silently if the file is missing

read_file("cats.txt")
read_file("dogs.txt")

try:
    os.makedirs("test_location")
except FileExistsError:
    pass

try:
    shutil.move("dogs.txt", "test_location/dogs.txt")
except FileNotFoundError:
    pass  # Fail silently if the file is missing
