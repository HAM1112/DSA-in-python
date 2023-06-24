class Node():
    def __init__(self,data) -> None:
        self.data = data
        self.right = None
        self.left = None
# insert
# inorder Display
# search for value
# find smallest value
# find largest value
class BinarySearchTree():
    def __init__(self) -> None:
        self.root = None
    
    #insert a value
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
    
    # Inorder display 
    def displayInorder(self):
        if self.root is None:
            print("Tree is empty")
            return
        return self._inorder(self.root)
    def _inorder(self, node):
        return (self._inorder(node.left) + [node.data] + self._inorder(node.right)) if node else []  
    
    # Search for a value
    def search(self,val):
        return self._search(self.root,val)
    def _search(self, node , val):
        if node is None:
            print("value not found")
            return
        if node.data == val :
            print("value found")
            return 
        if val < node.data:
            self._search(node.left,val)
        elif val > node.data:
            self._search(node.right,val)
    
    def smallest(self):
        pointer = self.root
        if pointer is None:
            print("Tree is empty")
            return
        while pointer.left is not None:
            pointer = pointer.left
        print(f'smallest value is {pointer.data}')
        return pointer.data    
    def largest(self):
        pointer = self.root
        if pointer is None:
            print("Tree is empty")
            return
        while pointer.right is not None:
            pointer = pointer.right
        print(f"largest value is {pointer.data}")
        return pointer.data
            
    
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
# arr = [i for i in range(1,21)]
# for i in arr:
#     print(i,end=" ")
#     BTS.search(i)

BTS.smallest()
BTS.largest()