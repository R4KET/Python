age = 1

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 40:
    price = 40
else:
    price = 10

print(f"Your admission cost is ${price}")