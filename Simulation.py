from Soldier import *
from Battlefield import *
import Graph_simulation
import auxiliar
import time


def start_simulation(map_rows, map_cols,amount_army_a, amount_army_b, rounds):
    soldiers : List[Soldier] = [] #lista que contendra todos los soldados de la simulacion
    map = Map(map_rows,map_cols) #mapa de la simulacion
    army_a = create_soldier(amount_army_a,'A',map)
    army_b = create_soldier(amount_army_b,'B',map)

    for soldier in army_a:
        soldiers.append(soldier)
    for soldier in army_b:
        soldiers.append(soldier)
    #poblar el mapa que se graficara con los soldados creados
    populated_map = map.populate_battlefield()
    #se ordenan los soldados de ambos ejercitos segun su velocidad
    soldiers.sort(key = lambda soldier : soldier.speed, reverse= True)

    map.plot_battlefield(populated_map, "Mapa antes de la simulacion (red = Army A, blue = Army B)")

    soldiers_a = []
    soldiers_b = []

    pyplot.show()


    iterations = [i for i in range(rounds)]
    while rounds> 0:
        #contar a todos los soldados por ejercito para graficar luego
        soldiers_a, soldiers_b = Graph_simulation.count_soldiers_alive(soldiers_a,soldiers_b,map)
        #mandar a todo los soldados a atcar
        for soldier in soldiers:
            attacked = soldier.attack_strategy_one(map)
            if not attacked:
                start = time.time()
                next_pos = auxiliar.bfs(map.get_battlefield(),soldier)
                print(time.time() - start, "++++++++++++")
                if next_pos is not None:
                    soldier.move_soldier(next_pos[0],next_pos[1],map.get_battlefield())
        #luego de cada ronda, donde todos los soldados ataquen, se debe quitar de la lista de los soldados aquellos que tengan vida <= 0
        remove_soldier_form_list(soldiers,army_a,army_b)

        #lo mismo debe hacerse en el campo de batalla
        map.remove_fallen_soldiers()
        if len(army_a) <= len(army_b)*0.2  or len(army_b) <= len(army_a)*0.2:   ## revisar esto bien
            break
        rounds -= 1
    auxiliar.fix_axes(iterations,soldiers_a,soldiers_b)
    #colocar los soldados que quedaron en el mapa para plotearlo
    battlefield_after_battle = map.populate_battlefield()
    map.plot_battlefield(battlefield_after_battle, "Mapa despues de la simulacion (red = Army A, blue = Army B)")
    pyplot.show()
    Graph_simulation.plot_soldiers_alive("battle progression",iterations,soldiers_a,soldiers_b)
    (soldiers_a, soldiers_b, "Cantidad de soldados")
    pyplot.show()
    print(army_a,army_b,len(soldiers))


def remove_soldier_form_list(soldiers,army_a, army_b):
    for i,soldier in enumerate(soldiers):
        if soldier.life_points <= 0:
            print(len(soldiers))
            temp = soldiers.pop(i)
            print(len(soldiers))
            if temp in army_a:
                army_a.remove(temp)
            else:
                army_b.remove(temp)


start_simulation(20,20,100,100,70)