cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here's the original list:")
print(cars)

print("Here's the sorted list:")
print(sorted(cars))

print("Here's the original list again:")
print(cars)

print("Here's the reverse-sorted list:")
print(sorted(cars, reverse=True))

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

print(len(cars))

print("-----")

cars = ['audi', 'bmw', 'suburu', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())