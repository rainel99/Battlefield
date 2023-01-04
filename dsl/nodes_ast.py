from turtle import left
from numpy import binary_repr
import ply.yacc as yacc


class AstNode(object):
    pass


class AstNodeChildren(AstNode):
    def __init__(self, *args) -> None:
        self.children = [args]


class SimulationNode(AstNode):
    def __init__(self, Map, Army_1, Army_2, program) -> None:
        self.M = Map
        self.A1 = Army_1
        self.A2 = Army_2
        self.program = program


class MapNode(AstNodeChildren):
    def __init__(self, *args) -> None:
        super().__init__(*args)


class ArmyNode(AstNodeChildren):
    def __init__(self, *args) -> None:
        super().__init__(*args)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1


class ProgramNode(AstNode):
    def __init__(self, decl) -> None:
        self.decl = decl


class DeclarationNode(AstNodeChildren):
    def __init__(self, *args) -> None:
        super().__init__(*args)


class DeclFuncNode(AstNode):
    def __init__(self, func_decl) -> None:
        self.func_decl = func_decl


class DeclVarNode(AstNode):
    def __init__(self, var_dec) -> None:
        self.var_dec = var_dec


class DeclStmtNode(AstNode):
    def __init__(self, stmt_decl) -> None:
        self.decl_stmt = stmt_decl


class VarNode(AstNode):
    def __init__(self, type_, id, expr) -> None:
        self.type_ = type_
        self.id = id
        self.expr = expr


class StmtNode(AstNodeChildren):
    def __init__(self, *args) -> None:
        super().__init__(*args)


class ExprStmtNode(StmtNode):
    def __init__(self, expr_node) -> None:
        self.expr_node = expr_node


class WhileStmtNode(StmtNode):
    def __init__(self, while_node) -> None:
        self.while_node = while_node


class IfStmtNode(StmtNode):
    def __init__(self, if_node) -> None:
        self.if_node = if_node


class PrintStmtNode(StmtNode):
    def __init__(self, print_node) -> None:
        self.pirnt_node = print_node


class ReturnStmtNode(StmtNode):
    def __init__(self, return_node) -> None:
        self.return_node = return_node


class BlockStmtNode(StmtNode):
    def __init__(self, block_node) -> None:
        self.block_node = block_node

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


class IfNode(AstNode):
    def __init__(self, condition, statement) -> None:
        self.condition = condition
        self.statement = statement


class PrintNode(AstNode):
    def __init__(self, expr) -> None:
        self.expr = expr


class ReturnNode(AstNode):
    def __init__(self, expr) -> None:
        self.expr = expr


class WhileNode(AstNode):
    def __init__(self, condition, statement) -> None:
        self.condition = condition
        self.statement = statement


class BlockNode(AstNode):
    def __init__(self, declaration) -> None:
        self.declaration = declaration


class ExpressionNode(AstNode):
    def __init__(self, assign) -> None:
        self.assign = assign


class AssignNode(ExpressionNode):
    def __init__(self, type_, id, value) -> None:
        self.type_ = type_
        self.id = id
        self.value = value


class BinaryExpNode(ExpressionNode):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right


class LogicExprNode(AstNode):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right


class LogicOrNode(LogicExprNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)


class LogicaAndNode(LogicExprNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)


class ComparisonNotEqNode(BinaryExpNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)


class ComparisonLtNode(BinaryExpNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)


class ComparisonGtNode(BinaryExpNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)


class ComparisonGteNode(BinaryExpNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)


class ComparisonLteNode(BinaryExpNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)


class ComparisonEqEqNode(BinaryExpNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)


class FuncNode(AstNodeChildren):  # no terminado
    def __init__(self, id, params, block) -> None:
        super().__i
        self.Id = id
        self.params = params
        self.block = block


class UnaryNode(AstNode):
    def __init__(self, operator, exp_right) -> None:
        self.operator = operator
        self.exp_right = exp_right


class UnaryNotNode(UnaryNode):
    def __init__(self, exp_right) -> None:
        self.exp_right = exp_right


class UnaryMinusNode(UnaryNode):
    def __init__(self, exp_right) -> None:
        self.exp_right = exp_right


class MinusNode(BinaryExpNode):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right


class PlusNode(BinaryExpNode):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right


class StarNode(BinaryExpNode):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right


class DivNode(BinaryExpNode):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right


class CallNode(AstNode):
    def __init__(self, primary) -> None:
        self.primary = primary


class CallArgsNode(CallNode):
    def __init__(self, primary, args) -> None:
        super().__init__(primary)
        self.args = args


class CallIdNode(CallNode):
    def __init__(self, primary, id) -> None:
        super().__init__(primary)
        self.id = id


class PrimaryNode(AstNode):
    def __init__(self, token) -> None:
        self.token = token


class PrimaryFalseNode(PrimaryNode):
    def __init__(self, token) -> None:
        super().__init__(token)


class PrimaryTrueNode(PrimaryNode):
    def __init__(self, token) -> None:
        super().__init__(token)


class PrimaryNumberNode(PrimaryNode):
    def __init__(self, token) -> None:
        super().__init__(token)


class PrimaryIdNode(PrimaryNode):
    def __init__(self, token) -> None:
        super().__init__(token)


class PrimaryNilNode(PrimaryNode):
    def __init__(self, token) -> None:
        super().__init__(token)


class ArgumentsNode(AstNode):
    def __init__(self, expr) -> None:
        self.expr = expr
