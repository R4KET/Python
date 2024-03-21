#for number in range(1,1000001):
#    print(number)

numbers = list(range(1,1000001))
min_value = min(numbers)
max_value = max(numbers)
sum_val = sum(numbers)
    
print(f"The minimal value is {min_value}")
print(f"The minimal value is {max_value}")
print(f"The sum of numbers is {sum_val}")

odd_numbers = list(range(1,20,2))
for odd_number in odd_numbers:
    print(odd_number)

threes = list(range(3,31))
for three in threes:
    print(three*3)

cubes = list(range(1,11))
for cube in cubes:
    print(cube**3)

cubes2 = [x**3 for x in range(1,11)]
print(cubes2)