class Stack():
    def __init__(self):
        self.stack = []
        self.size = 0
    
    def push(self,val):
        self.stack.append(val)
        self.size += 1
    
    def pop(self):
        self.stack.pop()
        self.size -= 1
    
    def display(self):
        print(self.stack)
    
    def displaySize(self):
        print(f"Size = {self.size}")
    
    def peek(self):
        print(self.stack[self.size-1])

    def middle(self):
        print(self.size//2)
        for i in range(self.size//2):
            self.stack.pop()
            self.size -= 1 
        self.peek()
            
            
ST = Stack()
ST.push(4)
ST.push(7)
ST.push(2)
ST.push(7)
ST.push(1)
ST.push(3)
ST.push(9)
ST.push(9)
ST.push(1)
ST.display()
ST.displaySize()
ST.middle()