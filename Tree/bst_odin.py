class Node():
    def __init__(self,data):
        self.data = data
        self.l = None
        self.r = None

class BinaryTree():
    def __init__(self):
        self.root = None
        self.node = 0
    
    # insert Using recursion 
    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root,data)
    
    def _insert_recursive(self,node,data):
        if data < node.data :
            if node.l is None:
                node.l = Node(data)
            else:
                self._insert_recursive(node.l ,data)
        elif data > node.data :
            if node.r is None:
                node.r = Node(data)
            else:
                self._insert_recursive(node.r,data) 
    
    def serach(self,data):
        if self.root is None:
            return "BST is Empty"
        return self._search(self.root , data)
    
    def _search(self,node,val):
        if node is None:
            return "BST does'nt contain the value"
        if node.data == val:
            return "Value  found"
        elif val < node.data :
            return self._search(node.l,val)
        return self._search(node.r,val)
    
    def displayInOrder(self):
        nodes = []
        self._inorder(self.root , nodes)
        return nodes
    

BTS = BinaryTree()

BTS.insert(6)
BTS.insert(10)
BTS.insert(3)
BTS.insert(4)
BTS.insert(7)

print(BTS.serach(8))



            
            
                    

    