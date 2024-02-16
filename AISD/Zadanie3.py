import random

class IntPair:
    def __init__(self, first, second):
        self.first = first
        self.second = second
        self.sum = first + second

def generate_random_pairs(count): #Generator par losowych liczb calkowitych
    pairs = []
    for _ in range(count):
        first = random.randint(1, 100)
        second = random.randint(1, 100)
        pair = IntPair(first, second)
        pairs.append(pair)
    return pairs

pair_list = generate_random_pairs(10)

for i, pair in enumerate(pair_list, 1):
    print(f"Para {i}: ({pair.first}, {pair.second}, {pair.sum})")

def calculate_sum_and_add_average(pair_list): #Oblicza sumę elementów na liście i dodaje średnią jako 11. element listy.
    total_sum = sum(pair.first + pair.second for pair in pair_list)
    average = total_sum / (len(pair_list) * 2)
    pair_list.append(IntPair(average, average))
    return pair_list

pair_list = calculate_sum_and_add_average(pair_list)

print("Lista z dodaną średnią -------------------------------------------------------------")
for i, pair in enumerate(pair_list, 1):
    print(f"Para {i}: ({pair.first}, {pair.second}, {pair.sum})")

# Usuń pierwszy napotkany maksymalny element z listy
max_value = max(pair_list, key=lambda pair: pair.first)
pair_list.remove(max_value)
print(f"Usunięto pierwszy napotkany maksymalny element: ({max_value.first}, {max_value.second}, {max_value.sum})")

print("Lista po usunięciu maksymalnego elementu -------------------------------------------------------------")
for i, pair in enumerate(pair_list, 1):
    print(f"Para {i}: ({pair.first}, {pair.second}, SUMA: {pair.sum})")

# Przenieś pozostałe pary do kolejki
class Kolejka:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

pair_queue = Kolejka()
for pair in pair_list:
    pair_queue.enqueue(pair)

# Oblicz sumę par liczb i uporządkuj je w kolejności rosnącej
total_sum = 0
sorted_pairs = []

while not pair_queue.is_empty():
    pair = pair_queue.dequeue()
    total_sum =+ pair.sum
    sorted_pairs.append(pair)

sorted_pairs = sorted(sorted_pairs, key=lambda pair: pair.sum)

print(f"Suma wszystkich par liczb: {total_sum}")

print("Pary w kolejności rosnącej -------------------------------------------------------------")
for i, pair in enumerate(sorted_pairs, 1):
    print(f"Para {i}: ({pair.first}, {pair.second}, SUMA: {pair.sum})")

