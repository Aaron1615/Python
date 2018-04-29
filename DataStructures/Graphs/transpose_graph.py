from adjacency_list import Graph,Vertex

def transpose_graph(graph):
    """Returns a transposed version of the graph input"""
    transposed = Graph()
    for key in graph.get_vertices():
        if not transposed.get_vertex(key):
            transposed.add_vertex(key)
        for neighbor in graph.get_vertex(key).get_connections():
            if not transposed.get_vertex(neighbor):
                transposed.add_vertex(neighbor.get_id())
            transposed.add_edge(neighbor.get_id(),key)
    return transposed  
