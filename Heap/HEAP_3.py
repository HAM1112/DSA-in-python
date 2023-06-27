class MaxHeap():
    def __init__(self) -> None:
        self.heap = []
    
    def insert(self,val):
        self.heap.append(val)
        self.bubbleup(len(self.heap)-1)
        
    
    def bubbleup(self,index):
        if index ==0:
            return 
        parent = (index -1) // 2
        
        if self.heap[index] > self.heap[parent]:
            self.heap[index] , self.heap[parent] = self.heap[parent] , self.heap[index]
            self.bubbleup(parent) 