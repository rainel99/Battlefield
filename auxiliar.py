#direct_array: N,S,E,W,NW,NE,SW,SE
from Soldier import Soldier
import re

directions_row = [-1,1,0,0,-1,-1,1,1]
directions_col = [0,0,1,-1,-1,1,-1,1]


def bfs(visit_complete, map, current_node,soldier):
    # graph = map.copy()
    pi = {}
    queue = []
    queue.append(current_node)

    while queue:
        s = queue.pop(0)
        visit_complete.append(s)
        if map[s[0]][s[1]] != None and map[s[0]][s[1]].army != soldier.army: #encontre un soldado del ejercito contrario
            return pi

        for ne in neighbour(map,soldier):
            if ne not in visit_complete:
                pi[ne] = s
                queue.append(ne)
    
    return pi


def neighbour(map, soldier):
    result = []
    for dir in range(len(directions_row)):
        new_row = soldier.get_pos_x() + directions_row[dir] 
        new_col = soldier.get_pos_y() + directions_col[dir]
        if new_row < len(map) and new_col < len(map[0]) and new_row >= 0 and new_col >= 0:
            result.append((new_row,new_col))
    return result


s1 = Soldier(0,3,'A')
s2 = Soldier(1,1,'B')
graph = [[None,None,None,s1]
        ,[None,s2,None,None]
        ,[None,None,None,None]
        ,[None,None,None,None]]

#print(len(graph), len(graph[0]))

dic = bfs([],graph,(0,3),s1)
#print(neighbour(graph,s1))
print(dic[(s1.get_pos_x(),s1.get_pos_y())])























































