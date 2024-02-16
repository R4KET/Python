class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)

def min(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current

def max(node):
    current = node
    while(current.right is not None):
        current = current.right
    return current

def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1
        
def predecesor(node, x):
    if node is None:
        return None
    if node.val == x:
        if node.left is not None:
            return max(node.left)
        else:
            return None
    if node.val > x:
        return predecesor(node.left, x)
    else:
        return predecesor(node.right, x)
    
def successor(node, x):
    if node is None:
        return None
    if node.val == x:
        if node.right is not None:
            return min(node.right)
        else:
            return None
    if node.val < x:
        return successor(node.right, x)
    else:
        left = successor(node.left, x)
        if left is not None:
            return left
        else:
            return node
        
def insertValue(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insertValue(root.right, key)
        else:
            root.left = insertValue(root.left, key)
    return root


def deleteValue(root, key):
    if root is None:
        return None
    if root.val < key:
        root.right = deleteValue(root.right, key)
    elif root.val > key:
        root.left = deleteValue(root.left, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = min(root.right)
        root.val = temp.val
        root.right = deleteValue(root.right, temp.val)
    return root
    
root = None
root = insert(None, 5)
insert(root, 3)
insert(root, 2)
insert(root, 0)
insert(root, 4)
insert(root, 9)
insert(root, 6)
insert(root, 1)
insert(root, 8)

print("InOrder: ") #LKP
inorder(root)
##print("PreOrder: ") #KLP
##preorder(root)
##print("PostOrder: ") #LPK
##postorder(root)
print("Min: " + str(min(root).val))
print("Max: " + str(max(root).val))
print("Wysokosc drzewa: " + str(height(root)))

print("Poprzednik: " + str(predecesor(root, 5).val))
print("Nastepnik: " + str(successor(root, 5).val))

print("================")
print("Wstawanie nowego wezla:")
insertValue(root, 7)
inorder(root)

print("================")
print("Usuwanie wskazanego wezla:")
deleteValue(root, 5)
inorder(root)