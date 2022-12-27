from ply.yacc import yacc
from nodes_ast import ArmyNode, MapNode, SimulationNode
from lexer import *


def p_simulation(p):  # S -> <Simulation> MAA </Simulation>
    '''Simualation : CmpOp.Lt Simulation CmpOp.Gt Map Army Army CmpOp.Lt AlgebraicOperators.Div Simulation  CmpOp.Gt'''
    p[0] = SimulationNode(p[4], p[5], p[6])


def p_map(p):  # M -> <Map> MapDetail <Map/>
    '''M : CmpOp.LT Map CmpOp.Gt MapDetail CmpOp.Lt AlgebraicOperators.Div Map CmpOp.Gt '''
    p[0] = MapNode(p[4])


def p_map_detail_row(p):
    '''MapDetail : Row.row Equal.Eq Numeric.Int Semicolom.Semicolom MapDetail'''
    p[0] = [("row", p[3])] + p[5]


def p_map_detail_col(p):
    '''MapDetail : Col.col Equal.Eq Numeric.Int Semicolom.Semicolom MapDetail'''
    p[0] = [("col", p[3])] + p[5]


def p_map_detail_eps(p):
    '''MapDetail : empty '''
    p[0] = []


def p_army(p):
    # Army -> <Army> ArmyDetail' <Army/>
    'Army : CmpOp.Lt Army CmpOp.Gt ArmyDetail CmpOp.Lt AlgebraicOperators.Div Army CmpOp.Gt'
    p[0] = ArmyNode(p[4])


def p_army_detail_name(p):
    '''ArmyDetail : ArmyName.am Equal.Eq Numeric.Int Semicolom.Semicolom ArmyDetail'''
    p[0] = [("army_name", p[3])] + p[5]


def p_army_detail_amount(p):
    '''ArmyDetail : Amount.amount Equal.Eq Numeric.Int Semicolom.Semicolom ArmyDetail '''
    p[0] = [("amount", p[3])] + p[5]


def p_army_detail_eps(p):
    '''ArmyDetail : empty '''
    p[0] = []


# file = open("dsl/test.txt", 'r')
# text = file.read()
# file.close()


# my_lexe = Lexer()
# TOKENS = my_lexe.tokenize_text(text)

parser = yacc()
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
