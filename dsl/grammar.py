from ply.yacc import yacc
from dsl.nodes_ast import AssignNode, FuncNode
from nodes_ast import ArmyNode, MapNode, SimulationNode
from lexer import *


def p_simulation(p):  # S -> <Simulation> MAA </Simulation>
    '''Simulation : LT SIMULATION GT M A A LT DIV SIMULATION GT'''
    p[0] = SimulationNode(p[4], p[5], p[6])


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

# ? DECLARATION


def p_declaration_fun(p):  # Declaracion de funcion
    '''Declaration : FuncDecl'''


def p_declaration_var(p):  # Declaracion de variable
    '''Declaration : VarDecl'''


def p_declaration_statement(p):
    '''Declaration : Statement'''  # Declaracion de declarracion XD


def p_var_decl(p):
    '''VarDecl : VAR ID EQ Expression'''  # Variable

# ? STATEMENT


def p_statement_exp(p):  # Statement -> Expresion
    '''Statement : ExprStmt'''


def p_statement_while(p):
    '''Statement : WhileStmt'''  # Statement -> While


def p_statement_if(p):
    '''Statement : IfStmt'''  # Statement -> If


def p_statement_print(p):
    '''Statement : PrintStmt'''  # Statement -> Print


def p_statement_return(p):
    '''Statement : ReturnStmt'''  # Statement -> Return


def p_statement_block(p):
    '''Statement : Block'''  # Statement -> Block


def p_block(p):
    '''Block : OKEY Declaration CKEY'''  # Block -> Declaracion


def p_exp_stmt(p):
    '''ExprStmt : Expression SEMICOLOM'''  # ExpresionSt -> Expresion


def p_if_stmt(p):
    '''IfStmt : IF OPP Expression CPP Statement'''  # !duda con el else #IfSt


def p_print_stmt(p):
    '''PrintStmt : PRINT Expression SEMICOLOM'''  # PrintSt


def p_return_stmt(p):
    '''ReturnStmt : RETURN Expression SEMICOLOM'''  # ReturnSt


def p_while_stmt(p):
    '''WhileStmt : WHILE OPP Exprssion CLP Statement'''  # WhileSt

# ? EXPRESSION


def p_expression(p):  # Expresion
    '''Expression : Assignment'''


def p_assignment(p):  # ! Falta hacer type y value #Assign
    '''Assignment : TYPE ID EQ VALUE'''
    p[0] = AssignNode(p[1], p[2], p[4])


def p_assignment_logic_or(p):
    '''Assignment : Logic_or'''


def p_logic_or(p):
    '''Logic_or : Logic_and Logic_and_aster'''


def p_logic_and(p):  # And
    '''Logic_and : Equality Equality_aster'''


def p_logic_and_aster(p):
    '''Logic_and_aster : OR Logic_and Logic_and_aster'''


def p_logic_and_aster_eps(p):
    '''Logic_and_aster : empty'''


def p_equality_aster(p):  # Equality
    '''Equality_aster : AND Equality Equality_aster'''


def p_equality_aster_eps(p):
    '''Equality_aster : empty'''


def p_equality_a(p):
    '''Equality : Comparison Comparison_NOTEQ_aster'''


def p_equality_b(p):
    '''Equality : Comparison Comparison_EQEQ_aster'''


def p_comparison_eqeq_aster(p):  # Comparison ==
    '''Comparison_EQEQ_aster : EQEQ Comparison Comparison_EQEQ_aster'''


def p_comparisson_noteq_aster(p):
    '''Comparison_NOTEQ_aster : NOTEQ Comparison Comparison_NOTEQ_aster'''


def p_comparison_eqeq_aster_eps(p):
    '''Comparison_EQEQ_aster : empty'''


def p_comparison_noteq_aster_eps(p):  # Comparison !=
    '''Comparison_NOTEQ_aster : empty'''


def p_comparison_gt(p):  # Comparison >
    '''Comparison : Term Term_GT_aster'''


def p_term_gt_aster(p):
    '''Term_GT_aster : GT Term Term_GT_aster'''


def p_term_gt_aster_eps(p):
    '''Term_GT_aster : empty'''


def p_comparison_lt(p):  # Comparison <
    '''Comparison : Term Term_LT_aster'''


