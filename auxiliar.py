#direct_array:   N,S,E,W,NW,NE,SW,SE
directions_row = [-1,1,0,0]
directions_col = [0,0,1,-1]


def bfs(map, current_node,soldier):
    # graph = map.copy()
    visit_complete = []
    pi = {}
    queue = []
    queue.append(current_node)
    pos_dest = None
    

    while queue:
        s = queue.pop(0)
        visit_complete.append(s)
        if map[s[0]][s[1]] != None and map[s[0]][s[1]].army != soldier.army: #encontre un soldado del ejercito contrario
            pos_dest = (s[0],s[1])
            return build_way_back(pi,pos_dest,(soldier.get_pos_x(),soldier.get_pos_y()))

        for ne in neighbour(map,s):
            if ne not in visit_complete:
                pi[ne] = s
                queue.append(ne)
    return None

def neighbour(map, cel):
    #devuelve las lista de los adyacentes a una posicion dada
    result = []
    for dir in range(len(directions_row)):
        new_row = cel[0] + directions_row[dir] 
        new_col = cel[1] + directions_col[dir]
        if new_row < len(map) and new_col < len(map[0]) and new_row >= 0 and new_col >= 0:
            result.append((new_row,new_col))
    return result

def build_way_back(dict , pos_dest, pos_start):
    result = []
    current = pos_dest
    result.append(pos_dest)
    while current != pos_start:
        current = dict[current]
        result.append(current)
    result= result[::-1]
    if len(result) > 1:
        return result[1]
    return result[0]


























































