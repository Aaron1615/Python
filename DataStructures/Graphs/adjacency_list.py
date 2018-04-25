import sys

class Vertex:
    """Vertex object which tracks which other vertices
    it is connected to along with the weights of the 
    edges between them"""
    
    def __init__(self,key):
        self.id = key
        self.connected_to = {}
        self.dist = sys.maxsize
        self.color = "white"
        self.pred = None

    
    def add_neighbor(self,neighbor,weight=0):
        """Adds an edge between the vertex and another
        vertex (neighbor)"""
        self.connected_to[neighbor] = weight
    
    def __str__(self):
        return str(self.id) + ' connected to: ' + str([x.id for x in self.connected_to])
    
    def set_color(self, color):
        """sets the color of the vertex"""
        self.color = color
    
    def set_distance(self,d):
        """sets the distance of the vertex"""
        self.dist = d
    
    def set_pred(self,p):
        """sets the predecesor of the vertex"""
        self.pred = p

    def get_pred(self):
        """returns the predecesor of the vertex"""
        return self.pred
        
    def get_distance(self):
        """returns the distance of the vertex"""
        return self.dist
        
    def get_color(self):
        """returns the color of the vertex"""
        return self.color
    
    def get_connections(self):
        """Returns the vertices to which the vertex
        is connected"""
        return self.connected_to.keys()
    
    def get_id(self):
        """Returns the key of the vertex"""
        return self.id
    
    def get_weight(self,neighbor):
        """Given a neighboring vertex (neighbor) returns 
        the weight of the edge between the two"""
        return self.connected_to[neighbor]

class Graph:
    """An object which maps vertex names to their corresponding
    vertex objects"""
    def __init__(self):
        self.vertice_list = {}
        self.num_vertices = 0

    def add_vertex(self,key):
        """Adds a new vertex to the Graph"""
        self.num_vertices +=1
        new_vertex = Vertex(key)
        self.vertice_list[key] = new_vertex
        return new_vertex

    def get_vertex(self,name):
        """Returns the vertex object of the corresponding
        name if it exists."""
        if name in self.vertice_list:
            return self.vertice_list[name]
        else:
            return None

    def __contains__(self,name):
        return name in self.vertice_list

    def add_edge(self,vertex_1,vertex_2,cost=0):
        """Adds an edge of a specified weight(cost)
        between two vertices"""
        if vertex_1 not in self.vertice_list:
            self.add_vertex(vertex_1)
        if vertex_2 not in self.vertice_list:
            self.add_vertex(vertex_2)
        self.vertice_list[vertex_1].add_neighbor(self.vertice_list[vertex_2], cost)

    def get_vertices(self):
        """Returns the names of all vertices in the graph"""
        return self.vertice_list.keys()

    def __iter__(self):
        return iter(self.vertice_list.values())
