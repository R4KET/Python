class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove_every_nth_element(self, n):
        if n < 1:
            return

        if n == 1:
            self.head = None
            return

        current = self.head
        count = 1
        while current:
            if count % (n - 1) == 0 and current.next:
                current.next = current.next.next
            current = current.next
            count += 1

    def move_greater_to_end(self):
        if not self.head:
            return

        current = self.head
        total = 0
        count = 0
        while current:
            total += current.data
            count += 1
            current = current.next

        average = total / count

        current = self.head
        previous = None
        end = None
        while current:
            if current.data > average:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                if not end:
                    end = current
                else:
                    end.next = current
                    end = end.next
                current = current.next
            else:
                previous = current
                current = current.next

        if end:
            end.next = None

        if end:
            current = self.head
            while current.next:
                current = current.next
            current.next = end

    def get_length(self):
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next
        return length

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def swap_with_adjacent(self, x):
        current = self.head

        while current and current.next:
            if current.data == x:
                current.data, current.next.data = current.next.data, current.data
                return
            current = current.next

    def move_closest_to_end(self, x):
        if not self.head:
            return

        current = self.head
        prev = None
        closest = None
        min_distance = float('inf')

        while current:
            distance = abs(current.data - x)
            if distance < min_distance:
                min_distance = distance
                closest = current
                prev_closest = prev
            prev = current
            current = current.next

        if closest != self.head:
            prev_closest.next = closest.next
            current = self.head
            while current.next:
                current = current.next
            current.next = closest
            closest.next = None

    def swap_max(self):
        if not self.head:
            return

        current = self.head
        max_node = current
        prev_max = None

        while current.next:
            if current.next.data > max_node.data:
                prev_max = current
                max_node = current.next
            current = current.next

        if max_node != self.head:
            if prev_max:
                prev_max.next = max_node.next
            else:
                self.head = max_node.next

            current = self.head
            while current.next:
                current = current.next
            current.next = max_node
            max_node.next = None

# Przykład użycia funkcji
linked_list = LinkedList()
data = [10, 2, 1, 9, 3, 4, 6, 54, 12, 0, 9]  # Podaj dane, jakie chcesz dodać do listy

for item in data:
    linked_list.append(item)

print("Pierwotna lista:")
linked_list.display()

n = 3  # Zdefiniuj wartość n
linked_list.remove_every_nth_element(n)

print("Lista po usunięciu co", n, "-tego elementu:")
linked_list.display()

linked_list.move_greater_to_end()

print("Lista po przeniesieniu większych elementów na koniec:")
linked_list.display()

x1 = 3
linked_list.swap_with_adjacent(x1)
print("Lista po zamianie elementu", x1, "z sąsiednim:")
linked_list.display()

x2 = 11
linked_list.move_closest_to_end(x2)
print("Lista po przesunięciu najbliższego elementu do", x2, "na koniec:")
linked_list.display()

linked_list = LinkedList()
data = [10, 2, 1, 100, 3, 4, 6, 54, 12, 0, 9]  # Podaj dane, jakie chcesz dodać do listy

for item in data:
    linked_list.append(item)

linked_list.swap_max()
print("Lista po przeniesieniu maksymalnego elementu na koniec:")
linked_list.display()
