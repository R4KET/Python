print("Hello, world!")
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def delete_nth_node(self, n):
        if self.head is None:
            return
        current_node = self.head
        previous_node = None
        count = 1
        while current_node is not None:
            if count % n == 0:
                if previous_node is None:
                    self.head = current_node.next
                else:
                    previous_node.next = current_node.next
                current_node = current_node.next
            else:
                previous_node = current_node
                current_node = current_node.next
            count += 1

    def __str__(self):
        linked_list_str = ""
        current_node = self.head
        while current_node is not None:
            linked_list_str += str(current_node.data) + " -> "
            current_node = current_node.next
        linked_list_str += "None"
        return linked_list_str

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)
linked_list.append(7)
linked_list.append(8)
linked_list.append(9)
linked_list.append(10)

print("Original linked list:")
print(linked_list)

linked_list.delete_nth_node(3)

print("Linked list after deleting every 3rd node:")
print(linked_list)
