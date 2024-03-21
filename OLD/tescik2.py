class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class AirTrafficControl:
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
            return "Reservation successful"
        else:
            current = self.root
            while current is not None:
                if (current.val - 3) <= time <= (current.val + 3):
                    return "Reservation failed"
                elif current.val < time:
                    current = current.right
                else:
                    current = current.left
            self.root = self.insert(self.root, time)
            return "Reservation successful"

    def land_plane(self, time):
        if self.root is None:
            return "No such reservation"
        else:
            current = self.root
            while current is not None:
                if current.val == time:
                    self.root = self.delete(self.root, time)
                    return "Landing successful"
                elif current.val < time:
                    current = current.right
                else:
                    current = current.left
            return "No such reservation"

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)

    def display_schedule(self):
        self.inorder(self.root)