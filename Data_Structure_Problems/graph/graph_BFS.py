# Graph BFS (Breadth First Search)

class Graph:
    def __init__(self):
        self.graph = {}
    
    # to add vertex
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    # to add edge
    def add_edge(self, vertex_1, vertex_2):
        if vertex_1 not in self.graph:
            self.add_vertex(vertex_1)
        
        if vertex_2 not in self.graph:
            self.add_vertex(vertex_2)
        
        self.graph[vertex_1].append(vertex_2)
        self.graph[vertex_2].append(vertex_1)
    
    # BFS implementation
    def bfs(self, start_vertex):
        visited = set()
        
        queue = []
        queue.append(start_vertex)
        visited.add(start_vertex)

        while len(queue) > 0:
            current_vertex = queue.pop(0)
            print(current_vertex)

            for adjacent_node in self.graph[current_vertex]:
                if adjacent_node not in visited:
                    visited.add(adjacent_node)
                    queue.append(adjacent_node)


graph = Graph()

graph.add_vertex("a")
graph.add_vertex("b")
graph.add_vertex("c")
graph.add_vertex("d")
graph.add_vertex("e")

graph.add_edge("a", "b")
graph.add_edge("b", "c")
graph.add_edge("c", "d")
graph.add_edge("d", "e")
graph.add_edge("e", "a")

graph.bfs("a")