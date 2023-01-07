
import characteristics_of_soldiers
import statistics as stat
import random
from typing import List
from Battlefield import Camp
import armors
from goap.base_agent import Agent
import auxiliar
import math

class Soldier(Agent):
    """
    Clase soldado.
    """

    def __init__(self, pos_x, pos_y, army, *keys) -> None:
        super().__init__(*keys)
        self.life_points = 5000
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.army = army
        self.attack_range = 2
        self.attack = 60
        self.defense = 20
        self.speed = random.randrange(15, 50)
        self.energy = 100
        self.age = -1  # esto debe crearse con una variable aleatoria
        self.energy_regen = 35
        self.crit_porb = 0
        self.characteristics: List[characteristics_of_soldiers.Characteristics] = [
        ]
        self.debuff = []
        self.armor: armors.BassicArmor = None
        self.camp = None
        self.weapon_life = 100

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

    def get_speed(self):
        return self.speed

    def get_energy(self):
        return self.energy

    def incress_chance_crit(self, prob):
        self.crit_porb += prob

    def get_crit(self):
        return self.crit_porb

    def get_attack(self):
        return self.attack

    def get_range_attack(self):
        return self.attack_range

    def get_defense(self):
        return self.defense

    def use_armor(self):
        self.armor.dress_soldier(self)

    def restore_stats(self):
        self.attack = 60
        self.life_points = 250
        self.energy_regen = 35
        self.weapon_life = 150

    def check_enviroment(self, map):
        """
        Este metodo recibe el mapa del terreno y busca si en el rango de ataque de este soldado hay
        un enemigo para atacarlo. Cuando encuentra al primer oponente se detiene la busqueda y
        se decide atacar dicho soldado.

        Args:
            map (Map): Mapa de la simualcion
        """
        if self.weapon_life <= 0:
            self.set_start_state(in_camp=False, unarmed=True,
                                 fighting=False, looking_enemy=False, has_materials = False)
            cost_to_return_camp = self.calculate_variable_action_cost(map)
            if cost_to_return_camp == None:
                cost_to_return_camp = 1000
            self.add_weight('move_to_camp', cost_to_return_camp)
            self.set_goal_state(unarmed=False)

        elif self.found_oponent(map)[0]:
            self.planner.set_start_state(
                in_camp=False, unarmed=False, fighting=False, looking_enemy=True, has_materials = False)
        else:
            self.planner.set_start_state(
                in_camp=False, unarmed=False, fighting=False, looking_enemy=False, has_materials = False)

    def calculate_variable_action_cost(self,map):
        for camp in self.camp.n_cells:
            if map.get_battlefield()[camp[0]][camp[1]] == None:
                cost = math.fabs(self.pos_x - camp[0]) + math.fabs(self.pos_y - camp[1]) 
                return cost

    def found_oponent(self, map):  # Retorna tupla de si existe el oponente y su posicion

        for i in range(self.get_pos_x() - self.get_range_attack(), self.get_pos_x() + self.get_range_attack() + 1):
            for j in range(self.pos_y - self.get_range_attack(), self.pos_y + self.get_range_attack()):
                if i < 0 or j < 0:
                    continue
                if i >= map.get_row() or j >= map.get_col():
                    continue
                if map.battlefield[i][j]:
                    if not isinstance(map.battlefield[i][j], Camp) and map.battlefield[i][j].army != self.army and map.battlefield[i][j].life_points > 0:
                        return True, map.battlefield[i][j]

        return False, None

    def fight_to(self, map):

        # hallar el oponente
        other_soldier = self.found_oponent(map)[1]
        if other_soldier is None:
            return  # ! no hay oponente alcanzable
        #! mellar el arma

        self.weapon_life -= 25
        if self.weapon_life <= 0:
            self.attack = 0
            return
        #! tener en cuenta el critico y temate_supp
        crit = 0
        if self.get_crit() > 0:
            temp = random.random()
            if temp < self.get_crit():
                #print("viene critico!")
                crit = self.get_attack()
        if other_soldier.defense <= 0:
            other_soldier.life_points -= self.get_attack() + crit
            return
        if other_soldier.defense <= self.get_attack() + crit:
            other_soldier.life_points -= (self.get_attack() +
                                          crit - other_soldier.get_defense())
        other_soldier.defense -= self.get_attack()

    def move_soldier_(self, pos_x, pos_y, battlefield):
        if battlefield[pos_x][pos_y] != None:
            print("me movi para donde hay alguien, error")
        else:
            battlefield[pos_x][pos_y] = self
            battlefield[self.pos_x][self.pos_y] = None  # Desface
        self.pos_x = pos_x
        self.pos_y = pos_y

    def move_soldier(self, map):
        next_pos = auxiliar.bfs(map, self)
        if next_pos != None:
            self.move_soldier_(next_pos[0], next_pos[1], map.get_battlefield())

    def use_energy(self, new_pos):
        dist_manh = abs(self.get_pos_x() -
                        new_pos[0]) + abs(self.get_pos_y() - new_pos[1])
        return dist_manh * 15

    def recover_enery(self):
        self.energy += self.energy_regen

    def solider_age(self, mean=-1, var=-1) -> int:
        if mean == -1:
            mean = 32
        if var == -1:
            var = 12
        v = stat.NormalDist(mean, var)
        age = v.samples(1)
        if age[0] < 15:
            self.solider_age(mean, var)
        else:
            self.age = int(age[0])
            return age

    def return_to_camp(self, map):
        for camp in self.camp.n_cells:
            if map.get_battlefield()[camp[0]][camp[1]] == None:
                self.move_soldier_(camp[0], camp[1], map.get_battlefield())
                # print("REGRESE AL CAMPAMENTO")

    def restore_weapon(self,map):
        self.attack = 60
        self.weapon_life = 100
        self.set_start_state(in_camp=True, unarmed=False,
                             fighting=False, looking_enemy=False, has_materials= False)
        self.set_goal_state(fighting=True)

    def create_weapon(self,map):
        self.attack = 60
        self.weapon_life = 100
        self.set_start_state(in_camp=False, unarmed=False,
                             fighting=False, looking_enemy=False, has_materials= False)
        self.set_goal_state(fighting=True)    

    def pass_funtion(self,map):
        pass

    actionDict = {  # ! diccionario de acciones mapea las condiciones a los metodos correspondientes
        'move_to_camp': return_to_camp,
        'figth': fight_to,
        'move': move_soldier,
        'obtain_weapon': restore_weapon,
        'collect_materials': pass_funtion,
        'create_weapons' : create_weapon,
    }


