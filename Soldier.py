


import random
from typing import List
from Battlefield import Map


class Soldier():
    """
    Clase soldado.
    """
    def __init__(self, pos_x, pos_y, army) -> None:
        self.life_points = 100
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.army = army
        self.attack_range = 2
        self.attack = 60
        self.defense = 20
        self.speed = random.randrange(15,50)
        self.energy = 100
        self.age = 30  #esto debe crearse con una variable aleatoria
        self.energy_regen = 35

    def get_life_points(self):
        return self.life_points
    
    def get_pos_x(self):
        return self.pos_x

    def get_pos_y(self):
        return self.pos_y
    
    def get_army(self):
        return self.army

    def __str__(self) -> str:
        return str(self.army)

    def __repr__(self) -> str:
        return self.__str__()


    def get_energy(self):
        return self.energy


    def attack_strategy_one(self,map):
        """
        Este metodo recibe el mapa del terreno y busca si en el rango de ataque de este soldado hay
        un enemigo para atacarlo. Cuando encuentra al primer oponente se detiene la busqueda y 
        se decide atacar dicho soldado.

        Args:
            map (Map): Mapa de la simualcion
        """
        found_oponent = False
        for i in range(self.pos_x - self.attack_range,self.pos_x + self.attack_range + 1):
            if found_oponent :
                return found_oponent
            for j in range(self.pos_y - self.attack_range, self.pos_y + self.attack_range):
                if i < 0 or j < 0:
                    break
                if i >= map.get_row() or j >= map.get_col():
                    break
                if map.battlefield[i][j]:
                    if map.battlefield[i][j].army != self.army and map.battlefield[i][j].life_points > 0 :
                        self.fight_to(map.battlefield[i][j])
                        found_oponent = True
                        break


    def fight_to(self,other_soldier):
        if other_soldier.defense <= 0:
            other_soldier.life_points -= self.attack
            return
        if other_soldier.defense <= self.attack:
            other_soldier.life_points -= (self.attack - other_soldier.defense)
        other_soldier.defense -= self.attack


            
    def move_soldier(self,pos_x, pos_y,battlefield):
        if battlefield[pos_x][pos_y] != None:
            print("me movi para donde hay alguien, error")
            # print(self.pos_x,self.pos_y,"Donde estoy")
            # print(pos_x,pos_y,"A donde quiero ir ")
            # print(battlefield[pos_x][pos_y],"Lo q hay donde quiero ir ")
            # print(battlefield)
        else:
            battlefield[pos_x][pos_y] = self
            battlefield[self.pos_x][self.pos_y] = None #Desface
        self.pos_x = pos_x
        self.pos_y = pos_y

    def use_energy(self, new_pos):
        dist_manh = abs(self.get_pos_x() - new_pos[0]) + abs(self.get_pos_y() - new_pos[1])
        return dist_manh * 15
                
                
    def recover_enery(self):
        self.energy+= self.energy_regen


    
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
        pos_x,pos_y = map.get_free_cell(army)
        if pos_x == None and pos_y == None:
            return -1
        temp = Soldier(pos_x,pos_y,army)
        soldiers.append(temp)
        map.battlefield[pos_x][pos_y] = temp

    return soldiers



