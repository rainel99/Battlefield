from ply.yacc import yacc
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

# while True:

#     s = '''
#         <Sim>
#             <Map>
#                 row = 5;
#                 col = 5;
#             </Map>
#             <Army>
#                 army_name = 1;
#                 amount = 5;
#             </Army>
#             <Army>
#                 army_name = 2;
#                 amount = 5;
#             </Army>
#         </Sim>
#         '''
#     result = parser.parse(s)
#     print(result)
# # ast = parser.parse()
# # print(TOKENS)


# while True:
#     try:
#         s = input('calc > ')
#     except EOFError:
#         break
#     if not s:
#         continue
#     result = parser.parse(s)
#     print(result)
#!!!!!!!!!!!!!!!!!!!!
# Yacc example


# Get the token map from the lexer.  This is required.
# # from calclex import tokens


# def p_expression_plus(p):
#     'expression : expression PLUS term'
#     p[0] = p[1] + p[3]


# def p_expression_minus(p):
#     'expression : expression MINUS term'
#     p[0] = p[1] - p[3]


# def p_expression_term(p):
#     'expression : term'
#     p[0] = p[1]


# def p_term_times(p):
#     'term : term TIMES factor'
#     p[0] = p[1] * p[3]


# def p_term_div(p):
#     'term : term DIVIDE factor'
#     p[0] = p[1] / p[3]


# def p_term_factor(p):
#     'term : factor'
#     p[0] = p[1]


# def p_factor_num(p):
#     'factor : NUMBER'
#     p[0] = p[1]


# def p_factor_expr(p):
#     'factor : LPAREN expression RPAREN'
#     p[0] = p[2]

# # Error rule for syntax errors


# def p_error(p):
#     print("Syntax error in input!")


# # Build the parser
# parser = yacc()

# while True:
#     try:
#         s = input('calc > ')
#     except EOFError:
#         break
#     if not s:
#         continue
#     result = parser.parse(s)
#     print(result)
