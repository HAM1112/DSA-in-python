class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self._insert_recursive(self.root, val)

    def _insert_recursive(self, node, val):
        if node is None:
            return Node(val)
        if val < node.data:
            node.left = self._insert_recursive(node.left, val)
        else:
            node.right = self._insert_recursive(node.right, val)
        return node

    def delete(self, val):
        self.root = self._delete_recursive(self.root, val)

    def _delete_recursive(self, node, val):
        if node is None:
            return node

        if val < node.data:
            node.left = self._delete_recursive(node.left, val)
        elif val > node.data:
            node.right = self._delete_recursive(node.right, val)
        else:
            # Case 1: Node has no children or only one child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Case 2: Node has two children
            # Find the minimum value in the right subtree
            min_node = self._find_min(node.right)

            # Replace the node's data with the minimum value
            node.data = min_node.data

            # Delete the minimum node from the right subtree
            node.right = self._delete_recursive(node.right, min_node.data)

        return node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def inorder(self):
        return self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        # if node is not None:
        #     self._inorder_recursive(node.left)
        #     print(node.data)
        #     self._inorder_recursive(node.right)
        return (self._inorder_recursive(node.left) + [node.data] + self._inorder_recursive(node.right)) if node else []


# Example usage:
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("Before deletion:")
print(bst.inorder())

bst.delete(30)

print("After deletion:")
print(bst.inorder())
