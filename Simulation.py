from Soldier import *
from Battlefield import *
import Graph_simulation
import auxiliar
import random as rd
from characteristics_of_soldiers import all_characteristics, EnumAttribute
from weather import stats as weather


def start_simulation(map_rows, map_cols, amount_army_a, amount_army_b, rounds):
    # lista que contendra todos los soldados de la simulacion
    soldiers: List[Soldier] = []
    map = Map(map_rows, map_cols)  # mapa de la simulacion
    army_a = create_soldier(amount_army_a, 'A', map)
    army_b = create_soldier(amount_army_b, 'B', map)
    for soldier in army_a:
        soldiers.append(soldier)
    for soldier in army_b:
        soldiers.append(soldier)
    # se ordenan los soldados de ambos ejercitos segun su velocidad
    soldiers.sort(key=lambda soldier: soldier.speed, reverse=True)
    soldiers_a = []
    soldiers_b = []
    add_soldiers_characteristics(army_a, 3)
    add_soldiers_characteristics(army_b, 3)

    # a partir de la region seleccionada y la fecha => generar una v_a para las precipitaciones
    rain = weather.Rain()
    country = "spain"
    month = "july"
    # country = input("spain o argentina: ")
    # month = input("print a month of the year: ")

    mean, var = rain.calc_mean_var(country)
    iterations = [i for i in range(rounds)]
    while rounds > 0:
        rain_mm = rain.get_rain_prob(mean, var, month)
        if rain_mm[0] > 50:
            for sol in soldiers:
                rain.apply_debuf(sol)

        # contar a todos los soldados por ejercito para graficar luego
        soldiers_a, soldiers_b = Graph_simulation.count_soldiers_alive(
            soldiers_a, soldiers_b, map)
        # mandar a todo los soldados a atcar
        for soldier in soldiers:
            attacked = soldier.attack_strategy_one(map)
            if not attacked:
                #start = time.time()
                next_pos = auxiliar.bfs(map.get_battlefield(), soldier)
                if next_pos != None:
                    # !!!!! aqui voy a cambiar cosas pa q si tienen energia se muevan, sino de un pasito nama
                    spend_energy = soldier.use_energy(next_pos)
                #print(time.time() - start, "++++++++++++")
                    if soldier.get_energy() - spend_energy >= 0:
                        soldier.move_soldier(
                            next_pos[0], next_pos[1], map.get_battlefield())
        # luego de cada ronda, donde todos los soldados ataquen, se debe quitar de la lista de los soldados aquellos que tengan vida <= 0
        remove_soldier_form_list(soldiers, army_a, army_b)
        # lo mismo debe hacerse en el campo de batalla
        map.remove_fallen_soldiers()
        # if len(army_a) <= len(army_b)*0.3  or len(army_b) <= len(army_a)*0.3:   ## revisar esto bien
        #     #print("No se acabo x las rondas de simulacion")
        #     break
        if len(army_a) == 0 or len(army_b) == 0:
            break
        # dar energia a todos los soldados
        for soldier in soldiers:
            soldier.recover_enery()
        if rain_mm[0] > 50:
            for sol in soldiers:
                rain.remove_debuff(sol)
        rounds -= 1
    auxiliar.fix_axes(iterations, soldiers_a, soldiers_b)
    # Graph_simulation.plot_soldiers_alive("battle progression",iterations,soldiers_a,soldiers_b)
    # (soldiers_a, soldiers_b, "Cantidad de soldados")
    # pyplot.show()
    print(army_a, army_b, len(soldiers))
    # print(map.battlefield)
    # print(rounds)


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


n = 0
while (n < 20):
    print(n)
    start_simulation(20, 20, 100, 100, 150)
    n += 1
