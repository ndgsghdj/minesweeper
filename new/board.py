class Tile: 
    def __init__(self, n):
        self.name = n
        self.neighbours = list()
    
    def add_neighbour(self, v, weight):
        if v not in self.neighbours:
            self.neighbours.append(v, weight)
            self.neighbours.sort()

class Board:
    vertices = {}

    def add_vertex(self, u, v, weight=0):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].add_neighbour(v, weight)
            self.vertices[u].add_neighbour(u, weight)
            return True
        else: 
            return False
    
    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbours))