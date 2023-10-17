class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        self.vertices[vertex] = []
    
    def add_edge(self, source, target):
        self.vertices[source].append(target)

my_graph = Graph()
my_graph.add_vertex('Lonika')
my_graph.add_vertex('Molina')
my_graph.add_vertex('Kristina')

my_graph.add_edge('Lonika', 'Molina')
my_graph.add_edge('Lonika', 'Kristina')
my_graph.add_edge('Kristina', 'Molina')

print(my_graph.vertices)