class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex, edge, is_bidirectional):
        if vertex not in self.graph:
            self.graph[vertex] = []
        
        if edge not in self.graph:
            self.graph[edge] = []

        self.graph[vertex].append(edge)
        if is_bidirectional:
            self.graph[edge].append(vertex)
    
    def delete_vertex(self, vertex):
        if vertex not in self.graph:
            print(vertex, " not found")
        else:
            del self.graph[vertex]
            for key in self.graph:
                values = self.graph[key]
                if vertex in values:
                    values.remove(vertex)
    
    def display(self):
        for key, values in self.graph.items():
            print(key, end=" : ")
            for value in values:
                print(value, end=" ")
            print()
        
graph = Graph()
graph.add_vertex(3, 5, True)
graph.add_vertex(3, 4, True)
graph.add_vertex(5, 6, False)
graph.display()
print("-------------")
graph.delete_vertex(3)
graph.display()