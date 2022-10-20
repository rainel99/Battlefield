#direct_array: N,S,E,W,NW,NE,SW,SE
directions_row = [-1,1,0,0,-1,-1,1,1]
directions_col = [0,0,1,-1,-1,1,-1,1]


def bfs(visit_complete, graph, current_node,soldier):
    visit_complete.append(current_node)
    queue = []
    queue.append(current_node)

    while queue:
        s = queue.pop(0)
        print(s)

        for neighbour in graph[s]:
            if neighbour not in visit_complete:
                visit_complete.append(neighbour)
                queue.append(neighbour)


def neighbour(map, soldier):
    for dir in directions_row:
        new_row = soldier.get_row() + directions_row() 
        new_col = soldier.get_col() + directions_col() 
        if new_row < map.get_row() and new_col < map.get_col():
            return