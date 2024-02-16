import time

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        else:
            if root.val < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root

    def minValueNode(self, root):
        current = root
        while(current.left is not None):
            current = current.left
        return current

    def delete(self, root, key):
        if root is None:
            return root
        if key < root.val:
            root.left = self.delete(root.left, key)
        elif(key > root.val):
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.key = self.minValueNode(root.right).val
            root.right = self.delete(root.right, root.key)
        return root

    def reserve_landing(self, time):
        if self.root is None:
            self.root = self.insert(self.root, time)
            return "Rezerwacja"
        else:
            current = self.root
            while current is not None:
                if (current.val - 3) <= time <= (current.val + 3):
                    return "Brak rezerwacji"
                elif current.val < time:
                    current = current.right
                else:
                    current = current.left
            self.root = self.insert(self.root, time)
            return "Rezerwacja"

    def land_plane(self, time):
        if self.root is None:
            return "Brak rezerwacji"
        else:
            current = self.root
            while current is not None:
                if current.val == time:
                    self.root = self.delete(self.root, time)
                    return "Ladowanie"
                elif current.val < time:
                    current = current.right
                else:
                    current = current.left
            return "Brak rezerwacji"

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)

    def display_schedule(self):
        self.inorder(self.root)

atc = BST()
current_time = time.time()

print(atc.reserve_landing(20))
print(atc.reserve_landing(41))
print(atc.reserve_landing(47))
print(atc.reserve_landing(50)) 
print(atc.reserve_landing(58))

atc.display_schedule() 

print(atc.reserve_landing(48)) 
print(atc.reserve_landing(54))  
print(atc.land_plane(54))  

atc.display_schedule()

landing_times = [20, 41, 47, 50, 58]
while landing_times:
    time = landing_times.pop(0)
    print(atc.land_plane(time))

atc.display_schedule()