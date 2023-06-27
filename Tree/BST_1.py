class Node():
    def __init__(self,data) -> None:
        self.data = data
        self.right = None
        self.left = None

# insert
# inorder Display
class BinarySearchTree():
    def __init__(self) -> None:
        self.root = None
    
    def insertValue(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert_recursive(self.root,val)
    def _insert_recursive(self,node,val):
        if val < node.data :
            if node.left is None:
                node.left = Node(val)
            else:
                self._insert_recursive(node.left,val)
        elif val > node.data :
            if node.right is None:
                node.right = Node(val)
            else:
                self._insert_recursive(node.right, val)
    def displayInorder(self):
        if self.root is None:
            print("Tree is empty")
            return
        return self._inorder(self.root)
    def _inorder(self, node):
        return (self._inorder(node.left) + [node.data] + self._inorder(node.right)) if node else [] 
    
    #deletion 
    def delete(self,val):
        self._delete(self.root,val)
    def _delete(self,node,val):
        if node is None:
            return node
        if val < node.data :
            node.left = self._delete(node.left,val)
        elif val > node.data :
            node.right = self._delete(node.right,val)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            minnode = self.smallest(node.r)
            node.data = minnode.data
            node.r = self._delete(node.r,minnode)
        return node
        
        
                

BTS = BinarySearchTree()

BTS.insertValue(6)
BTS.insertValue(3)
BTS.insertValue(5)
BTS.insertValue(1)
BTS.insertValue(8)
BTS.insertValue(10)
BTS.insertValue(15)
BTS.insertValue(20)
print(BTS.displayInorder())
BTS.delete(5)
print(BTS.displayInorder())

