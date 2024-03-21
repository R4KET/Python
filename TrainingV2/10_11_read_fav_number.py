import json

filename = 'numbers_10_11.json'
with open(filename) as f:
    number = json.load(f)

print(number)