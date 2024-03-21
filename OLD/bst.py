import random

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Wstawia nowy klucz do drzewa BST."""
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        """Pomocnicza funkcja do wstawiania klucza."""
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)
        return root

    def search(self, key):
        """Wyszukuje klucz w drzewie BST."""
        return self._search(self.root, key)

    def _search(self, root, key):
        """Pomocnicza funkcja do wyszukiwania klucza."""
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def delete(self, key):
        """Usuwa klucz z drzewa BST."""
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        """Pomocnicza funkcja do usuwania klucza."""
        if root is None:
            return root
        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.key = self._find_min(root.right)
            root.right = self._delete(root.right, root.key)
        return root

    def _find_min(self, root):
        """Znajduje minimalny klucz w drzewie."""
        while root.left is not None:
            root = root.left
        return root.key

    def inorder_traversal(self):
        """Przechodzi drzewo w kolejności InOrder."""
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, root, result):
        """Pomocnicza funkcja do przechodzenia drzewa InOrder."""
        if root:
            self._inorder_traversal(root.left, result)
            result.append(root.key)
            self._inorder_traversal(root.right, result)

    def preorder_traversal(self):
        """Przechodzi drzewo w kolejności PreOrder."""
        result = []
        self._preorder_traversal(self.root, result)
        return result

    def _preorder_traversal(self, root, result):
        """Pomocnicza funkcja do przechodzenia drzewa PreOrder."""
        if root:
            result.append(root.key)
            self._preorder_traversal(root.left, result)
            self._preorder_traversal(root.right, result)

    def postorder_traversal(self):
        """Przechodzi drzewo w kolejności PostOrder."""
        result = []
        self._postorder_traversal(self.root, result)
        return result

    def _postorder_traversal(self, root, result):
        """Pomocnicza funkcja do przechodzenia drzewa PostOrder."""
        if root:
            self._postorder_traversal(root.left, result)
            self._postorder_traversal(root.right, result)
            result.append(root.key)

    def find_minimum(self):
        """Znajduje minimalny klucz w drzewie."""
        if self.root is None:
            return None
        return self._find_minimum(self.root)

    def _find_minimum(self, root):
        """Pomocnicza funkcja do znajdowania minimalnego klucza."""
        while root.left is not None:
            root = root.left
        return root.key

    def find_maximum(self):
        """Znajduje maksymalny klucz w drzewie."""
        if self.root is None:
            return None
        return self._find_maximum(self.root)

    def _find_maximum(self, root):
        """Pomocnicza funkcja do znajdowania maksymalnego klucza."""
        while root.right is not None:
            root = root.right
        return root.key

    def tree_height(self):
        """Oblicza wysokość drzewa."""
        return self._tree_height(self.root)

    def _tree_height(self, root):
        """Pomocnicza funkcja do obliczania wysokości drzewa."""
        if root is None:
            return 0
        left_height = self._tree_height(root.left)
        right_height = self._tree_height(root.right)
        return max(left_height, right_height) + 1

    def find_successor(self, key):
        """Znajduje następnika podanego węzła."""
        node = self.search(key)
        if node is None:
            return None
        if node.right is not None:
            return self._find_min(node.right)
        successor = None
        current = self.root
        while current:
            if node.key < current.key:
                successor = current
                current = current.left
            elif node.key > current.key:
                current = current.right
            else:
                break
        return successor.key if successor else None

    def find_predecessor(self, key):
        """Znajduje poprzednika podanego węzła."""
        node = self.search(key)
        if node is None:
            return None
        if node.left is not None:
            return self._find_max(node.left)
        predecessor = None
        current = self.root
        while current:
            if node.key < current.key:
                current = current.left
            elif node.key > current.key:
                predecessor = current
                current = current.right
            else:
                break
        return predecessor.key if predecessor else None

    def insert_element(self, key):
        """Wstawia podany element w odpowiednie miejsce drzewa."""
        self.root = self._insert(self.root, key)

    def delete_element(self, key):
        """Usuwa podany element z drzewa."""
        self.root = self._delete(self.root, key)

# Przykład użycia funkcji
if __name__ == "__main__":
    bst = BST()
    keys = [50, 30, 70, 20, 40, 60, 80]

    for key in keys:
        bst.insert(key)

    print("InOrder Traversal:")
    print(bst.inorder_traversal())

    key_to_find_successor = 30
    successor = bst.find_successor(key_to_find_successor)
    if successor is not None:
        print(f"Successor of {key_to_find_successor}: {successor}")
    else:
        print(f"Successor of {key_to_find_successor}: None")

    key_to_find_predecessor = 60
    predecessor = bst.find_predecessor(key_to_find_predecessor)
    if predecessor is not None:
        print(f"Predecessor of {key_to_find_predecessor}: {predecessor}")
    else:
        print(f"Predecessor of {key_to_find_predecessor}: None")

    key_to_insert = 55
    bst.insert_element(key_to_insert)
    print(f"Inserted {key_to_insert} into the tree. InOrder Traversal:")
    print(bst.inorder_traversal())

    key_to_delete = 50
    bst.delete_element(key_to_delete)
    print(f"Deleted {key_to_delete} from the tree. InOrder Traversal:")
    print(bst.inorder_traversal())

    print(f"Minimum element in the tree: {bst.find_minimum()}")
    print(f"Maximum element in the tree: {bst.find_maximum()}")
    print(f"Height of the tree: {bst.tree_height()}")
    print("PreOrder Traversal:")
    print(bst.preorder_traversal())
    print("PostOrder Traversal:")
    print(bst.postorder_traversal())
    print("InOrder Traversal:")
    print(bst.inorder_traversal())
