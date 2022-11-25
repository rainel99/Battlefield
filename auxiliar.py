#direct_array:   N,S,E,W,NW,NE,SW,SE

directions_row = [-1,1,0,0]
directions_col = [0,0,1,-1]
import time
from Soldier import Soldier



def fix_axes(iterations, soldiers_A,soldiers_B):
    temp_A = soldiers_A[len(soldiers_A) - 1]
    while len(iterations) != len(soldiers_A):
        soldiers_A.append(temp_A)
    temp_B = soldiers_B[len(soldiers_B) - 1]
    while len(iterations) != len(soldiers_B):
        soldiers_B.append(temp_B)


def bfs(map,soldier):
    visit_complete = []
    my_queue = []
    current_node  = (soldier.get_pos_x(),soldier.get_pos_y())
    my_queue.append(current_node)
    initial_pos = (soldier.get_pos_x(),soldier.get_pos_y())
    while my_queue:
        current_node = my_queue.pop(0)
        visit_complete.append(current_node)
        for i in range(len(directions_col)):
            new_row = current_node[0] + directions_row[i] 
            new_col = current_node[1] + directions_col[i]
            if in_range(new_row,new_col,len(map),len(map[0])) and (new_row,new_col) not in visit_complete and (new_row,new_col) not in my_queue :
                if map[new_row][new_col] != None and map[new_row][new_col].army != soldier.army and current_node != initial_pos:
                    return current_node
                if map[new_row][new_col] == None:
                    my_queue.append((new_row,new_col))


def in_range(new_r,new_c, len_map_r,len_map_c):
    if new_r < len_map_r and new_c < len_map_c and new_r >= 0 and new_c >= 0:
        return True
    return False

# a = Soldier(0,0,'A')
# b = Soldier(4,3,'B')
# graph = [[None]*5 for _ in range(5)]
# graph[0][0] = a
# graph[4][3] = b
# output = bfs(graph,a)
# print(output)


# print(abs(a.get_pos_x() - output[0]) + abs(a.get_pos_y() - output[1]))




















































