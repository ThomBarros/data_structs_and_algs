class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self._count = 0

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            self._count += 1
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value == node.value:
            return
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
                self._count += 1
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
                self._count += 1
            else:
                self._insert_recursive(node.right, value)

    def get_node_count(self):
        return self._count 
       
    def print_values(self):
        self._print_inorder(self.root)

    def _print_inorder(self, node):
        if node:
            self._print_inorder(node.left)
            print(node.value)
            self._print_inorder(node.right)

    def delete_tree(self):
        self.root = None
        self._count = 0 

    def is_in_tree(self, value):
        if self.root is None:
            raise Exception("Tree is empty")
        else:
            return self._search(self.root, value)

    def _search(self, node, value):
        if node is None:
            return False 
        if value == node.value:
            return True
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    def get_height(self):
        if self.root is None:
            return 0 
        return self._get_height_recursive(self.root)

    def _get_height_recursive(self, node):
        if node is None:
            return -1
        return 1 + max(self._get_height_recursive(node.left), self._get_height_recursive(node.right))         
        
    def get_min(self):
        if self.root is None:
            raise Exception("Tree is empty")

        current = self.root
        while current:
            if current.left is None:
                break
            current = current.left
        return current.value

    def get_max(self):
        if self.root is None:
            raise Exception("Tree is empty")

        current = self.root
        while current:
            if current.right is None:
                break
            current = current.right

        return current.value

    def is_binary_search_tree(self):
        if self.root is None:
            raise Exception("Tree is empty")
        return self._is_bst_recursive(self.root, float('-inf'), float('inf'))

    def _is_bst_recursive(self, node, min_val, max_val):
        if node is None:
            return True
        if not (min_val < node.value < max_val):
            return False
        return (self._is_bst_recursive(node.left, min_val, node.value) and self._is_bst_recursive(node.right, node.value, max_val))

    def delete_value(self, value):
        if self.root is None:
            raise Exception("Tree is empty")
        elif not self.is_in_tree(value):
            raise Exception("Value not in tree")
        self.root = self._delete_recursive_value(self.root, value)

    def _delete_recursive_value(self, node, value):
        if node is None:
            return None
        if value < node.value:
            node.left = self._delete_recursive_value(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive_value(node.right, value)
        else:
            if node.left is None and node.right is None:
                self._count -= 1
                return None

            if node.left is None:
                self._count -= 1
                return node.right
            if node.right is None:
                self._count -= 1
                return node.left

            successor_value = self.get_successor(node.right)
            node.value = successor_value
            node.right = self._delete_recursive_value(node.right, successor_value)

        return node
    
    def get_successor(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.value


def run_tests():
    print("Creating tree...")
    bst = BinarySearchTree()

    values = [50, 30, 70, 20, 40, 60, 80]
    for v in values:
        bst.insert(v)

    print("Inserted values:", values)
    print("Node count (should be 7):", bst.get_node_count())

    bst.insert(30)
    print("After duplicate insert (should still be 7):", bst.get_node_count())

    print("Search 40 (True):", bst.is_in_tree(40))
    print("Search 100 (False):", bst.is_in_tree(100))

    print("Min (should be 20):", bst.get_min())
    print("Max (should be 80):", bst.get_max())

    print("Height (should be 2):", bst.get_height())

    print("Inorder traversal (should be sorted):")
    bst.print_values()

    print("\nDeleting leaf node 20...")
    bst.delete_value(20)
    print("Node count (should be 6):", bst.get_node_count())
    bst.print_values()

    print("\nDeleting node 30 (one child)...")
    bst.delete_value(30)
    print("Node count (should be 5):", bst.get_node_count())
    bst.print_values()

    print("\nDeleting node 70 (two children)...")
    bst.delete_value(70)
    print("Node count (should be 4):", bst.get_node_count())
    bst.print_values()

    print("\nDeleting root 50...")
    bst.delete_value(50)
    print("Node count (should be 3):", bst.get_node_count())
    bst.print_values()

    print("\nTrying to delete 999 (should raise exception)...")
    try:
        bst.delete_value(999)
    except Exception as e:
        print("Caught expected exception:", e)

    print("\nIs valid BST (should be True):", bst.is_binary_search_tree())

    print("\nDeleting entire tree...")
    bst.delete_tree()
    print("Node count (should be 0):", bst.get_node_count())
    print("Height (should be 0):", bst.get_height())

    print("\nAll tests completed.")


if __name__ == "__main__":
    run_tests()