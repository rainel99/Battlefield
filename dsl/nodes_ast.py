from abc import abstractmethod
from ply import yacc
import pickle
from Soldier import create_soldier
from Start_Simulation import start_simulation
from Battlefield import Map
from dsl.context import Context

# def create_context_child(context):
#     my_context = {}
#     for key in context:
#         my_context[key] = context[key]
#     return my_context


class AstNode(object):
    def __init__(self, type=None) -> None:
        self.type = type

    @abstractmethod
    def eval(self, context):
        pass

    @abstractmethod
    def checktype(self, context):
        pass


class AstNodeChildren(AstNode):
    def __init__(self, *args) -> None:
        self.children = args


class SimulationNode(AstNode):
    def __init__(self, Map, Army_1, Army_2, round, program) -> None:
        self.M = Map
        self.A1 = Army_1
        self.A2 = Army_2
        self.rounds = int(round)
        self.program = program
        self.context = Context()

    def eval(self):
        self.program.eval(self.context)
        row, col = self.M.eval(self.context)
        amount, army_name = self.A1.eval(self.context)
        amount_, army_name_ = self.A2.eval(self.context)
        my_map = Map(row, col, amount//3)
        army_1 = create_soldier(amount, army_name, my_map)
        army_2 = create_soldier(amount_, army_name_, my_map)
        pickle_1 = open('./gen.txt', 'rb')
        gen = pickle.load(pickle_1)
        start_simulation(my_map, army_1, army_2, self.rounds, gen[0])

    def checktype_(self):
        if not self.M.checktype(self.context) or not self.A1.checktype(self.context) or not self.A2.checktype(self.context) or not self.program.checktype(self.context):
            return False
        else:
            return True


class MapNode(AstNodeChildren):
    def __init__(self, *args) -> None:
        self.children = args

    def eval(self, context):
        if self.children[0][0][0] == 'ROW':
            return self.children[0][0][1], self.children[0][1][1]
        else:
            return self.children[0][1][1], self.children[0][0][1]

    def checktype(self, context):
        if len(self.children[0]) != 2:
            print(
                "Error! : Solo se permite definir el tipo row y col para la definición de mapa")
            return False
        if not (self.children[0][0][0] == 'ROW' and self.children[0][1][0] == 'COL') and not (self.children[0][0][0] == 'COL' and self.children[0][1][0] == 'ROW'):
            print("Error! : Debe haber un tipo row y col para definir el mapa.")
            return False
        self.type = AstNode
        return True


class ArmyNode(AstNodeChildren):
    def __init__(self, *args) -> None:
        super().__init__(*args)

    def eval(self, context):
        if self.children[0][0] == 'ARMY_name':
            return self.children[0][0][1], self.children[0][1][1]
        else:
            return self.children[0][1][1], self.children[0][0][1]

    def checktype(self, context):
        if len(self.children[0]) > 2:
            print(
                "Error! : Solo se permite definir el tipo army_name y amount para la definición del ejército")
            return False
        if not (self.children[0][0][0] == 'AMOUNT' and self.children[0][1][0] == 'ARMY_name') and not (self.children[0][0][0] == 'ARMY_name' and self.children[0][1][0] == 'AMOUNT'):
            print(
                "Error! : Debe haber un tipo army_name y amount para definir el ejército")
            return False
        self.type = AstNode
        return True


class ProgramNode(AstNode):
    def __init__(self, decl) -> None:
        self.decl = decl

    def eval(self, context):
        for d in self.decl:
            d.eval(context)

    def checktype(self, context):
        for d in self.decl:
            if not d.checktype(context):
                return False
        return True

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


class DeclFuncNode(AstNode):
    def __init__(self, func_decl) -> None:
        self.func_decl = func_decl

    def eval(self, context):
        self.func_decl.eval(context)

    def checktype(self, context):
        if self.func_decl.checktype(context):
            return False
        self.type = AstNode
        return True


class DeclVarNode(AstNode):
    def __init__(self, var_dec) -> None:
        self.var_dec = var_dec

    def eval(self, context):
        self.var_dec.eval(context)

    def checktype(self, context):
        if self.var_dec.checktype(context):
            return False
        self.type = AstNode
        return True


class DeclStmtNode(AstNode):
    def __init__(self, stmt_decl) -> None:
        self.decl_stmt = stmt_decl

    def eval(self, context):
        self.decl_stmt.eval(context)

    def checktype(self, context):
        if self.decl_stmt.checktype(context):
            return False
        self.type = AstNode
        return True


class VarNode(AstNode):
    def __init__(self, type_, id, expr) -> None:
        self.type_ = type_
        self.id = id
        self.expr = expr

    def eval(self, context):
        context.asing_value(self.id,self.expr.eval(context))

    def checktype(self, context):
        if self.id in context:
            return False
        else:
            if not self.type_.echecktype(context) or self.expr.checktype(context):
                return False
            if self.type_.type == -1:
                print("Error! : Variable inicializada como void")
                return False
            context.asing_value(self.id,(self.type_.type, self.expr.type))
        self.type = self.type_.type
        return True


class StmtNode(AstNode):
    pass


class ExprStmtNode(StmtNode):
    def __init__(self, expr_node) -> None:
        self.expr_node = expr_node

    def eval(self, context):
        self.expr_node.eval(context)

    def checktype(self, context):
        if not self.expr_node.checktype(context):
            return False
        self.checktype = AstNode
        return True


class WhileStmtNode(StmtNode):
    def __init__(self, while_node) -> None:
        self.while_node = while_node

    def eval(self, context):
        self.while_node.eval(context)

    def checktype(self, context):
        if not self.while_node.checktype(context):
            return False
        self.checktype = AstNode
        return True


class IfStmtNode(StmtNode):
    def __init__(self, if_node) -> None:
        self.if_node = if_node

    def eval(self, context):
        self.if_node.eval(context)

    def checktype(self, context):
        if not self.if_node.checktype(context):
            return False
        self.checktype = AstNode
        return True


class PrintStmtNode(StmtNode):
    def __init__(self, print_node) -> None:
        self.pirnt_node = print_node

    def eval(self, context):
        self.pirnt_node.eval(context)

    def checktype(self, context):
        if not self.pirnt_node.checktype(context):
            return False
        self.checktype = AstNode
        return True


class ReturnStmtNode(StmtNode):
    def __init__(self, return_node) -> None:
        self.return_node = return_node

    def eval(self, context):
        self.return_node.eval(context)

    def checktype(self, context):
        if not self.return_node.checktype(context):
            return False
        self.checktype = AstNode
        return True


class BlockStmtNode(StmtNode):
    def __init__(self, block_node) -> None:
        self.block_node = block_node

    def eval(self, context):
        self.block_node.eval(context)

    def checktype(self, context):
        if not self.block_node.checktype(context):
            return False
        self.checktype = AstNode
        return True

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


class IfNode(AstNode):
    def __init__(self, condition, statement, else_) -> None:
        self.condition = condition
        self.statement = statement
        self.else_ = else_

    def eval(self, context):
        new_context = Context(context)
        if self.condition.eval(context).token == 'True':
            self.statement.eval(new_context)
        elif self.else_ != None:
            self.else_.eval(context)

    def checktype(self, context):
        if not self.statement.checktype(context) or not self.condition.checktype(context):
            return False
        self.checktype = AstNode
        return True


class ElseNode(AstNode):
    def __init__(self, statement) -> None:
        self.statement = statement

    def eval(self, context):
        new_context = Context(context)
        self.statement.eval(new_context)

    def checktype(self, context):
        if not self.statement.checktype(context):
            return False
        self.checktype = AstNode
        return True


class PrintNode(AstNode):
    def __init__(self, expr) -> None:
        self.expr = expr

    def eval(self, context):
        a = self.expr.eval(context).token
        print(a)

    def checktype(self, context):
        if not self.expr.checktype(context):
            return False
        self.checktype = self.expr.type
        return True


class ReturnNode(AstNode):
    def __init__(self, expr) -> None:
        self.expr = expr

    def eval(self, context):
        raise Exception(self.expr.eval(context))

    def checktype(self, context):
        if not self.expr.checktype(context):
            return False
        self.type = self.expr.type
        return True


class WhileNode(AstNode):
    def __init__(self, condition, statement) -> None:
        self.condition = condition
        self.statement = statement

    def eval(self, context):
        while self.condition.eval(context).token == 'True':
            new_context = Context(context)
            self.statement.eval(new_context)
            context = new_context

    def checktype(self, context):
        if not self.condition.checktype(context) or not self.statement.checktype(context):
            return False
        self.type = AstNode
        return True


class BlockNode(AstNode):
    def __init__(self, declaration) -> None:
        self.declaration = declaration

    def eval(self, context):
        for d in self.declaration:
            d.eval(context)

    def checktype(self, context):
        types = []
        for d in self.declaration:
            if not d.checktype(context):
                return False, []
            if isinstance(d, ReturnNode):  # ! revisar esto
                types.append(d.type)

        self.type = AstNode
        return True, types


class ExpressionNode(AstNode):
    def __init__(self, assign) -> None:
        self.assign = assign

    def eval(self, context):
        self.assign.eval(context)


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class AssignNode(ExpressionNode):
    def __init__(self, type_, id, value) -> None:
        self.type_ = type_
        self.id = id
        self.value = value

    def eval(self, context):  # ! revisar
       # var = context.find_value(self.id)  
        new_v = self.value.eval(context)
        #var = (self.type_, new_v)
        context.asing_value(self.id,new_v)

    def checktype(self, context):
        if not self.value.checktype(context) or not self.type_.checktype(context):
            return False
        if self.id in context.symbols.keys():
            return False
        else:
            self.type_.checktype(context)
            if not self.value.checktype(context):
                return False
            # if self.type_.type != self.value.type:
            #     return False
            context.asing_value(self.id,(self.type_.type, self.value))
        if self.type_.type != self.value.type:
            return False
        self.type = self.type_.type
        return True


class AssignNode_(ExpressionNode):
    def __init__(self, id, value) -> None:
        self.id = id
        self.value = value

    def eval(self, context):
        if context.find_value(self.id):
            var = context.find_value(self.id)  
            new_v = self.value.eval(context)
            var.token = new_v.token
        else:
            context.asing_value(self.id,new_v)

    def checktype(self, context):
        if self.id not in context.symbols.keys():
            return False
        if not self.value.checktype(context):
            return False
        # !checkear esto, el indexer del dicc deberia dar un tipo
        if context.symbols[self.id] != self.value.type:
            return False
        self.type = self.value.type
        return True


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
        if self.left.eval(context).token or self.right.eval(context).token:
            return PrimaryTrueNode('True')
        else:
            return PrimaryFalseNode('False')
        #return  self.left.eval(context).token or self.right.eval(context).token

    def checktype(self, context):
        if not self.left.checktype(context) or not self.right.checktype(context):
            return False
        if self.left.type != 'bool' or self.right.type != 'bool':
            self.type = self.left.type
            return True
        return False


class LogicaAndNode(LogicExprNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)

    def eval(self, context):
        if self.left.eval(context).token and self.right.eval(context).token:
            return PrimaryTrueNode('True')
        else:
            return PrimaryFalseNode('False')
        #return self.left.eval(context).token and self.right.eval(context).token

    def checktype(self, context):
        if not self.left.checktype(context) or not self.right.checktype(context):
            return False
        if self.left.type == 'bool' or self.right.type == 'bool':
            self.type = self.left.type
            return True
        return False


class ComparisonNotEqNode(BinaryExpNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)

    def eval(self, context):
        if self.left.eval(context).token != self.right.eval(context).token:
            return PrimaryTrueNode('True')
        else:
            return PrimaryFalseNode('False')
        #return self.left.eval(context).token != self.right.eval(context).token

    def checktype(self, context):
        if not self.left.checktype(context) or not self.right.checktype(context):
            return False
        if self.left.type == 'int' or self.right.type == 'int':
            self.type = self.left.type
            return True
        return False


class ComparisonLtNode(BinaryExpNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)

    def eval(self, context):
        if self.left.eval(context).token < self.right.eval(context).token:
            return PrimaryTrueNode('True')
        else:
            return PrimaryFalseNode('False')
        #return self.left.eval(context).token < self.right.eval(context).token

    def checktype(self, context):
        if not self.left.checktype(context) or not self.right.checktype(context):
            return False
        if self.left.type == 'int' or self.right.type == 'int':
            self.type = self.left.type
            return True
        if self.left.type == 'str' or self.right.type == 'str':
            self.type = self.left.type
            return True
        return False


class ComparisonGtNode(BinaryExpNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)

    def eval(self, context):
        a = self.left.eval(context).token
        if self.left.eval(context).token > self.right.eval(context).token:
            return PrimaryTrueNode('True')
        else:
            return PrimaryFalseNode('False')
        #return self.left.eval(context).token > self.right.eval(context).token

    def checktype(self, context):
        if not self.left.checktype(context) or not self.right.checktype(context):
            return False
        if self.left.type == 'int' or self.right.type == 'int':
            self.type = self.left.type
            return True
        if self.left.type == 'str' or self.right.type == 'str':
            self.type = self.left.type
            return True
        return False


class ComparisonGteNode(BinaryExpNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)

    def eval(self, context):
        if self.left.eval(context).token >= self.right.eval(context).token:
            return PrimaryTrueNode('True')
        else:
            return PrimaryFalseNode('False')
        #return self.left.eval(context).token >= self.right.eval(context).token

    def checktype(self, context):
        if not self.left.checktype(context) or not self.right.checktype(context):
            return False
        if self.left.type == 'int' or self.right.type == 'int':
            self.type = self.left.type
            return True
        if self.left.type == 'str' or self.right.type == 'str':
            self.type = self.left.type
            return True
        return False


class ComparisonLteNode(BinaryExpNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)

    def eval(self, context):
        if self.left.eval(context).token <= self.right.eval(context).token:
            return PrimaryTrueNode('True')
        else:
            return PrimaryFalseNode('False')
        #return self.left.eval(context).token <= self.right.eval(context).token

    def checktype(self, context):
        if not self.left.checktype(context) or not self.right.checktype(context):
            return False
        if self.left.type == 'int' or self.right.type == 'int':
            self.type = self.left.type
            return True
        if self.left.type == 'str' or self.right.type == 'str':
            self.type = self.left.type
            return True
        return False


class ComparisonEqEqNode(BinaryExpNode):
    def __init__(self, left, right) -> None:
        super().__init__(left, right)

    def eval(self, context):
        if self.left.eval(context).token == self.right.eval(context).token:
            return PrimaryTrueNode('True')
        else:
            return PrimaryFalseNode('False')
        #return self.left.eval(context).token == self.right.eval(context).token

    def checktype(self, context):
        if not self.left.checktype(context) or not self.right.checktype(context):
            return False
        if self.left.type == 'int' and self.right.type == 'int':
            self.type = self.left.type
            return True
        if self.left.type == 'str' or self.right.type == 'str':
            self.type = self.left.type
            return False
        return False


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class FuncNode(AstNodeChildren):
    def __init__(self, id, params, block, return_type) -> None:
        self.id = id
        self.params = params
        self.block = block
        self.return_type = return_type

    def eval(self, context):
        params_name = []
        for tup in self.params:
            params_name.append(tup[1])
        context.asing_value(self.id, (params_name, self.block))

    def checktype(self, context):
        if self.id in context.symbols.keys():
            print("Error! : Funcion id existente.")
            return False
        context.asing_value(self.id, (self.return_type.type, self.params))
        new_context = Context(context)
        for param in self.params:
            new_context.symbols[param[1]] = param[0].type
        bool__, returns_block_types = self.block.checktype(new_context)
        if not bool__ or not self.return_type.checktype(context):
            return False
        # for t in returns_block_types:
        #     if t != self.return_type.type:
        #         print("Error! : Inconcistencia en el tipo de valor retornado")
        #         return False
        self.type = self.return_type.type
        return True


class UnaryNode(AstNode):
    def __init__(self, exp_right) -> None:
        self.exp_right = exp_right


class UnaryNotNode(UnaryNode):
    def __init__(self, exp_right) -> None:
        self.exp_right = exp_right

    def eval(self, context):
        return not self.exp_right.eval(context).token

    def checktype(self, context):
        if not self.exp_right.checktype(context):
            return False
        if self.exp_right.type != 'bool':
            return False
        self.type = 'bool'
        return True


class UnaryMinusNode(UnaryNode):
    def __init__(self, exp_right) -> None:
        self.exp_right = exp_right

    def eval(self, context):
        return PrimaryNumberNode(- self.exp_right.eval(context).token)

    def checktype(self, context):
        if not self.exp_right.checktype(context):
            return False
        if self.exp_right.type != 'int':
            return False
        self.type = 'int'
        return True


class MinusNode(BinaryExpNode):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def eval(self, context):
        return PrimaryNumberNode(self.left.eval(context).token - self.right.eval(context).token)

    def checktype(self, context):
        if not self.left.checktype(context) or not self.right.checktype(context):
            return False
        if self.left.type != 'int' or self.right.type != 'int':
            return False

        self.type = 'int'
        return True


class PlusNode(BinaryExpNode):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def eval(self, context):
        a = self.left.eval(context).token
        b = self.right.eval(context).token
        return PrimaryNumberNode(self.left.eval(context).token + self.right.eval(context).token)

    def checktype(self, context):
        if not self.left.checktype(context) or not self.right.checktype(context):
            return False
        if self.left.type == 'int' or self.right.type == 'int':
            self.type = 'int'
            return True
        if self.left.type == 'str' or self.right.type == 'str':
            self.type = 'str'
            return True
        return False


class StarNode(BinaryExpNode):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def eval(self, context):
        return PrimaryNumberNode(self.left.eval(context).token * self.right.eval(context).token)

    def checktype(self, context):
        if not self.left.checktype(context) or not self.right.checktype(context):
            return False
        if self.left.type != 'int' or self.right.type != 'int':
            return False

        self.type = 'int'
        return True


class DivNode(BinaryExpNode):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def eval(self, context):
        return PrimaryNumberNode(self.left.eval(context).token / self.right.eval(context).token)

    def checktype(self, context):
        if not self.left.checktype(context) or not self.right.checktype(context):
            return False
        if self.left.type != 'int' or self.right.type != 'int':
            return False

        self.type = 'int'
        return True


class CallNode(AstNode):
    def __init__(self, primary) -> None:
        self.primary = primary


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class CallArgsNode(CallNode):
    def __init__(self, primary, args) -> None:
        super().__init__(primary)
        self.args = args

    def eval(self, context):
        temp = None
        new_context = Context(context)
        if new_context.find_value(self.primary.id) != None:
            if len(self.args) != len(new_context.find_value(self.primary.id)[0]):

                print("Error! : Llamada a funcion con mas parametros de los que recibe")
            for i, name_var in enumerate(new_context.find_value(self.primary.id)[0]):
                new_context.asing_value(name_var, self.args[i].eval(context))
            #try:
            new_context.find_value(self.primary.id)[1].eval(new_context)
            #except:
            #    return
        else:
            assert Exception("----")

    def checktype(self, context):
        if context.find_value(self.primary.id) == None:
            print("Error! : Llamado a funcion fuera de contexto")
            return False
        if not self.primary.checktype(context):
            return False
        self.type = context.find_value(self.primary.id)[0]
        return True


class PrimaryNode(AstNode):
    def __init__(self, token) -> None:
        self.token = token

    def eval(self, context):
        return self


class PrimaryFalseNode(PrimaryNode):
    def __init__(self, token) -> None:
        super().__init__(token)

    def eval(self, context):
        return self

    def checktype(self, context):
        self.type = 'bool'
        return True


class PrimaryTrueNode(PrimaryNode):
    def __init__(self, token) -> None:
        super().__init__(token)

    def eval(self, context):
        return self

    def checktype(self, context):
        self.type = 'bool'
        return True


class PrimaryNumberNode(PrimaryNode):
    def __init__(self, token) -> None:
        super().__init__(token)

    def eval(self, context):
        return self

    def checktype(self, context):
        self.type = 'int'
        return True


class PrimaryStringNode(PrimaryNode):
    def __init__(self, token) -> None:
        super().__init__(token)

    def eval(self, context):
        return self

    def checktype(self, context):
        self.type = 'str'
        return True


class PrimaryIdNode(PrimaryNode):  # !revisar
    def __init__(self, token) -> None:
        super().__init__(token)

    def eval(self, context):
        if self.token in context.key():
            return context.symbols[self.token]
        else:
            raise Exception("Variable fuera del contexto")

    def checktype(self, context):
        if self.token not in context.key():
            return False
        self.type = self.token
        return True


class PrimaryNilNode(PrimaryNode):
    def __init__(self, token) -> None:
        super().__init__(token)

    def eval(self, context):
        return self

    def checktype(self, context):
        self.type = None
        return True


class ArgumentsNode(AstNode):  # ! revisar
    def __init__(self, expr) -> None:
        self.expr = expr

    def eval(self, context):
        for ex in self.expr:
            ex.eval(context)

    def checktype(self, context):
        return True


class CallVar(AstNode):
    def __init__(self, id) -> None:
        self.id = id

    def eval(self, context):
        if context.find_value(self.id) != None:
            if type(context.find_value(self.id)) is tuple:
                return context.find_value(self.id)[1].eval(context)
            else:
                return context.find_value(self.id)
        else:
             assert Exception("----")

        # if self.id in context: #Antiguo
        #     if type(context.symbols[self.id]) is tuple:
        #         return context.symbols[self.id][1].eval(context)
        #     else:
        #         return context.symbols[self.id]
        # else:
        #     assert Exception("----")

    def checktype(self, context):  # !revisar
        # if self.id in context:
        #     print("Error! : Id de variable existente")
        #     return False
        # self.type = context[self.id][0]

        # if not self.id in context.keys(): #Antiguo
        #     return False
        if context.find_value(self.id) == None:
            return  False
        if type(context.find_value(self.id)) == tuple:
            self.type = context.find_value(self.id)[0]
        # if type(context[self.id]) == list:

        else:
            self.type = context.symbols[self.id]
        return True


class TypeIntNode(AstNode):
    def __init__(self, type=None) -> None:
        self.type = type

    def checktype(self, context):
        self.type = 'int'
        return True

    def eval(self, context):
        pass


class TypeBoolNode(AstNode):
    def __init__(self, type=None) -> None:
        self.type = type

    def checktype(self, context):
        self.type = 'bool'
        return True

    def eval(self, context):
        pass


class TypeVoidNode(AstNode):
    def __init__(self, type=None) -> None:
        self.type = type

    def checktype(self, context):
        self.type = -1
        return True

    def eval(self, context):
        pass
