class Hash:
    def __init__(self, size):
        self.table = [None] * size
        self.size = size
    
    def hashkey(self, key):
        total = 0
        for i in range(len(key)):
            total += ord(key[i])
        return total % self.size
    
    def set(self, key, value):
        index = self.hashkey(key)
        if self.table[index] is None:
            self.table[index] = []
        for i in range(len(self.table[index])):
            if self.table[index][i][0] == key:
                self.table[index][i][1] = value
                return
        self.table[index].append([key, value])
    
    def display(self):
        for i in range(self.size):
            if self.table[i] is not None:
                print(i, self.table[i])
                
hash = Hash(50)
hash.set("name", "shakil")
hash.set("house", "wayanad")
hash.set("mane", "hai")
hash.display()

