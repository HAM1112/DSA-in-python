class Node():
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None
        
class BST():
    def __init__(self) -> None:
        self.root = None
        
    def insert(self,val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(self.root, val)        
    def _insert(self, node , val):
        if val < node.data:
            if node.left is None:
                node.left = Node(val)
            else:
                self._insert(node.left,val)
        
        elif val > node.data:
            if node.right is None:
                node.right = Node(val)
            else:
                self._insert(node.right ,val)
    def inOrder(self):
        return self._inorder(self.root)
    def _inorder(self,node):        
        return (self._inorder(node.left) + [node.data] + self._inorder(node.right)) if node else []
    
    
    # Sum of all node values
    def sumOfNodes(self):
        output = self._sum(self.root)
        return output
    def _sum(self,node):
        if node:
            return self._sum(node.left) + node.data + self._sum(node.right)
        return 0
    
    #smallest
    def smallest(self):
        return self._smallest(self.root)
    def _smallest(self,node):
        pointer = node
        
        while pointer.left is not None:
            pointer = pointer.left

        return pointer.data    
    
    #validate
    def isBst(self):
        return self._isbst(self.root,float('-inf'),float('inf'))
    def _isbst(self,node, minval, maxval):
        if node is None:
            return True
        
        if node.data <= minval or node.data >= maxval:
            return False
        
        return (self._isbst(node.left,minval,node.data) and self._isbst(node.right,node.data,maxval))
    
    # deletion
    def delete(self,val):
        self._delete(self.root, val)
    def _delete(self,node,val):
        if node is None:
            return node
        if val < node.data:
            node.left = self.__delete(node.left,val)
        elif val > node.data:
            node.right = self._delete(node.right, val)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            minNode = self.smallest(node.r)
            node.data = minNode.data
            node.r = self._delete(node.r,minNode)
        return node            
    # def depth(self):
    #     return self._depth(self.root)
    # def _depth(self,node)
        
        
BST = BST()
BST.insert(25)
BST.insert(50)
BST.insert(10)
BST.insert(5)
print(BST.inOrder())
print(BST.isBst())
print(BST.smallest())
