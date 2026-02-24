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
            return 

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
        pass

    def delete_tree(self):
        pass

    def is_in_tree(self):
        pass

    def get_height(self):
        pass
        
    def get_min(self):
        pass

    def get_max(self):
        pass

    def is_binary_search_tree(self):
        pass

    def delete_value(self):
        pass

    def get_successor(self):
        pass


















