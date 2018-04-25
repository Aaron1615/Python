from adjacency_list import Graph

def knight_graph(board_size):
    kt_graph = Graph()
    for row in range(board_size):
        for col in range(board_size):
            node_id = position_to_node_id(row,col,board_size)
            new_positions = generate_legal_moves(row,col,board_size)
            for move in new_positions:
                new_id = position_to_node_id(move[0],move[1],board_size)
                kt_graph.add_edge(node_id,new_id)
        return kt_graph
def position_to_node_id(row,column,board_size):
    return (row * board_size) + column

def generate_legal_moves(x,y,board_size):
    new_moves = []
    move_offstes = [(-1,-2),(-1,2),(-2,-1),(-2,1),(1,-2),(1,2),(2,-1),(2,1)]
    for i in move_offstes:
        new_x = x + i[0]
        new_y = y + i[1]
        if legal_coordinate(new_x,board_size) and legal_coordinate(new_y,board_size):
            new_moves.append((new_x,new_y))
        return new_moves

def legal_coordinate(x,board_size):
    if x >=0 and x < board_size:
        return True
    else:
        return False

def knight_tour(number,path,current,limit):
    current.set_color("gray")
    path.append(current)
    
    if number < limit:
        neighbor_list = list(current.get_connections())
        i = 0
        done = False

        while i < len(neighbor_list) and not done:        
            if neighbor_list[i].get_color() == "white":
                done = knight_tour(number + 1, path,neighbor_list[i], limit)
            i = i + 1
    
        if not done:
            path.pop()
            current.set_color("white")
    
    else:
        done = True
    return done
