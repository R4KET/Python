import random

age = random.randint(0, 100)
print(f"Wiek: {age}")

if age < 2:
    print("Niemowlecie")
if age >= 2 and age < 4:
    print("Dziecko uczace sie chodzic")
if age >= 4 and age < 13:
    print("Dziecko")
if age >= 13 and age < 20:
    print("Nastolatek")
if age >= 20 and age < 65:
    print("Dorosly")
if age >= 65:
    print("Senior")