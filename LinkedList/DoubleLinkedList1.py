class Node():
    def __init__(self,value):
        self.data = value
        self.next = None
        self.prev = None

class DoublyLinkedList():
    head = None
    size = 0
    tail = None
    
    def append(self,value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
        else:
            pointer = self.head
            while pointer.next is not None:
                pointer = pointer.next
            newNode.prev = pointer
            pointer.next = newNode
            self.tail = newNode
        self.size += 1
    
    
    
    
    
    # DISPLAY 
    
    
    def displayAll(self):
        if self.head == None:
            print("Linked list is empty ")
        else:
            pointer = self.head 
            
            while pointer is not None:
                print(f"data is :: {pointer.data}")
                pointer = pointer.next
            print()
            print(f"size of Linked list is : {self.size}")
            print()
    def displayPrevNextOf(self,index):
        if self.head == None:
            print("Linked list is empty")
        elif index >= self.size or index < 0:
            print("Limint exceeded !!!!!!!!!!!!!")
        else:
            pointer = self.head
            counter = 0 
            while counter < index:
                pointer = pointer.next
                counter += 1
            print(f"value at index : {pointer.data}")
            print(f"value next of index: {pointer.next.data}")
            print(f"value prev of index: {pointer.prev.data}")
    
    def DisplayFirstNode(self):
        if self.head == None:
            print("Linked list is empty")
        else:
            print(self.head.data)
    def DisplayLastNode(self):
        if self.head == None:
            print("Linked list is empty")
        else:
            print(self.tail.data)
    
    
             
DLL1 = DoublyLinkedList()

DLL1.append("DATA  1")
DLL1.append("DATA  2")
DLL1.append("DATA  3")
DLL1.append("DATA  4")

DLL1.displayAll()

DLL1.displayPrevNextOf(2)

DLL1.DisplayFirstNode()
DLL1.DisplayLastNode()

