from pythonds.graphs import Graph, Vertex
from pythonds.basic import Queue

def bfs(graph,start):
    """Given a graph and a start node,
    performs a breadth first search, adding
    distance from the start and predecessors to
    the vertices"""
  start.setDistance(0)
  start.setPred(None)
  vert_queue = Queue()
  vert_queue.enqueue(start)
  while (vert_queue.size() > 0):
    current_vert = vert_queue.dequeue()
    for neighbor in current_vert.getConnections():
      if (neighbor.getColor() == 'white'):
        neighbor.setColor('gray')
        neighbor.setDistance(current_vert.getDistance() + 1)
        neighbor.setPred(current_vert)
        vert_queue.enqueue(neighbor)
    current_vert.setColor('black')