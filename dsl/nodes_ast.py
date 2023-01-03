from turtle import left
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


class ExpressionNode(AstNode):
    def __init__(self) -> None:
        super().__init__()


class AssignNode(ExpressionNode):
    def __init__(self, type_, id, value) -> None:
        self.type_ = type_
        self.id = id
        self.value = value


class BinaryExpNode(ExpressionNode):
    def __init__(self, left, operator, right) -> None:
        self.left = left
        self.operator = operator
        self.right = right


class FuncNode(AstNodeChildren):  # no terminado
    def __init__(self, id, params, block) -> None:
        super().__i
        self.Id = id
        self.params = params
        self.block = block
