import os
import json

filename = 'numbers_10_11.json'

if os.path.exists(filename):
    with open(filename) as f:
        number = json.load(f)
    print(f"Your favorite number is: {number}")
else:
    number = input("What is  your favorite number? ")
    with open(filename,'w') as f:
        json.dump(int(number),f)
    print("Your favorite number has been saved.")