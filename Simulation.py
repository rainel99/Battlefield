from Soldier import *
from Battlefield import *
import random


map = Map(100,100)
agents_A = []
agents_B = []

a = create_soldier(1000,'A',map)
b = create_soldier(1000,'B',map)

populated_map = map.populate_battlefield(map.battlefield,map.rows,map.cols)
map.plot_battlefield(populated_map, "Mapa antes de la simulacion (red = Army A, blue = Army B)")
pyplot.show()
