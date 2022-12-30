import random as rd
from matplotlib import pyplot, colors


class Map():
    def __init__(self, rows, cols, visits) -> None:
        """_summary_
        Clase para representar el campo de batalla de la simulacion.
        Args:
            rows (_int_): representa la cantidad de filas del campo de batalla.
            cols (_int_): representa la cantidad de columnas del campo de batalla.
        """
        self.rows = rows
        self.cols = cols
        self.battlefield = [[None for _ in range(cols)] for _ in range(rows)]
        self.camps_for_army = 1
        self.camps: list[Camp] = []
        self.create_camps(self.camps_for_army, 'A', visits)
        self.create_camps(self.camps_for_army, 'B', visits)
        self.camps[0].n_cells = nearby_cells(self.camps[0], self)
        self.camps[1].n_cells = nearby_cells(self.camps[1], self)

    def get_camps(self):
        return self.camps

    def get_row(self):
        return self.rows

    def get_col(self):
        return self.cols

    def get_battlefield(self):
        return self.battlefield

    def is_free_cell(self, row, col):
        return self.get_battlefield()[row][col] == None

    # funcion para devolver una instancia del mapa
    def copy(self):
        graph = [None for _ in range(self.get_row)
                 for _ in range(self.get_col())]
        for row in range(self.get_row()):
            for col in range(self.get_col()):
                if not self.is_free_cell(row, col):
                    graph[row][col] = self.battlefield[row][col].army
        return graph

    def get_free_cell_random(self, army):
        if army == 'A':
            return rd.randint(0, self.get_row() // 2), rd.randint(0, self.get_row())
        return rd.randint(self.get_row() // 2, self.get_row()), rd.randint(0, self.get_row())

    # coloca los soldados en el campo de batalla, ubicando cada ejercito
    # en una de las mitades de la matriz
    def get_free_cell(self, army):
        free_cells = []
        if army == 'A':
            for row in range(self.get_row()//2):  # range(0, self.rows//2)
                for col in range(self.get_col()):  # range(self.get_col())
                    if self.is_free_cell(row, col):
                        free_cells.append((row, col))
        if army == 'B':
            # range(self.rows//2, self.rows)
            for row in range(self.get_row()//2, self.get_row()):
                for col in range(self.get_col()):  # range(self.get_col())
                    if self.is_free_cell(row, col):
                        free_cells.append((row, col))
        if len(free_cells) == 0:
            return None, None

        randmon = rd.randrange(0, len(free_cells))
        return free_cells[randmon]

    def plot_battlefield(self, populated_battl, plotTitle):
        # seleccionar los colores para el mapa
        color_map = colors.ListedColormap(["lightgrey", "red", "blue"])
        pyplot.figure(figsize=(12, 12))
        pyplot.title(plotTitle, fontsize=24)
        pyplot.xlabel("x coordinates", fontsize=20)
        pyplot.ylabel("y coordinates", fontsize=20)
        pyplot.xticks(fontsize=16)
        pyplot.yticks(fontsize=16)
        pyplot.imshow(X=populated_battl, cmap=color_map)

    def populate_battlefield(self):
        # .imshow () necesita una matriz con elementos flotantes;
        population_map = [
            [0.0 for _ in range(self.get_row())] for _ in range(self.get_col())]
        # si el agente es de tipo A, poner 1.0, si es de tipo B, pyt 2.0
        for i in range(self.get_row()):
            for j in range(self.get_col()):
                if self.battlefield[i][j]:
                    if self.battlefield[i][j].army == "A":  # agentes del grupo A
                        population_map[i][j] = 1.0  # 1.0 significa "A"
                    elif self.battlefield[i][j].army == "B":
                        population_map[i][j] = 2.0  # 2.0 significa "B"
        # devolver valores mapeados
        return (population_map)

    def remove_fallen_soldiers(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.battlefield[i][j] and not isinstance(self.battlefield[i][j], Camp):
                    if self.battlefield[i][j].life_points <= 0:
                        self.battlefield[i][j] = None

    def create_camps(self, camp_amount, army, visits):
        while camp_amount > 0:
            pos_x, pos_y = self.get_free_cell(army)
            self.battlefield[pos_x][pos_y] = Camp(army, pos_x, pos_y, visits)
            camp_amount -= 1
            self.camps.append(self.battlefield[pos_x][pos_y])
            print(f"campamento creado en {pos_x, pos_y}")


class Camp(object):

    def __init__(self, army, pos_x, pos_y, visits) -> None:
        self.army = army
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.visits = visits
        self.state = True  # variable para saber si continua permitiendo visitas
        self.n_cells = []

    def dec_visit(self):
        self.visits -= 1
        if self.visits == 0:
            self.state = False
            print("CAMPAMENTO AGOTADO")

    def __repr__(self) -> str:
        return "C"


def fix_weapons_and_restore_stats(camp, map):
    for pos in camp.n_cells:
        if map.get_battlefield()[pos[0]][pos[1]] != None and map.get_battlefield()[pos[0]][pos[1]].army == camp.army:
            map.get_battlefield()[pos[0]][pos[1]].restore_stats()


def nearby_cells(camp, map):
    result = []
    if (camp.pos_x + 1) < map.get_row():
        result.append((camp.pos_x + 1, camp.pos_y))
    if (camp.pos_x - 1) >= 0:
        result.append((camp.pos_x - 1, camp.pos_y))
    if (camp.pos_y + 1) < map.get_col():
        result.append((camp.pos_x, camp.pos_y + 1))
    if (camp.pos_y + 1) > 0:
        result.append((camp.pos_x, camp.pos_y - 1))
    return result
