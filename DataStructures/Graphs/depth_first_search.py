from adjacency_list import Graph,Vertex

class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0
    
    def DFS(self):
        for a_vertex in self:
            a_vertex.set_color("white")
            a_vertex.set_pred(-1)
        for a_vertex in self:
            if a_vertex.get_color() == "white":
                self.DFSvisit(a_vertex)

    def DFSvisit(self,start_vertex):
        start_vertex.set_color("gray")
        self.time += 1
        start_vertex.set_discovery(self.time)
        for next_vertex in start_vertex.get_connections():
            if next_vertex.get_color() == "white":
                next_vertex.set_pred(start_vertex)
                self.DFSvisit(next_vertex)
        start_vertex.set_color("black")
        self.time += 1
        start_vertex.set_finish(self.time)
