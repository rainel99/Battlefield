import ply.yacc as yacc


class AstNode(object):
    pass


class AstNodeChildren(AstNode):
    def __init__(self, *args) -> None:
        self.children = [args]


class SimulationNode(AstNode):
    def __init__(self, Map, Army_1, Army_2) -> None:
        self.M = Map
        self.A1 = Army_1
        self.A2 = Army_2


class MapNode(AstNodeChildren):
    def __init__(self, *args) -> None:
        super().__init__(*args)


class ArmyNode(AstNodeChildren):
    def __init__(self, *args) -> None:
        super().__init__(*args)
