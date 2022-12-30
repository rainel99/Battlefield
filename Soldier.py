
import characteristics_of_soldiers
import statistics as stat
import random
from typing import List
from Battlefield import Camp, Map
import armors


class Soldier():
    """
    Clase soldado.
    """

    def __init__(self, pos_x, pos_y, army) -> None:
        self.life_points = 250
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

    def attack_strategy_one(self, map):
        """
        Este metodo recibe el mapa del terreno y busca si en el rango de ataque de este soldado hay
        un enemigo para atacarlo. Cuando encuentra al primer oponente se detiene la busqueda y 
        se decide atacar dicho soldado.

        Args:
            map (Map): Mapa de la simualcion
        """
        found_oponent = False
        for i in range(self.get_pos_x() - self.get_range_attack(), self.get_pos_x() + self.get_range_attack() + 1):
            if found_oponent:
                return found_oponent
            for j in range(self.pos_y - self.get_range_attack(), self.pos_y + self.get_range_attack()):
                if i < 0 or j < 0:
                    break
                if i >= map.get_row() or j >= map.get_col():
                    break
                if map.battlefield[i][j]:
                    if not isinstance(map.battlefield[i][j], Camp) and map.battlefield[i][j].army != self.army and map.battlefield[i][j].life_points > 0:
                        self.fight_to(map.battlefield[i][j])
                        found_oponent = True
                        break

    def fight_to(self, other_soldier):
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

    def move_soldier(self, pos_x, pos_y, battlefield):
        if battlefield[pos_x][pos_y] != None:
            print("me movi para donde hay alguien, error")
        else:
            battlefield[pos_x][pos_y] = self
            battlefield[self.pos_x][self.pos_y] = None  # Desface
        self.pos_x = pos_x
        self.pos_y = pos_y

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
                self.move_soldier(camp[0], camp[1], map.get_battlefield())
                print("REGRESE AL CAMPAMENTO")


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
    for _ in range(amount_of_soldier):
        pos_x, pos_y = map.get_free_cell(army)
        if pos_x == None and pos_y == None:
            return -1
        temp = Soldier(pos_x, pos_y, army)
        v_a = characteristics_of_soldiers.Experience()
        temp.solider_age()
        v_a.apply_buff(temp)
        soldiers.append(temp)
        map.battlefield[pos_x][pos_y] = temp

    return soldiers
