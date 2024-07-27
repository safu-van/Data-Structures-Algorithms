class Graph:
    def __init__(self):
        self.map = {}
    
    def add_vertex(self, vertex, edge, is_bidirectional):
        if vertex not in self.map:
            self.map[vertex] = []
        
        if edge not in self.map:
            self.map[edge] = []

        self.map[vertex].append(edge)
        if is_bidirectional:
            self.map[edge].append(vertex)
    
    def display(self):
        for key, values in self.map.items():
            print(key, end=" :")
            for value in values:
                print(value, end=" ")
            print()
        
graph = Graph()
graph.add_vertex(3, 5, True)
graph.add_vertex(3, 4, True)
graph.add_vertex(5, 6, False)
graph.display()