def create_soldier(amount_of_soldier, army, map):
    """_summary_

    Args:
        amount_of_soldier (int): Cantidad de soldados que se desea crear
        army (str): Ejercito al que pertenecen los soldados a crear
        map (Map): Mapa de la simulacion

    Returns:
        List[Soldier]: Devuelve una lista con los soldados creadoss
    """
  

    soldiers = []
    if army == 1:
        army = 'A'
    if army == 2:
        army = 'B'
    for _ in range(amount_of_soldier):
        pos_x, pos_y = map.get_free_cell(army)
        if pos_x == None or pos_y == None:
            return -1
        temp = Soldier(pos_x, pos_y, army, 'in_camp',
                       'unarmed', 'fighting', 'looking_enemy','has_materials')

        temp.set_start_state(in_camp=False, unarmed=False,
                             fighting=False, looking_enemy=False, has_materials= False)
        temp.set_goal_state(fighting=True)
        temp.add_condition('move_to_camp', in_camp=False, unarmed=True)
        temp.add_reaction('move_to_camp', in_camp=True)
        temp.add_condition('figth', unarmed=False,
                           fighting=False, looking_enemy=True)
        temp.add_reaction('figth', fighting=True)
        temp.add_condition('move', unarmed=False,
                           fighting=False, looking_enemy=False)
        temp.add_reaction('move', looking_enemy=True)
        temp.add_condition('obtain_weapon', in_camp=True)
        temp.add_reaction('obtain_weapon', unarmed=False)
        temp.add_condition('collect_materials', in_camp= False, unarmed= True)
        temp.add_reaction('collect_materials', has_materials = True)
        temp.add_condition('create_weapons', has_materials = True )
        temp.add_reaction('create_weapons', unarmed = False)
        temp.add_weight('create_weapons', 10) # Costo fijo
        temp.add_weight('collect_materials', 4) #Si pongo materiales costo variable
        temp.set_action_list()

        v_a = characteristics_of_soldiers.Experience()
        temp.solider_age()
        v_a.apply_buff(temp)
        soldiers.append(temp)
        map.battlefield[pos_x][pos_y] = temp

    return soldiers
