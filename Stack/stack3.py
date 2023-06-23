class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty.")
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty.")

    def size(self):
        return len(self.items)
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Size:", stack.size())  # Output: Size: 3
print("Top element:", stack.peek())  # Output: Top element: 3
item = stack.pop()
print("Popped item:", item)  # Output: Popped item: 3
print("Is stack empty?", stack.is_empty())  # Output: Is stack empty? False
