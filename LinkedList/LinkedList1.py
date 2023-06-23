class Node():
    def __init__(self,value):
        self.data = value
        self.next = None

class LinkedList():
    head = None
    size = 0
    
    def append(self,value):
        newNode = Node(value)
        if self.head == None :
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
        self.size += 1
    
    def insertAtIndex(self,value,index):
        if index > self.size or index < 0 :
            print("Sorry not possible!!! INDEX LIMIT EXCEEDED")
        elif index == 0:
            self.prepend(value)
        elif index == self.size:
            self.append(value)
        else:
            newNode = Node(value)
            counter = 0
            pointer = self.head
            while counter < index-1:
                pointer = pointer.next
                counter += 1
            newNode.next = pointer.next
            pointer.next = newNode
            self.size += 1                                                                    
     
    def displayAllValues(self):
        if self.head == None:
            print("Link List is empty")
        else:
            pointer = self.head
            while pointer is not None:
                print(f"data is :: {pointer.data}" )
                pointer = pointer.next
        print()
        print(f"Size of Linked List is : {self.size}")
        
     #node At index
    def at(self,index):
        if index >= self.size:
            print("INDEX EXCEEDED!!!!!")
            return 
        counter = 0
        pointer = self.head
        while counter < index:
            pointer = pointer.next
            counter += 1
        print(f"data at index {index} is : {pointer.data}")
         
    def tail(self):
        if self.head is None:
            print("Link List is empty")
        else:
            pointer = self.head
            while pointer.next is not None:
                pointer = pointer.next
            print(f"Tail node data = {pointer.data}")
    
    def pop(self):
        if self.head == None:
            print("Link List is empty")
        else:
            pointer = self.head
            while pointer.next.next is not None:
                pointer = pointer.next
            pointer.next = None
            self.size -=1
            
            
    def truncate(self):
        if self.head == None:
            print("Link List is empty")
        else:
            pointer = self.head
            self.head = pointer.next  
            self.size -= 1
            
    def removeFrom(self,index):
        if index < 0 or index >= self.size :
            print("Not possible ")
        elif index == 0 :
            self.truncate()
            self.size -= 1
        elif index == self.size - 1:
            self.pop()
            self.size -= 1
        else:
            counter = 0
            pointer = self.head
            while counter < index-1:
                pointer = pointer.next
                counter += 1
            pointer.next = pointer.next.next
            self.size -= 1
         
            
    def contain(self,value):
        if self.head == None:
            print("Link List is empty")
        else:
            pointer = self.head
            counter = 0
            while  pointer!= None:
                if(pointer.data == value):
                    print(f"value found at index {counter}")
                    break
                elif pointer.next == None:
                    print(f"Value Not Fount")
                pointer = pointer.next
                counter += 1 
            
            print()
    
    def toString(self):
        if self.head == None:
            print("Link List is empty")
        else:
            pointer = self.head
            string = f"" 
            while pointer != None:
                string += f" ( {pointer.data} ) -> "
                pointer = pointer.next
            print(f"{string} -> None " )
    
    def displayReverse(self,node):
        if self.head == None:
            print("Linked list is empty") # retern head
        else:
            if node.next == None:
                print(f"reverse Data is :: {node.data}")
            else:
                self.displayReverse(node.next)
                print(f"reverse Data is :: {node.data}")
    
    def sortLL(self):
        pass
                       
         
# LL1 = LinkedList()    

# #add New Nodes
# LL1.append("DATA 1")
# LL1.append("DATA 2")
# LL1.append("DATA 3")
# LL1.prepend("DATA 4")
# LL1.prepend("DATA 5")
# LL1.prepend("DATA 6")
# LL1.insertAtIndex("DATA 1000",2)
# LL1.insertAtIndex("DATA 2000",0)
# LL1.insertAtIndex("DATA 3000",8)




# LL1.displayAllValues()  
# LL1.at(2) # display value at index 2   
# LL1.tail()

# print("-------------1 display /\ value at index (2) /\ view tail node /\ /\ /\ ")
# print()
# print()
# #remove Node
# LL1.pop()
# LL1.truncate()
# LL1.displayAllValues()  
# print("-------------2 display /\ pop() /\ truncate() ")
# print()
# print()
# LL1.contain("DATA 3")
# LL1.toString()
# LL1.removeFrom(2)
# LL1.displayAllValues()
# print("------------- 3 display /\ contain(DATA 3) /\ to string /\ removefrom(2)")
# print()
# print()

# LL1.displayAllValues()
# LL1.displayReverse(LL1.head)



# arr = ["hello" , "my","name","is","iron","man"]
# LL2 = LinkedList()
# for i in arr:
#     LL2.append(i)
# LL2.displayAllValues()

LL3 = LinkedList()


