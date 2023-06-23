class Node():
    def __init__(self,value):
        self.data = value
        self.next = None

class LinkedList():
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
            pointer.next = newNode
        self.size += 1
        self.tail = newNode
        self.sort()
    
    def sort(self):
        iPointer = self.head
        while iPointer != None:
            jPointer = iPointer.next
            while jPointer != None:
                if iPointer.data > jPointer.data:
                    temp = iPointer.data
                    iPointer.data = jPointer.data
                    jPointer.data = temp
                jPointer = jPointer.next
            iPointer = iPointer.next
    
    def removeDuplicate(self):
        pointer = self.head 
        while pointer.next is not None:
            if pointer.data == pointer.next.data:
                pointer.next = pointer.next.next
                self.size -= 1
            pointer = pointer.next
      
    def displayAll(self):
        if self.head == None:
            print("Link List is empty")
        else:
            pointer = self.head
            while pointer is not None:
                print(f"data is :: {pointer.data}" )
                pointer = pointer.next
        print()
        print(f"Size of Linked List is : {self.size}")                
        
print("========================================================================================================================================================")
LL1 = LinkedList()

LL1.append(9)
LL1.append(5)
LL1.append(13)
LL1.append(2)
LL1.append(4)
LL1.append(5)
LL1.append(23)
LL1.append(2)
LL1.append(85)
LL1.append(21)
LL1.append(98)
LL1.removeDuplicate()

LL1.displayAll()
print("========================================================================================================================================================")
