class TriNode():
    def __init__(self) -> None:
        self.children = {}
        self.endOfWord = False

class Trie():
    def __init__(self) -> None:
        self.root = TriNode()
    
    def insert(self, word):
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TriNode()
            node = node.children[char]
        node.endOfWord = True
    
    def search(self,word):
        node = self.root
        
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.endOfWord
    
        

trie = Trie()
trie.insert("hello")
print(trie.search("hello"))
