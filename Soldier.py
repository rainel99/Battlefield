


import random
from typing import List

from Battlefield import Map


class Soldier():
    def __init__(self, pos_x, pos_y, army) -> None:
        self.life_points = 100
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.army = army

    def get_life_points(self):
        return self.life_points
    
    def get_pos_x(self):
        return self.pos_x

    def get_pos_y(self):
        return self.pos_y
    
    def get_army(self):
        return self.army

def create_soldier(amount_of_soldier, army ,map):
    """_summary_

    Args:
        amount_of_soldier (int): Cantidad de soldados que se desea crear
        army (str): Ejercito al que pertenecen los soldados a crear
        map (Map): Mapa de la simulacion

    Returns:
        List[Soldier]: Devuelve una lista con los soldados creadoss
    """
    soldiers = []
    for _ in range(amount_of_soldier):
        pos_x,pos_y = map.get_free_cell()
        if pos_x == None and pos_y == None:
            return -1
        temp = Soldier(pos_x,pos_y,army)
        soldiers.append(temp)
        map.battlefield[pos_x][pos_y] = temp

    return soldiers
