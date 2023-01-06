import numpy as np
import statistics as stat
import random
import characteristics_of_soldiers as cs
from enum import IntEnum


class RainDebuff(IntEnum):
    Rain_debuf = 0


class Rain:
    def __init__(self) -> None:
        self.dic_country_path = {'argentina': "weather/argentina.txt",
                                 'spain': "weather/espanna.txt"}
        self.dic_month_num = {'january': 0, "febraury": 1, "march": 2, "april": 3, " may": 4, "june": 5,
                              "july": 6, "august": 7, "september": 8, "october": 9, "november": 11, "december": 11}

    def calc_mean_var(self, country: str):
        path = ''
        if country not in self.dic_country_path.keys():
            mean = input("Valor de la media de las precipitaciones: ")
            var = input("Valor de la varianza de las precipitaciones: ")
            return mean, var
        else:
            path = self.dic_country_path[country]
        file = open(path, 'r')
        values = file.readlines()
        file.close()

        matrix_values = [[], [], [], [], [], [], [], [], [], [], [], []]
        for val in values:
            temp = val.split()
            for i in range(len(temp)):
                matrix_values[i].append(float(temp[i]))

        my_mean = []
        my_var = []
        for list_elem in matrix_values:
            my_mean.append(np.mean(list_elem))
        for list_elem in matrix_values:
            my_var.append(np.var(list_elem))

        return my_mean, my_var

    def get_rain_prob(self, mean, var, month):
        if month not in self.dic_month_num.keys():
            month = 'july'
        if type(mean) is list:
            v_a = stat.NormalDist(
                mean[self.dic_month_num[month]], var[self.dic_month_num[month]]**(1/2))
        else:
            month = random.randint(0, 11)
            v_a = stat.NormalDist(int(mean), int(var)**1/2)
        result = v_a.samples(1)
        return result

    def apply_debuf(self, soldier):
        for ch in soldier.characteristics:
            if isinstance(ch, cs.AdvantageousTerrain):
                return
        soldier.debuff.append(RainDebuff)
        soldier.speed = int(soldier.get_speed()) - 5
        soldier.attack = soldier.get_attack() - 3

    def remove_debuff(self, soldier):
        for deb in soldier.debuff:
            if isinstance(deb, RainDebuff):
                soldier.speed += 5
                soldier.attack += 3


# https://history.sacolife.com/45425/cual-es-la-edad-promedio-de-los-soldados-que-sirven-en-guerras-a-lo-largo-de-la-historia.html
# link de edades promedio de los soldados romanos
