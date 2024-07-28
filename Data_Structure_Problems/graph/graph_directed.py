# Directed Graph

class Graph:
    def __init__(self):
        self.graph = {}
    
    # to add vertex
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    # to delete vertex
    def delete_vertex(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]

            for key in self.graph:
                values = self.graph[key]
                if vertex in values:
                    values.remove(vertex)
    
    # to add edge
    def add_edge(self, vertex_1, vertex_2):
        if vertex_1 not in self.graph:
            self.add_vertex(vertex_1)
        
        if vertex_2 not in self.graph:
            self.add_vertex(vertex_2)
        
        self.graph[vertex_1].append(vertex_2)
    
    # to remove edge
    def remove_edge(self, vertex_1, vertex_2):
        if vertex_1 not in self.graph:
            print(vertex_1, " not found in the graph")
        elif vertex_2 not in self.graph:
            print(vertex_2, " not found in the graph")
        else:
            if vertex_2 in self.graph[vertex_1]:
                self.graph[vertex_1].remove(vertex_2)
            else:
                print(f"edge not found between {vertex_1} & {vertex_2}")

    def display(self):
        for key, values in self.graph.items():
            print(key, end=" : ")
            for value in values:
                print(value, end=" ")
            print()


graph = Graph()
graph.add_vertex("a")
graph.add_vertex("b")
graph.add_vertex("c")
graph.add_edge("a", "b")
graph.add_edge("a", "c")
graph.display()

