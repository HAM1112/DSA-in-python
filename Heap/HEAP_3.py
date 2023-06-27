class MaxHeap():
    def __init__(self) -> None:
        self.heap = []
    # insert value
    def insert(self, val):
        self.heap.append(val)
        self.bubbleup(len(self.heap)-1)
    
    #heapify up
    def bubbleup(self,index):
        if index == 0:
            return
        parent = (index - 1) // 2
        if self.heap[index] > self.heap[parent]:
            self.heap[index],self.heap[parent] = self.heap[parent] ,self.heap[index]
            self.bubbleup(parent)
    
    # delete a value
    def delete(self,val):
        if val not in self.heap:
            print("value not found")
            return
        index = self.heap.index(val)
        self.heap.pop(index)
        parent = (index - 1 ) // 2
        self.bubbleup(parent)
        self.heapify(0)
    
    #heapify down
    def heapify(self,index):
        l = (index * 2) + 1
        r = (index * 2) + 2
        large = index
        
        if l < len(self.heap) and self.heap[index] < self.heap[l]:
            large = l
        if r < len(self.heap) and self.heap[large] < self.heap[r]:
            large = r
        
        if large != index:
            self.heap[large] , self.heap[index] = self.heap[index] , self.heap[large]
            self.heapify(large)
        
    # extract the max value in heap 
    def extractMax(self):
        maxval = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify(0)
        return maxval
    
heap = MaxHeap()
heap.insert(40)
heap.insert(30)
heap.insert(50)
heap.insert(80)
heap.insert(90)
heap.insert(10)
heap.insert(100)
print(heap.heap)
print(heap.extractMax())
print(heap.heap)
heap.delete(30)
print(heap.heap)