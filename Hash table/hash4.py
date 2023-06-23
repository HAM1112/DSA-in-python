class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.bucket_array = [None] * self.size
    def _hash_function(self, key):
        return hash(key) % self.size
    def insert(self, key, value):
        index = self._hash_function(key)
        if self.bucket_array[index] is None:
            node = Node(key, value)
            self.bucket_array[index] = node
        else:
            current = self.bucket_array[index]
            while current.next is not None:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            new_node = Node(key, value)
            current.next = new_node
    def get(self, key):
        index = self._hash_function(key)
        current = self.bucket_array[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None
    def remove(self, key):
        index = self._hash_function(key)
        current = self.bucket_array[index]
        previous = None
        while current is not None:
            if current.key == key:
                if previous is None:
                    # Node to remove is the head of the list
                    self.bucket_array[index] = current.next
                else:
                    # Node to remove is not the head of the list
                    previous.next = current.next
                return
            previous = current
            current = current.next

    def display(self):
        for index in range(self.size):
            current = self.bucket_array[index]
            while current is not None:
                print(f"Key: {current.key}, Value: {current.value}")
                current = current.next


# Usage example
hash_table = HashTable()
hash_table.insert("apple", 5)
hash_table.insert("banana", 7)
hash_table.insert("cherry", 10)
hash_table.insert("apple", 3)  # Updating value for existing key
hash_table.remove("banana")
hash_table.display()
