class Node():
    def __init__(self,value):
        self.data = value
        self.next = None

class LinkedList():
    head = None
    def append(self,value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        else:
            pointer = self.head 
            while pointer.next is not None:
                pointer = pointer.next
            pointer.next = newNode
                
LL1 = LinkedList()



num = int(input("enter your decimal : "))
def decToBi(value):
    if value >=1 :
        decToBi(value//2)
    print(value % 2 , end=" ")


decToBi(num)

