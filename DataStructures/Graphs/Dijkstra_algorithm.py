from priority_queue import priority_queue
from adjacency_list import Graph,Vertex

def dijkstra(agraph,start):
    """given agraph and a starting node, finds the shortest
    path to all other nodes from the starting node(start)"""
    pq = priority_queue()
    start.set_distance(0)
    pq.build_heap([(v.get_distance(),v) for v in agraph])
    while not pq.is_empty():
        current_vert = pq.delete_min()
        for next_vert in current_vert.get_connections():
            new_dist = current_vert.get_distance() + current_vert.get_weight(next_vert)
            if new_dist < next_vert.get_distance():
                next_vert.set_distance(new_dist)
                next_vert.set_pred(current_vert)
                pq.decrease_key(next_vert,new_dist)