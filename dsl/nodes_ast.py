import ply.yacc as yacc


class AstNode(object):
    pass


class AstNodeChildren(AstNode):
    def __init__(self, *args) -> None:
        self.children = args


class SimulationNode(AstNodeChildren):
    def __init__(self, M, A1, A2) -> None:
        self.M = M
        self.A1 = A1
        self.A2 = A2


class MapNode(AstNodeChildren):
    def __init__(self, *args) -> None:
        super().__init__(*args)


class ArmyNode(AstNodeChildren):
    def __init__(self, *args) -> None:
        super().__init__(*args)
