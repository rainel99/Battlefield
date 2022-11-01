from time import sleep

from Soldier import *
from Battlefield import *
import Graph_simulation
import auxiliar



def start_simulation(map_rows, map_cols,amount_army_A, amount_army_B, rounds):
    soldiers : List[Soldier] = [] #lista que contendra todos los soldados de la simulacion
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
        print(soldiers_A,soldiers_B,"lo que ha contado")
        print(map.battlefield,"Estado verdadero")
        #mandar a todo los soldados a atcar
        for soldier in soldiers:
            attacked = soldier.attack_strategy_one(map)
            if not attacked:
                next_pos = auxiliar.bfs(map.get_battlefield(),soldier)
                print(map.get_battlefield(),"lo que le entra el bfs")
                if next_pos != None:
                    soldier.move_soldier(next_pos[0],next_pos[1],map.get_battlefield())
        #luego de cada ronda, donde todos los soldados ataquen, se debe quitar de la lista de los soldados aquellos que tengan vida <= 0
        remove_soldier_form_list(soldiers,army_A,army_B)
        #lo mismo debe hacerse en el campo de batalla
        map.remove_fallen_soldiers()

        if len(army_A) == 0 or len(army_B) == 0:
            break
        rounds -= 1
        #battlefield_after_battle = map.populate_battlefield(map.battlefield, map.get_row(),map.get_col())
        #map.plot_battlefield(battlefield_after_battle,"")
        # pyplot.show()
        # sleep(1.0)
        # pyplot.close("all")
        print(rounds, len(soldiers))
    auxiliar.fix_axes(iterations,soldiers_A,soldiers_B)
    #colocar los soldados que quedaron en el mapa para plotearlo
    battlefield_after_battle = map.populate_battlefield(map.battlefield, map.get_row(),map.get_col())
    map.plot_battlefield(battlefield_after_battle, "Mapa despues de la simulacion (red = Army A, blue = Army B)")
    pyplot.show()
    Graph_simulation.plot_soldiers_alive("battle progression",iterations,soldiers_A,soldiers_B)
    print(soldiers_A, soldiers_B, "Cantidad de soldados")
    pyplot.show()


def remove_soldier_form_list(soldiers,army_A, army_B):
    for i,soldier in enumerate(soldiers):
        if soldier.life_points <= 0:
            temp = soldiers.pop(i)
            if temp in army_A:
                army_A.remove(temp)
            else:
                army_B.remove(temp)

#start_simulation(30,30,300,300,70)
start_simulation(10,10,30,30,70)