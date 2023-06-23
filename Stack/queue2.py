class Queue():
    def __init__(self,limit):
        self.queue = []
        self.size = 0
        self.limit = limit
    
    def enque(self,val):
        full = self.isFull()
        if full:
            print("Queue is Full")
            return
        self.queue.insert(0,val)
        self.size += 1
    
    def deque(self):
        empty = self.isEmpty()
        if empty :
            print("Queue is Full")
            return
        self.queue.pop()
        self.size -= 1
        
    def isEmpty(self):
        if self.size == 0:
            return True
        return False
    
    def isFull(self):
        if self.size == self.limit:
            return True
        return False
    def display(self):
        print(self.queue)

queue = Queue(10)
queue.enque(10)
queue.enque(30)
queue.enque(40)
queue.enque(20)
queue.enque(50)
queue.display()
queue.deque()    
queue.display()