def p_term_lt_aster(p):
    '''Term_LT_aster : LT Term Term_LT_aster'''


def p_term_lt_aster_eps(p):
    '''Term_LT_aster : empty'''


def p_comparison_lte(p):  # Comparison <=
    '''Comparison : Term Term_LTE_aster'''


def p_term_lte_aster(p):
    '''Term_LTE_aster : LTE Term Term_LTE_aster'''


def p_term_lte_aster_eps(p):
    '''Term_LTE_aster : empty'''


def p_comparison_gte(p):  # Comparison >=
    '''Comparison : Term Term_GTE_aster'''


def p_term_gte_aster(p):
    '''Term_GTE_aster : GTE Term Term_GTE_aster'''


def p_term_gte_aster_eps(p):
    '''Term_GTE_aster : empty'''


def p_fact_minus(p):  # Term -
    '''Term : Factor Factor_minus_aster'''


def p_factor_minus_aster(p):
    '''Factor_minus_aster : MINUS Factor Factor_Aster'''


def p_factor_minus_aster_eps(p):
    '''Factor_minus_aster : empty'''


def p_factor_plus(p):
    '''Term : Factor Factor_plus_aster'''


def p_factor_plus_aster(p):
    '''Factor_plus_aster : PLUS Factor Factor_plus_aster'''


def p_factor_plus_aster_eps(p):
    '''Factor_plus_aster : empty'''


def p_unary_plus(p):
    '''Factor : Unary Unary_plus_aster'''


def p_unary_plus_aster(p):
    '''Unary_plus_aster : PLUS Unary Unary_plus_aster'''


def p_unary_plus_aster_eps(p):
    '''Unary_plus_aster : empty'''


def p_unary_div(p):
    '''Factor : Unary Unary_div_aster'''


def p_unary_div_aster(p):
    '''Unary_div_aster : PLUS Unary Unary_div_aster'''


def p_unary_plus_aster_eps(p):
    '''Unary_div_aster : empty'''


def p_unary_not(p):
    '''Unary : NOT Unary'''


def p_unary_call(p):
    '''Unary : Call'''


def p_call(p):  # call
    '''Call : Primary Arguments_aster '''


def p_arguments_aster(p):
    '''Arguments_aster : OPP Arguments CLP'''


def p_arguments_aster_eps(p):
    '''Arguments_aster : empty'''


def p_call_id_aster(p):
    '''Call : Primary Id_aster'''


def p_id_aster(p):
    '''Id_aster : DOT ID'''


def id_aster_eps(p):
    '''Id_aster : emptys'''


def primary_true(p):
    '''Primary : TRUE'''


def primary_false(p):
    '''Primary : FALSE'''


def primary_false(p):
    '''Primary : FALSE'''


def primary_number(p):
    '''Primary : NUMBER'''


def primary_string(p):
    '''Primary : STRING'''  # ! TNGO Q HACER EL TIPO STRING


def p_primary_id(p):
    '''Primary : ID'''


def p_primary_expression(p):
    '''Primary : Expressions'''


def p_arguments(p):
    '''Arguments : Expression Expression_aster'''


def p_expression_aster(p):
    '''Expression_aster : COMMA Expression_aster'''


def p_expression_aster_eps(p):
    '''Expression_aster : Empty'''

#!Function


def p_fun_decl(p):
    '''FuncDecl : FUNC Function'''


def p_function(p):
    '''Function : ID OPP Params CLP Block '''
    p[0] = FuncNode(p[1],p[3],p[5])

def p_params(p):
    '''Params : TYPE ID ParamsAster'''
    p[0] = [(p[1], p[2])] + p[3]


def p_params_eps(p):
    '''Params :empty'''
    p[0] = []


def p_params_aster(p):
    '''ParamsAster : COMMA Params ParamsAster'''
    p[0] = p[2] + p[3]


def p_params_aster_eps(p):
    '''ParamsAster : empty'''
    p[0] = []




#!EndFunction


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
parser = yacc()
result = parser.parse(
    " <Sim><Map>row = 5;col = 5;</Map><Army>army_name = 1;amount = 5;</Army><Army>army_name = 2;amount = 5;</Army></Sim>")
print(result)
