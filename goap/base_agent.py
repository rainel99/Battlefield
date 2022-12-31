from goap_astar import Planner, Action_List

class Agent:  # Clase base para los agentes
    def __init__(self, *keys):
        self.planner = Planner(*keys) # Planner
        self.actions = Action_List() # Lista de acciones
    
    def set_start_state(self, **kwargs): # Establecer estado inicial del agente
        self.planner.set_start_state(**kwargs)
    
    def set_goal_state(self, **kwargs): # Establecer estado objetivo del agente
        self.planner.set_goal_state(**kwargs)
    
    def set_action_list(self): # Establecer lista de acciones del agente
        self.planner.set_action_list(self.actions)

    def add_condition(self, key, **kwargs): # Establecer condición de una acción
        self.actions.add_condition(key, **kwargs)

    def add_reaction(self, key, **kwargs): # Establecer reacción de una acción
        self.actions.add_reaction(key, **kwargs)
    
    def add_weight(self, key, weight): # Establecer peso de una acción
        self.actions.set_weight(key, weight)
    
    def calculate(self):
        return self.planner.calculate()