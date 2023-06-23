class Hash():
    def __init__(self,size):
        self.size = size
        self.table = [None] * size
    
    def hash(self,key):
        total = 0
        for i in key:
            total += ord(i)
        # print(f"{total % self.size} line 10")
        return total % self.size
    def set(self,key,value):
        index = self.hash(key)
        if self.table[index] is None:
            self.table[index] = []
            
        for i in range(len(self.table[index])):
            if self.table[index][i][0] == key:
                self.table[index][i][1] = value
        
        self.table[index].append([key,value])
    
    def display(self):
        for i in range(self.size):
            if self.table[i] is not None:
                print(self.table[i])
                
    def get(self,key):
        index = self.hash(key)
        
        if self.table[index] is not None:
            for i in range(len(self.table[index])):
                if self.table[index][i][0] == key:
                    print(f"value with key {key} is : {self.table[index][i][1]}")
                    return
        
        print("key Not Found")
        return
            
hash1 = Hash(20)
hash1.set("harry","brave")
hash1.set("hermonie","knowledge")
hash1.set("ron","trustworthy")
hash1.set("hagrid","keeper")
hash1.set("draco","bully")
hash1.set("snape","caring")
hash1.display()
print()
print("searching")
print()
hash1.get("hermonie")


