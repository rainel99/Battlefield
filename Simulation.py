from math import inf
from Soldier import *
from Battlefield import *
import Graph_simulation
import auxiliar
import random as rd
from characteristics_of_soldiers import all_characteristics, EnumAttribute
from weather import stats as weather
from armors import armors, dress_army, dress_army_variant_b, min_price
import gen_algorithm as ga
from colorama import Fore
import pickle


def start_simulation(map_rows, map_cols, amount_army_a, amount_army_b, rounds, gen):
    arms = armors
    start_price = ((amount_army_a + amount_army_b) // 3) * 30
    # !revisar bien esto!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    soldiers: List[Soldier] = []
    visits = amount_army_a // 3
    map = Map(map_rows, map_cols, visits)  # mapa de la simulacion
    army_a = create_soldier(amount_army_a, 'A', map)
    __arms = gen[3:]
    dress_army_variant_b(army_a, __arms, arms)
    # dress_army(army_a, start_price, min_price.price)
    army_b = create_soldier(amount_army_b, 'B', map)
    dress_army(army_b, start_price, min_price.price)
    auxiliar.marge_armys(army_a, army_b, soldiers)
    asign_camps_to_soldiers(soldiers, map.get_camps())
    check_possition(soldiers, map.camps, map)
    # se ordenan los soldados de ambos ejercitos segun su velocidad
    soldiers.sort(key=lambda soldier: soldier.speed, reverse=True)
    soldiers_a = []
    soldiers_b = []
    # aqui estamos anhadiendo caracteristicas a los soldados, 3 por soldado
    __charact = gen[:3]
    add_charact_variat_b(army_a, __charact)
    #add_soldiers_characteristics(army_a, 3)
    add_soldiers_characteristics(army_b, 3)

    # a partir de la region seleccionada y la fecha => generar una v_a para las precipitaciones
    rain = weather.Rain()
    # para testear se elejira como pais espanha y mes julio
    country = "spain"
    month = "july"
    # country = input("spain o argentina: ")
    # month = input("print a month of the year: ")

    mean, var = rain.calc_mean_var(country)
    iterations = [i for i in range(rounds)]
    print("Mapa inicial:")
    print_map(map)
    print('\n')
    while rounds > 0:
        rain_mm = rain.get_rain_prob(mean, var, month)
        if rain_mm[0] > 50:
            for sol in soldiers:
                rain.apply_debuf(sol)

        soldiers_a, soldiers_b = Graph_simulation.count_soldiers_alive(
            soldiers_a, soldiers_b, map)
        for soldier in soldiers:
            if soldier.weapon_life <= 0:
                if soldier.camp.state == True:
                    soldier.return_to_camp(map)
                    continue
            else:
                attacked = soldier.attack_strategy_one(map)
                if not attacked:
                    next_pos = auxiliar.bfs(map.get_battlefield(), soldier)
                    if next_pos != None:
                        # !!!!! aqui voy a cambiar cosas pa q si tienen energia se muevan, sino de un pasito nama
                        spend_energy = soldier.use_energy(next_pos)
                        if soldier.get_energy() - spend_energy >= 0:
                            soldier.move_soldier(
                                next_pos[0], next_pos[1], map.get_battlefield())
        if rounds % 5 == 0:
            print_map(map)
        print('\n')
        # if len(army_a) <= len(army_b)*0.3  or len(army_b) <= len(army_a)*0.3:   ## revisar esto bien
        #     #print("No se acabo x las rondas de simulacion")
        #     break
        if len(army_a) == 0 or len(army_b) == 0:
            break
        soldier_energy(soldiers)
        if rain_mm[0] > 50:
            for sol in soldiers:
                rain.remove_debuff(sol)
        for camp in map.camps:
            fix_weapons_and_restore_stats(camp, map)
        remove_soldier_form_list(soldiers, army_a, army_b)
        map.remove_fallen_soldiers()
        rounds -= 1

    auxiliar.fix_axes(iterations, soldiers_a, soldiers_b)
    # Graph_simulation.plot_soldiers_alive("battle progression",iterations,soldiers_a,soldiers_b)
    # (soldiers_a, soldiers_b, "Cantidad de soldados")
    # pyplot.show()
    print(army_a, army_b, len(soldiers))
    # print(map.battlefield)
    # print(rounds)
    print_map(map)
    return soldiers


def remove_soldier_form_list(soldiers, army_a, army_b):
    for i, soldier in enumerate(soldiers):
        if soldier.life_points <= 0:
            temp = soldiers.pop(i)
            if temp in army_a:
                army_a.remove(temp)
            else:
                army_b.remove(temp)


def add_soldiers_characteristics(list_soliders, max_charact):
    rdm = rd.Random()
    perm = list(range(6))
    rdm.shuffle(perm)
    for sol in list_soliders:
        for i in range(max_charact):
            t = all_characteristics[perm[i]]
            t.apply_buff(sol, EnumAttribute.Medium)
            sol.characteristics.append(t)


def add_charact_variat_b(list_soldiers, charact_index: list[int]):
    for sol in list_soldiers:
        for i in charact_index:
            charact = all_characteristics[i]
            charact.apply_buff(sol, EnumAttribute.Medium)
            sol.characteristics.append(charact)


def soldier_energy(soldiers):
    for soldier in soldiers:
        if soldier.get_energy() > 300:
            continue
        soldier.recover_enery()


def asign_camps_to_soldiers(soldiers, camps):
    for soldier in soldiers:
        if soldier.army == camps[0].army:
            soldier.camp = camps[0]
        else:
            soldier.camp = camps[1]


def print_map(map):
    for x in range(map.get_row()):
        for y in range(map.get_col()):
            if map.get_battlefield()[x][y] == None:
                print("_", end=' ', sep=' ')
            else:
                print(map.get_battlefield()[x][y], end=' ', sep=' ')
        print('\n')


def check_possition(soldiers, camps, map):
    for sol in soldiers:
        if (sol.get_pos_x(), sol.get_pos_y()) in (camps[0].n_cells) or (sol.get_pos_x(), sol.get_pos_y()) in (camps[1].n_cells):
            if (sol.get_pos_x() + 1) < map.get_row() and map.battlefield[sol.get_pos_x() + 1][sol.get_pos_y()] == None:
                map.battlefield[sol.get_pos_x()][sol.get_pos_y()] = None
                sol.pos_x = sol.get_pos_x() + 1
                map.battlefield[sol.get_pos_x()][sol.get_pos_y()] = sol
            if (sol.get_pos_x() - 1) < map.get_row() and map.battlefield[sol.get_pos_x() - 1][sol.get_pos_y()] == None:
                map.battlefield[sol.get_pos_x()][sol.get_pos_y()] = None
                sol.pos_x = sol.get_pos_x() - 1
                map.battlefield[sol.get_pos_x()][sol.get_pos_y()] = sol
            if (sol.get_pos_y() + 1) < map.get_col() and map.battlefield[sol.get_pos_x()][sol.get_pos_y() + 1] == None:
                map.battlefield[sol.get_pos_x()][sol.get_pos_y()] = None
                sol.pos_y = sol.get_pos_y() + 1
                map.battlefield[sol.get_pos_x()][sol.get_pos_y()] = sol
            if (sol.get_pos_x() + 1) < map.get_col() and map.battlefield[sol.get_pos_x()][sol.get_pos_y() - 1] == None:
                map.battlefield[sol.get_pos_x()][sol.get_pos_y()] = None
                sol.pos_y = sol.get_pos_y() - 1
                map.battlefield[sol.get_pos_x()][sol.get_pos_y()] = sol


# Para usar el algoritmo genético descomente las 3 siguientes lineas
# y comente las lineas, 186-188
# ga_ = ga.GeneticALgorithm(
#     characteristics_of_soldiers, armors, min_price, 1000, start_simulation)
# gen = ga_.optimize()
# gen = [3, 2, 1, (0, 4), (1, 5), (2, 4), (3, 6), (4, 2)]
pickle_1 = open(
    'C:/Users/acer/Downloads/Telegram Desktop/Simulacion/Proyecto simulacion/Battlefield/gen.txt', 'rb')
gen = pickle.load(pickle_1)
soldiers_ = start_simulation(20, 20, 40, 40, 100, gen[0])
