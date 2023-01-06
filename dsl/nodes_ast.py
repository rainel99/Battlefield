from abc import abstractmethod
from contextlib import ContextDecorator
from logging import exception
from sre_constants import ASSERT_NOT
from symbol import expr
from matplotlib.style import context
import ply.yacc as yacc
from psycopg2 import paramstyle
from pyparsing import condition_as_parse_action
from zmq import ContextTerminated


def create_context_child(context):
    my_context = {}
    for key in context:
        my_context[key] = context[key]
    return my_context


class AstNode(object):
    pass

    @abstractmethod
    def eval(self, context):
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

    def eval(self):
        new_context = {}
        self.program.eval(new_context)


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

    def eval(self, context: dict):
        for d in self.decl:
            d.eval(context)


class DeclFuncNode(AstNode):
    def __init__(self, func_decl) -> None:
        self.func_decl = func_decl

    def eval(self, context):
        self.func_decl.eval(context)


class DeclVarNode(AstNode):
    def __init__(self, var_dec) -> None:
        self.var_dec = var_dec

    def eval(self, context):
        self.var_dec.eval(context)


class DeclStmtNode(AstNode):
    def __init__(self, stmt_decl) -> None:
        self.decl_stmt = stmt_decl

    def eval(self, context):
        self.decl_stmt.eval(context)


class VarNode(AstNode):
    def __init__(self, type_, id, expr) -> None:
        self.type_ = type_
        self.id = id
        self.expr = expr

    def eval(self, context):
        if id in context.keys():
            assert Exception("-----")
        else:
            context[self.id] = self.expr.eval(context)


class StmtNode(AstNode):
    pass


class ExprStmtNode(StmtNode):
    def __init__(self, expr_node) -> None:
        self.expr_node = expr_node

    def eval(self, context):
        self.expr_node.eval(context)


class WhileStmtNode(StmtNode):
    def __init__(self, while_node) -> None:
        self.while_node = while_node

    def eval(self, context):
        self.while_node.eval(context)


class IfStmtNode(StmtNode):
    def __init__(self, if_node) -> None:
        self.if_node = if_node

    def eval(self, context):
        self.if_node.eval(context)


class PrintStmtNode(StmtNode):
    def __init__(self, print_node) -> None:
        self.pirnt_node = print_node

    def eval(self, context):
        self.pirnt_node.eval(context)


class ReturnStmtNode(StmtNode):
    def __init__(self, return_node) -> None:
        self.return_node = return_node

    def eval(self, context):
        self.return_node.eval(context)


class BlockStmtNode(StmtNode):
    def __init__(self, block_node) -> None:
        self.block_node = block_node

    def eval(self, context):
        self.block_node.eval(context)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


class IfNode(AstNode):
    def __init__(self, condition, statement, else_) -> None:
        self.condition = condition
        self.statement = statement
        self.else_ = else_

    def eval(self, context):
        new_context = create_context_child(context)
        if self.condition.eval(context):
            self.statement.eval(new_context)
        elif self.else_ != None:
            self.else_.eval(context)


class ElseNode(AstNode):
    def __init__(self, statement) -> None:
        self.statement = statement

    def eval(self, context):
        new_context = create_context_child(context)
        self.statement.eval(new_context)


class PrintNode(AstNode):
    def __init__(self, expr) -> None:
        self.expr = expr

    def eval(self, context):
        print(self.expr.eval(context))
        # print(self.expr)


class ReturnNode(AstNode):
    def __init__(self, expr) -> None:
        self.expr = expr

    def eval(self, context):
        raise Exception(self.expr.eval(context))


class WhileNode(AstNode):
    def __init__(self, condition, statement) -> None:
        self.condition = condition
        self.statement = statement

    def eval(self, context):
        while self.condition.eval(context):
            new_context = create_context_child(context)
            self.statement.eval(new_context)
            context = new_context


class BlockNode(AstNode):
    def __init__(self, declaration) -> None:
        self.declaration = declaration

    def eval(self, context):
        for d in self.declaration:
            d.eval(context)  # ! Comprabar!!!!!!!!!!!!!!!!!!!!!!!!!!!!


class ExpressionNode(AstNode):
    def __init__(self, assign) -> None:
        self.assign = assign

    def eval(self, context):
        self.assign.eval(context)


class AssignNode(ExpressionNode):
    def __init__(self, type_, id, value) -> None:
        self.type_ = type_
        self.id = id
        self.value = value

    def eval(self, context):
        context[self.id] = self.value.eval(context)


class AssignNode_(ExpressionNode):
    def __init__(self, id, value) -> None:
        self.id = id
        self.value = value

    def eval(self, context):
        context[self.id] = self.value.eval(context)


class BinaryExpNode(ExpressionNode):
    def __init__(self, left: AstNode, right: AstNode) -> None:
        self.left = left
        self.right = right


