import random

lottery = [1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e']
my_ticket = [2, 1, 3, 7]

iterations = 0

while True:
    selected_elements = random.sample(lottery, 4)
    iterations += 1

    if selected_elements == my_ticket:
        break

print("Congratulations! It took", iterations, "iterations to win with the ticket:", my_ticket)

#selected_elements = random.choices(lottery, k = 4)

#print(f"Any ticket matching these four numbers or letters wins a prize {selected_elements}")
