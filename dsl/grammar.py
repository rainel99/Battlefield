from ply.yacc import yacc
from nodes_ast import *
from nodes_ast import ArmyNode, MapNode, SimulationNode
from lexer import *


def p_simulation(p):  # S -> <Simulation> MAA </Simulation>
    '''Simulation : LT SIMULATION GT M A A Program LT DIV SIMULATION GT'''
    p[0] = SimulationNode(p[4], p[5], p[6], p[7])


def p_map(p):  # M -> <Map> MapDetail <Map/>
    '''M : LT MAP GT MapDetail LT DIV MAP GT '''
    p[0] = MapNode(p[4])


def p_map_detail_row(p):
    '''MapDetail : ROW EQ NUMERIC SEMICOLOM MapDetail'''
    p[0] = [("ROW", p[3])] + p[5]


def p_map_detail_col(p):
    '''MapDetail : COL EQ NUMERIC SEMICOLOM MapDetail'''
    p[0] = [("COL", p[3])] + p[5]


def p_map_detail_eps(p):
    '''MapDetail : empty '''
    p[0] = []


def p_army(p):
    'A : LT ARMY GT ArmyDetail LT DIV ARMY GT'
    p[0] = ArmyNode(p[4])


def p_army_detail_name(p):
    '''ArmyDetail : ARMY_name EQ NUMERIC SEMICOLOM ArmyDetail'''
    p[0] = [("ARMY_name", p[3])] + p[5]


def p_army_detail_amount(p):
    '''ArmyDetail : AMOUNT EQ NUMERIC SEMICOLOM ArmyDetail '''
    p[0] = [("AMOUNT", p[3])] + p[5]


def p_army_detail_eps(p):
    '''ArmyDetail : empty'''
    p[0] = []
#!a partir de aqui es new


# def p_program_aster(p):
#     '''Program_aster : Program Program_aster'''
#     p[0] = [p[1]] + p[2]


# def p_program_eps(p):
#     '''Program_aster : empty'''
#     p[0] = []


def p_program(p):
    '''Program : Declaration_aster'''
    p[0] = ProgramNode(p[1])
# ? DECLARATION


def p_declaration_fun(p):  # Declaracion de funcion
    '''Declaration : FuncDecl '''
    p[0] = [p[1]]


def p_declaration_var(p):  # Declaracion de variable
    '''Declaration : VarDecl '''
    p[0] = [p[1]]


def p_declaration_statement(p):
    '''Declaration : Statement'''
    p[0] = [p[1]]


# def p_declaration_empty(p):
#     '''Declaration : empty'''
#     p[0] = []


def p_var_decl(p):
    '''VarDecl : Type_ ID EQ Expression SEMICOLOM'''
    p[0] = VarNode(p[1], p[2], p[4])


# ? STATEMENT


def p_statement_exp(p):  # Statement -> Expresion
    '''Statement : ExprStmt '''
    p[0] = p[1]


def p_statement_while(p):
    '''Statement : WhileStmt'''  # Statement -> While
    p[0] = p[1]


def p_statement_if(p):
    '''Statement : IfStmt'''  # Statement -> If
    p[0] = p[1]


def p_statement_print(p):
    '''Statement : PrintStmt'''  # Statement -> Print
    p[0] = p[1]


def p_statement_return(p):
    '''Statement : ReturnStmt'''  # Statement -> Return
    p[0] = p[1]


def p_statement_block(p):
    '''Statement : Block'''  # Statement -> Block
    p[0] = p[1]


def p_block(p):
    '''Block : OKEY Declaration_aster CKEY'''  # Block -> Declaracion
    p[0] = BlockNode(p[2])


def p_block_decl_aster(p):
    '''Declaration_aster : Declaration Declaration_aster'''
    p[0] = p[1] + p[2]


def p_block_decl_aster_eps(p):
    '''Declaration_aster : empty'''
    p[0] = []


def p_exp_stmt(p):
    '''ExprStmt : Expression SEMICOLOM'''  # ExpresionSt -> Expresion
    p[0] = p[1]


def p_if_stmt(p):
    '''IfStmt : IF OPP Expression CLP Statement Else_aster'''  # !duda con el else #IfSt
    p[0] = IfNode(p[3], p[5], p[6])


def p_else(p):
    '''Else_aster : ELSE Statement'''
    p[0] = ElseNode(p[2])


def p_else_eps(p):
    '''Else_aster : empty'''
    p[0] = None


def p_print_stmt(p):
    '''PrintStmt : PRINT Expression SEMICOLOM'''  # PrintSt
    p[0] = PrintNode(p[2])


def p_return_stmt(p):
    '''ReturnStmt : RETURN Expression SEMICOLOM'''  # ReturnSt
    p[0] = ReturnNode(p[2])


def p_while_stmt(p):
    '''WhileStmt : WHILE OPP Expression CLP Statement'''  # WhileSt
    p[0] = WhileNode(p[3], p[5])
# ? EXPRESSION


def p_expression(p):  # Expresion
    '''Expression : Assignment'''
    p[0] = p[1]


def p_assignment_(p):
    '''Assignment : ID EQ Logic_or'''
    p[0] = AssignNode_(p[1], p[3])


def p_assignment(p):
    '''Assignment : Type_ ID EQ Logic_or'''
    p[0] = AssignNode(p[1], p[2], p[4])


def p_assignment_logic_or(p):
    '''Assignment : Logic_or'''
    p[0] = p[1]


def p_logic_or(p):
    '''Logic_or : Logic_or OR Logic_and'''
    p[0] = LogicOrNode(p[1], p[3])


def p_logic_or_(p):
    '''Logic_or : Logic_and'''
    p[0] = p[1]


