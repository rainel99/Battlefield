import random as rd
from matplotlib import pyplot,colors
class Map():
    def __init__(self, rows, cols) -> None:
        """_summary_
        Clase para representar el campo de batalla de la simulacion.
        Args:
            rows (_int_): representa la cantidad de filas del campo de batalla.
            cols (_int_): representa la cantidad de columnas del campo de batalla.
        """
        self.rows = rows
        self.cols = cols
        self.battlefield = [[None for _ in range(rows)] for _ in range(cols)]
    
    def get_row(self):
        return self.rows

    def get_col(self):
        return self.cols
    
    def get_battlefield(self):
        return self.battlefield

    def is_free_cell(self,row,col):
        return self.get_battlefield()[row][col] == None

    #funcion para devolver una instancia del mapa
    def copy(self):
        graph = [None for _ in range(self.get_row) for _ in range(self.get_col())]
        for row in range(self.get_row()):
            for col in range(self.get_col()):
                if not self.is_free_cell(row,col):
                    graph[row][col] = self.battlefield[row][col].army
        return graph

    #coloca los soldados en el campo de batalla, ubicando cada ejercito
    #en una de las mitades de la matriz
    def get_free_cell(self,army):
        free_cells = []
        if army == 'A':
            for row in range(0,self.get_row()//2): #range(0, self.rows//2)
                for col in range(self.get_col()): #range(self.get_col())
                    if self.is_free_cell(row,col):
                        free_cells.append((row,col))
        if army == 'B':
            for row in range(self.get_row()//2,self.get_row()):#range(self.rows//2, self.rows)
                for col in range(self.get_col()):#range(self.get_col())
                    if self.is_free_cell(row,col):
                        free_cells.append((row,col))
        if len(free_cells) == 0:
            return None, None

        randmon = rd.randrange(0,len(free_cells))
        return free_cells[randmon]     

    def plot_battlefield(self,populated_battl, plotTitle):
        #seleccionar los colores para el mapa
        color_map = colors.ListedColormap(["lightgrey","red","blue"])
        pyplot.figure(figsize= (12,12))
        pyplot.title(plotTitle,fontsize = 24)
        pyplot.xlabel("x coordinates", fontsize = 20)
        pyplot.ylabel("y coordinates", fontsize = 20)
        pyplot.xticks(fontsize = 16)
        pyplot.yticks(fontsize = 16)
        pyplot.imshow(X = populated_battl, cmap = color_map)

    def populate_battlefield(self,battlefield,row,col):
        # .imshow () necesita una matriz con elementos flotantes;
        population_map = [[0.0 for _ in range(row)] for _ in range(col)]
        # si el agente es de tipo A, poner 1.0, si es de tipo B, pyt 2.0
        for i in range(row):
            for j in range(col):
                if battlefield[i][j]:
                    if battlefield[i][j].army == "A": # agentes del grupo A
                        population_map[i][j] = 1.0 # 1.0 significa "A"
                    elif battlefield[i][j].army == "B":
                        population_map[i][j] = 2.0 # 2.0 significa "B"
        # devolver valores mapeados
        return(population_map)

    def remove_fallen_soldiers(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.battlefield[i][j]:
                    if self.battlefield[i][j].life_points <= 0:
                        self.battlefield[i][j] = None