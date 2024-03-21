squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)


liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(liczby))
print(max(liczby))
print(sum(liczby))

squares = [value**2 for value in range(1, 11)] # list comprehension, lista skladana
print(squares)