def p_logic_and(p):
    '''Logic_and : Logic_and AND Equality'''
    p[0] = LogicaAndNode(p[1], p[3])


def p_logic_and_(p):
    '''Logic_and : Equality'''
    p[0] = p[1]


def p_equality_eq(p):
    '''Equality : Equality NOTEQ Comparison'''
    p[0] = ComparisonNotEqNode(p[1], p[3])


def p_equality_noteq(p):
    '''Equality : Equality EQEQ Comparison'''
    p[0] = ComparisonEqEqNode(p[1], p[3])


def p_equality_(p):
    '''Equality : Comparison'''
    p[0] = p[1]


def p_comparison_gt(p):  # Comparison >
    '''Comparison : Comparison GT Term'''
    p[0] = ComparisonGtNode(p[1], p[3])


def p_comparison_lt(p):  # Comparison <
    '''Comparison : Comparison LT Term'''
    p[0] = ComparisonLtNode(p[1], p[3])


def p_comparison_lte(p):  # Comparison <=
    '''Comparison : Comparison LTE Term'''
    p[0] = ComparisonLteNode(p[1], p[3])


def p_comparison_gte(p):  # Comparison >=
    '''Comparison : Comparison GTE Term'''
    p[0] = ComparisonGteNode(p[1], p[3])


def p_comparison_(p):
    '''Comparison : Term'''
    p[0] = p[1]


def p_factor_minus(p):  # Term -
    '''Term : Term MINUS Factor'''
    p[0] = MinusNode(p[1], p[3])


def p_factor_plus(p):
    '''Term : Term PLUS Factor'''
    p[0] = PlusNode(p[1], p[3])


def p_factor_(p):
    '''Term : Factor'''
    p[0] = p[1]


def p_unary_star(p):
    '''Factor : Factor STAR Unary'''
    p[0] = StarNode(p[1], p[3])


def p_unary_div(p):
    '''Factor : Factor DIV Unary'''
    p[0] = DivNode(p[1], p[3])


def p_unary_(p):
    '''Factor : Unary'''
    p[0] = p[1]


def p_unary_not(p):
    '''Unary : NOT Unary'''
    p[0] = UnaryNotNode(p[2])


def p_unary_minus(p):
    '''Unary : MINUS Unary'''
    p[0] = UnaryMinusNode(p[2])


def p_unary_call(p):
    '''Unary : Call'''
    p[0] = p[1]


def p_call(p):  # call
    '''Call : Primary OPP Arguments CLP'''
    p[0] = CallArgsNode(p[1], p[3])


def p_call_(p):
    '''Call : Primary'''
    p[0] = p[1]


def p_arguments_aster_eps(p):
    '''Arguments : empty'''
    p[0] = []


# def p_call_id_aster(p):
#     '''Call : Primary Id_aster'''
#     p[0] = CallIdNode(p[1], p[2])


# def p_id_aster(p):
#     '''Id_aster : DOT ID'''
#     p[0] = p[1]


# def p_id_aster_eps(p):
#     '''Id_aster : empty'''
#     p[0] = []  # ! not sure


def p_primary_true(p):
    '''Primary : TRUE'''
    p[0] = PrimaryTrueNode(p[1])


def p_primary_false(p):
    '''Primary : FALSE'''
    p[0] = PrimaryFalseNode(p[1])


def p_primary_number(p):
    '''Primary : NUMERIC'''
    p[0] = PrimaryNumberNode(p[1])


def p_primary_nil(p):
    '''Primary : NIL'''
    p[0] = PrimaryNilNode(p[1])

# def primary_string(p):
#     '''Primary : STRING'''  # ! TNGO Q HACER EL TIPO STRING


def p_primary_id(p):
    '''Primary : ID'''
    p[0] = CallVar(p[1])


# def p_primary_expression(p):
#     '''Primary : OPP Arguments CLP'''
#     p[0] = p[2]  # !duda


def p_arguments(p):
    '''Arguments : Expression Expression_aster'''
    p[0] = [p[1]] + p[2]


def p_expression_aster(p):
    '''Expression_aster : COMMA Expression Expression_aster'''
    p[0] = [p[2]] + p[3]


def p_expression_aster_eps(p):
    '''Expression_aster : empty'''
    p[0] = []
#!Function


def p_fun_decl(p):
    '''FuncDecl : FUNC Function'''
    p[0] = p[2]


def p_function(p):
    '''Function : ID OPP Params CLP Block '''
    p[0] = FuncNode(p[1], p[3], p[5])


def p_params(p):
    '''Params : Type_ ID ParamsAster'''
    p[0] = [(p[1], p[2])] + p[3]


def p_params_eps(p):
    '''Params : empty'''
    p[0] = []


def p_params_aster(p):
    '''ParamsAster : COMMA Params ParamsAster'''
    p[0] = p[2] + p[3]


def p_params_aster_eps(p):
    '''ParamsAster : empty'''
    p[0] = []


#!EndFunction

def p_type_(p):
    '''Type_ : INT'''
    p[0] = p[1]


def p_error(p):
    print("Syntax error in input!")


def p_empty(p):
    'empty :'
    pass

# file = open("dsl/test.txt", 'r')
# text = file.read()
# file.close()


# TOKENS = my_lexe.tokenize_text(text)
# lexer = lex.lex()
file = open("dsl/test.txt")
lines = file.read()
parser = yacc.yacc()
result = parser.parse(lines)
result.eval()
# result = parser.parse(
#     " <Sim><Map>row = 5;col = 5;</Map><Army>army_name = 1;amount = 5;</Army><Army>army_name = 2;amount = 5;</Army> ;</Sim>")
print(result)
