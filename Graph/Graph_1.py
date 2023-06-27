class Graph():
    def __init__(self) -> None:
        self.graph = {}
    
    def addNode(self,node):
        if node in self.graph:
            print("Value Already exist!!!")
            return
        self.graph[node] = []
    
    def addEdge(self,v1,v2):
        if v1 not in self.graph or v2 not in self.graph:
            print("One of the node is not present ")
            return
        else:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)
    def deleteNode(self,node):
        if node not in self.graph:
            print("Value not found")
            return
        self.graph.pop(node)
        for i in self.graph:
            if node in self.graph[i]:
                self.graph[i].remove(node)
    def deleteEdge(self,v1,v2):
        if v1 not in self.graph or v2 not in self.graph:
            print("One of the node is not present ")
            return
        self.graph[v1].remove(v2)
        self.graph[v2].remove(v1)

graph = Graph()
# adding nodes
graph.addNode("A")
graph.addNode("B")
graph.addNode("C")
graph.addNode("D")
#adding edges 
graph.addEdge("A","B")
graph.addEdge("A","C")
graph.addEdge("A","D")
graph.addEdge("B","D")
# deleting node
graph.deleteNode("B")
# deleting edge
graph.deleteEdge("A","D")


print(graph.graph)
    