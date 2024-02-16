class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not bool(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def remove_nth_element(self, n):
        if n > self.size():
            return "Error: n is greater than the size of the queue"
        else:
            for i in range(n-1):
                self.dequeue()
            self.dequeue()

    def swap_first_last(self):
        if self.size() < 2:
            return "Error: queue has less than 2 elements"
        else:
            self.items[0], self.items[-1] = self.items[-1], self.items[0]
            return self.items
        
        

kolejka = Queue()
kolejka.enqueue(1)
kolejka.enqueue(2)
kolejka.enqueue(3)
kolejka.enqueue(4)
kolejka.enqueue(5)

print(kolejka.items)

kolejka.swap_first_last()

print(kolejka.items)