class LogicExprNode(AstNode):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right


class LogicOrNode(LogicExprNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)

    def eval(self, context):
        return self.left.eval(context) or self.right.eval(context)


class LogicaAndNode(LogicExprNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)

    def eval(self, context):
        return self.left.eval(context) and self.right.eval(context)


class ComparisonNotEqNode(BinaryExpNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)

    def eval(self, context):
        return self.left.eval(context) != self.right.eval(context)


class ComparisonLtNode(BinaryExpNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)

    def eval(self, context):
        return self.left.eval(context) < self.right.eval(context)


class ComparisonGtNode(BinaryExpNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)

    def eval(self, context):
        return self.left.eval(context) > self.right.eval(context)


class ComparisonGteNode(BinaryExpNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)

    def eval(self, context):
        return self.left.eval(context) >= self.right.eval(context)


class ComparisonLteNode(BinaryExpNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)

    def eval(self, context):
        return self.left.eval(context) <= self.right.eval(context)


class ComparisonEqEqNode(BinaryExpNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)

    def eval(self, context):
        a = self.left.eval(context)
        b = self.right.eval(context)
        temp = a == b
        return self.left.eval(context) == self.right.eval(context)
        # if self.left in context and self.right in context:
        #     context[self.left] == context[self.right]
        # else:
        #     self.left.eval(context) == self.right.eval(context)


class FuncNode(AstNodeChildren):  # no terminado!!!!!!!!!!!!!!!!!
    def __init__(self, id, params, block) -> None:
        self.id = id
        self.params = params
        self.block = block

    def eval(self, context):
        params_name = []
        for tup in self.params:
            params_name.append(tup[1])
        context[self.id] = (params_name, self.block)


class UnaryNode(AstNode):
    def __init__(self, exp_right) -> None:
        self.exp_right = exp_right


class UnaryNotNode(UnaryNode):
    def __init__(self, exp_right) -> None:
        self.exp_right = exp_right

    def eval(self, context):
        return not self.exp_right.eval(context)


class UnaryMinusNode(UnaryNode):
    def __init__(self, exp_right) -> None:
        self.exp_right = exp_right

    def eval(self, context):
        return - self.exp_right.eval(context)


class MinusNode(BinaryExpNode):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def eval(self, context):
        return self.left.eval(context) - self.right.eval(context)


class PlusNode(BinaryExpNode):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def eval(self, context):
        return self.left.eval(context) + self.right.eval(context)


class StarNode(BinaryExpNode):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def eval(self, context):
        return self.left.eval(context) * self.right.eval(context)


class DivNode(BinaryExpNode):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def eval(self, context):
        return self.left.eval(context) / self.right.eval(context)


class CallNode(AstNode):
    def __init__(self, primary) -> None:
        self.primary = primary


class CallArgsNode(CallNode):
    def __init__(self, primary, args) -> None:
        super().__init__(primary)
        self.args = args

    def eval(self, context):
        new_context = create_context_child(context)
        if self.primary.id in new_context.keys():
            if len(self.args) != len(new_context[self.primary.id][0]):
                assert Exception("----")
            for i, name_var in enumerate(new_context[self.primary.id][0]):
                new_context[name_var] = self.args[i].eval(context)
            try:
                context[self.primary.id][1].eval(new_context)
            except:
                return
        else:
            assert Exception("----")

# class CallIdNode(CallNode):
#     def __init__(self, primary, id) -> None:
#         super().__init__(primary)
#         self.id = id


class PrimaryNode(AstNode):
    def __init__(self, token) -> None:
        self.token = token

    def eval(self, context):
        return self.token


class PrimaryFalseNode(PrimaryNode):
    def __init__(self, token) -> None:
        super().__init__(token)

    def eval(self, context):
        return False


class PrimaryTrueNode(PrimaryNode):
    def __init__(self, token) -> None:
        super().__init__(token)

    def eval(self, context):
        return True


class PrimaryNumberNode(PrimaryNode):
    def __init__(self, token) -> None:
        super().__init__(token)

    def eval(self, context):
        return self.token


class PrimaryIdNode(PrimaryNode):
    def __init__(self, token) -> None:
        super().__init__(token)

    def eval(self, context):
        if self.token in context.key():
            return context[self.token]
        else:
            assert Exception("----")


class PrimaryNilNode(PrimaryNode):
    def __init__(self, token) -> None:
        super().__init__(token)

    def eval(self, context):
        return None


class ArgumentsNode(AstNode):
    def __init__(self, expr) -> None:
        self.expr = expr

    def eval(self, context):
        for ex in expr:
            ex.eval(context)


class CallVar(AstNode):
    def __init__(self, id) -> None:
        self.id = id

    def eval(self, context):
        if self.id in context:
            return context[self.id]
        else:
            assert Exception("----")
