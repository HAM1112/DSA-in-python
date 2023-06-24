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
    
    # def displayInOrder(self):
    #     nodes = []
    #     self._inorder(self.root , nodes)
    #     return nodes
    
    # def _inorder(self,node,nodes):
    #     if node :
    #         self._inorder(node.l,nodes)
    #         nodes.append(node.data)
    #         self._inorder(node.r,nodes)
    
    # PREORDER
    def displayPreorder(self):
        return self.preorder(self.root)
    def preorder(self,node):
        return ([node.data] + self.preorder(node.l) + self.preorder(node.r)) if node else []
    
    # INORDER
    def displayInorder(self):
        return self.inorder(self.root)
    def inorder(self,node):
        return (self.inorder(node.l) + [node.data] + self.inorder(node.r)) if node else []
    
    # POSTORDER
    def displayPostorder(self):
        return self.postorder(self.root)
    def postorder(self,node):
        return (self.postorder(node.l) + self.postorder(node.r) + [node.data]) if node else []
    
    
    
    # Find smallest value in treee
    def smallest(self):
        pointer = self.root
        
        if pointer is None :
            print("Tree is empty")
            return
        
        while pointer.l :
            pointer = pointer.l
        
        return pointer.data
    
    # Find largest value in tree
    def largest(self):
        pointer = self.root
        
        if pointer is None:
            print("Tree is empty")
            return
        while pointer.r:
            pointer = pointer.r
        
        return pointer.data
    
    def delete(self, data):
        self.root = self._delete_recursive(self.root, data)

    def _delete_recursive(self, node, data):
        if node is None:
            return node

        if data < node.data:
            node.l = self._delete_recursive(node.l, data)
        elif data > node.data:
            node.r = self._delete_recursive(node.r, data)
        else:
            if node.l is None:
                return node.r
            elif node.r is None:
                return node.l

            min_node = self.smallest(node.r)
            node.data = min_node.data
            node.r = self._delete_recursive(node.r, min_node.data)
        return node

BTS = BinaryTree()

BTS.insert(6)
BTS.insert(10)
BTS.insert(3)
BTS.insert(4)
BTS.insert(7)

print(BTS.serach(8))
print(BTS.displayInorder())
# print(BTS.displayPostorder())
# print(BTS.displayPreorder())
print(BTS.smallest())
print(BTS.largest())

BTS.delete(10)

print(BTS.displayInorder())



            
            
                    

    