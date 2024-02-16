import time

class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

def add_event(bst, key):
    if bst.search(bst.root, key) is None:
        bst.root = bst.insert(bst.root, key)
        return True
    return False

def remove_event(bst, key):
    node = bst.search(bst.root, key)
    if node:
        bst.root = remove_node(bst.root, node)
        return True
    return False

def remove_node(root, node):
    if root is None:
        return root
    if node.key < root.key:
        root.left = remove_node(root.left, node)
    elif node.key > root.key:
        root.right = remove_node(root.right, node)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        root.key = get_min_value(root.right)
        root.right = remove_node(root.right, root)
    return root

def get_min_value(root):
    current = root
    while current.left is not None:
        current = current.left
    return current.key

def check_reservation(bst, key):
    current = bst.root
    while current:
        if key - 3 <= current.key <= key + 3:
            return False
        elif key < current.key:
            current = current.left
        else:
            current = current.right
    return True

def print_events(bst):
    events = []
    in_order_traversal(bst.root, events)
    print("Planowane zdarzenia:", events)

def in_order_traversal(root, events):
    if root:
        in_order_traversal(root.left, events)
        events.append(root.key)
        in_order_traversal(root.right, events)

# Example
bst = BST()
current_time = int(time.time())  # Get current system time

add_event(bst, 41)
add_event(bst, 47)
add_event(bst, 50)
add_event(bst, 58)

print_events(bst)

reservation_attempt_1 = 48
reservation_attempt_2 = 20
reservation_attempt_3 = 54

if check_reservation(bst, reservation_attempt_1):
    print(f"Próba rezerwacji {reservation_attempt_1} – odmowa")
else:
    print(f"Próba rezerwacji {reservation_attempt_1} – sukces")

if check_reservation(bst, reservation_attempt_2):
    print(f"Próba rezerwacji {reservation_attempt_2} – odmowa")
else:
    print(f"Próba rezerwacji {reservation_attempt_2} – sukces")

if check_reservation(bst, reservation_attempt_3):
    print(f"Próba rezerwacji {reservation_attempt_3} – sukces")
else:
    print(f"Próba rezerwacji {reservation_attempt_3} – odmowa")
