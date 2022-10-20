from Soldier import *
from Battlefield import *
import random
import Graph_simulation



def start_simulation(map_rows, map_cols,amount_army_A, amount_army_B, rounds):
    soldiers = [] #lista que contendra todos los soldados de la simulacion
    map = Map(map_rows,map_cols) #mapa de la simulacion
    army_A = create_soldier(amount_army_A,'A',map) 
    army_B = create_soldier(amount_army_B,'B',map)

    for soldier in army_A:
        soldiers.append(soldier)
    for soldier in army_B:
        soldiers.append(soldier)
    #poblar el mapa que se graficara con los soldados creados
    populated_map = map.populate_battlefield(map.battlefield,map.get_row(),map.get_col())
    #se ordenan los soldados de ambos ejercitos segun su velocidad
    soldiers.sort(key = lambda soldier : soldier.speed, reverse= True)

    map.plot_battlefield(populated_map, "Mapa antes de la simulacion (red = Army A, blue = Army B)")

    soldiers_A = []
    soldiers_B = []

    pyplot.show()

    iterations = [i for i in range(rounds)]
    while rounds> 0:

        soldiers_A, soldiers_B = Graph_simulation.count_soldiers_alive(soldiers_A,soldiers_B,map)
        #mandar a todo los soldados a atcar
        for soldier in soldiers:
            soldier.attack_strategy_one(map)
        #luego de cada ronda, donde todos los soldados ataquen, se debe quitar de la lista de los soldados aquellos que tengan vida <= 0
        remove_soldier_form_list(soldiers)
        #lo mismo debe hacerse en el campo de batalla
        map.remove_fallen_soldiers()
        rounds -= 1
    #colocar los soldados que quedaron en el mapa para plotearlo
    battlefield_after_battle = map.populate_battlefield(map.battlefield, map.get_row(),map.get_col())
    map.plot_battlefield(battlefield_after_battle, "Mapa despues de la simulacion (red = Army A, blue = Army B)")
    pyplot.show()
    Graph_simulation.plot_soldiers_alive("battle progression",iterations,soldiers_A,soldiers_B)
    pyplot.show()


def remove_soldier_form_list(soldiers):
    for i,soldier in enumerate(soldiers):
        if soldier.life_points <= 0:
            soldiers.pop(i)

start_simulation(50,50,300,500,15)