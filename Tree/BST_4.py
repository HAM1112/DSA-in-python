class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        
class BTS():
    def __init__(self) -> None:
        self.root = None
        
    def insert(self,val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(self.root,val)
    def _insert(self,node,val):
        if val < node.data :
            if node.left is None:
                node.left = Node(val)
            else:
                self._insert(node.left)
        elif val > node.data :
            if node.right is None:
                node.right = Node(val)
            else:
                self._insert(node.right,val)
            