class Node():
    def __init__(self, value) -> None:
        self.next = None
        self.data = value
        
        
class LinkedList():
    head = None 
    size = 0 
    
    # addd value to the end of an array
    def append(self,value):
        newNode = Node(value)
        
        if self.head == None:
            self.head = newNode
        else:
            pointer = self.head
            while pointer.next is not None:
                pointer = pointer.next
            pointer.next = newNode
        self.size += 1
        
    def prepend(self,value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        
    
    # display all the values in an array 
    def print_All_value(self):
        if self.head == None:
            print("Linked List is empty")
            return
        else:
            pointer = self.head
            while pointer is not None:
                print(f"{pointer.data} ")
                pointer = pointer.next
    
    # number of nodes in the list
    def numberOfItems(self):
        if self.head is None:
            print("empty")
        else:
            counter = 0
            pointer = self.head
            while pointer is not None:
                counter += 1
                pointer = pointer.next

            print("Number of items is " + str(counter))
            return counter
    
    # Get head node 
    def start(self):
        if self.head == None : return "List is empty"
        start = f"FIRST NODE == value : {self.head.data}  "
        return start
    
    # get tail node // last node
    def tail(self):
        if self.head == None : return "List is empty"
        pointer = self.head
        
        while pointer.next is not None:
            pointer = pointer.next
        return f"LAST NODE == value : {pointer.data} "
            
        
LL1 = LinkedList()
arr = [3,2,4,6,3,6,7,7,8,4,2]

for i in range(len(arr)):
    LL1.append(arr[i])

LL1.print_All_value()