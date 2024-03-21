import json

number = input("What is your favorite number? ")

filename = 'numbers_10_11.json'
with open(filename,'w') as f:
    json.dump(int(number),f)