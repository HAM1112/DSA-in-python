class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty.")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty.")

    def size(self):
        return len(self.items)
queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Size:", queue.size())  # Output: Size: 3
print("Front element:", queue.front())  # Output: Front element: 1

item = queue.dequeue()
print("Dequeued item:", item)  # Output: Dequeued item: 1

print("Is queue empty?", queue.is_empty())  # Output: Is queue empty? False
