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
            check = self.search(val)
            if check is True:
                print("Value already exsist")
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
    # inorder traversal
    def inorder(self):
        if self.root is None:
            print("Tree is empty")
            return
        return self._inorder(self.root)
    def _inorder(self,node):
        return (self._inorder(node.left) + [node.data] + self._inorder(node.right)) if node else []
    
    # search for element
    def search(self,val):
        if self.root is None:
            print("Tree is empty")
            return False
        return self._search(self.root,val)
    def _search(self,node,val):
        if node is None:
            # print("Value not Found")
            return False
        if node.data == val:
            print("Found the value")
            return True
        if val < node.data :
            return self._search(node.left,val)
        return self._search(node.right,val)
    
    # smallest value
    def smallest(self):
        smallestnode = self._smallest(self.root)
        return smallestnode.data
    def _smallest(self,node):
        pointer = node
        while pointer.left:
            pointer = pointer.left
        return pointer
        
            
    
    def delete(self,val):
        self._delete(self.root,val)
    
    def _delete(self, node, val):
        if node is None:
            return node

        if val < node.data:
            node.left = self._delete(node.left, val)
        elif val > node.data:
            node.right = self._delete(node.right, val)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_node = self._smallest(node.right)
            node.data = min_node.data
            node.right = self._delete(node.right, min_node.data)

        return node

    def isBst(self):
        return self._isbst(self.root,float('-inf'),float('inf'))
    def _isbst(self,node,minval,maxval):
        if node is None:
            return True
        
        if node.data <= minval or node.data >= maxval:
            return False
        
        return(self._isbst(node.left,minval,node.data) and self._isbst(node.right,node.data,maxval))
        
        

bst = BTS()
bst.insert(50)
bst.insert(60)
bst.insert(55)
bst.insert(95)
bst.insert(20)
bst.insert(55)

print(bst.inorder())
bst.delete(50)
print(bst.inorder())
print(bst.isBst())
