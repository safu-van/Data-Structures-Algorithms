# Weighted Graph & Undirected Graph

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
                for list in values:
                    if list[0] == vertex:
                        values.remove(list)
                        break
    
    # to add edge
    def add_edge(self, vertex_1, vertex_2, weight):
        if vertex_1 not in self.graph:
            self.add_vertex(vertex_1)

        if vertex_2 not in self.graph:
            self.add_vertex(vertex_2)
        
        self.graph[vertex_1].append([vertex_2, weight])
        self.graph[vertex_2].append([vertex_1, weight])

    # to remove edge
    def remove_edge(self, vertex_1, vertex_2, weight):
        if vertex_1 not in self.graph:
            print(vertex_1, " not found in the graph")
        elif vertex_2 not in self.graph:
            print(vertex_2, " not found in the graph")
        else:
            edge_1 = [vertex_1, weight]
            edge_2 = [vertex_2, weight]
            if edge_2 in self.graph[vertex_1]:
                self.graph[vertex_1].remove(edge_2)
                self.graph[vertex_2].remove(edge_1)
    
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
graph.add_vertex("d")
graph.add_edge("a", "b", 10)
graph.add_edge("b", "d", 10)
graph.add_edge("d", "c", 10)
graph.add_edge("c", "a", 10)
graph.display()
