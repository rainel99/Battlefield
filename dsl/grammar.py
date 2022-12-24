import ply.yacc as yacc
from lexer import *


def p_simulation(p):  # S -> <Simulation> MAA <Simulation/>
    'S : CmpOp.Lt Simulation CmpOp.Gt MAA CmpOp.Lt Simulation AlgebraicOperators.Div CmpOp.Gt'


def p_map(p):  # M -> <Map> M' <Map/>
    'M : CmpOp.LT Map> M\' CmpOp.Gt Map CmpOp.Lt AlgebraicOperators.Div CmpOp.Gt '


def p_map_prime_row(p):
    # M' -> row = number ; M'
    #    | col = number ; M'
    #    | eps
    'M\' : row Equal.Eq Numeric Semicolom.Semicolom M\''
    if p[1] == 'row':
        pass
    if p[1] == 'col':
        pass
    else:
        pass


def p_army(p):
    # A -> <Army> A' <Army/>
    'A : <Army> A\' <Army\>'


def p_army_(p):
    # A' -> id = name ; A'
    #    | id = number ; A'
    #    | eps
    'A\' : Id.Id Equal.Eq Numeric Semicolom.Semicolom A\''
