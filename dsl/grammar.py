import ply.yacc as yacc
from dsl.nodes_ast import ArmyNode, MapNode, SimulationNode
from lexer import *




def p_simulation(p):  # S -> <Simulation> MAA </Simulation>
    '''Simualation : CmpOp.Lt Simulation CmpOp.Gt MapDetail Army Army CmpOp.Lt AlgebraicOperators.Div Simulation  CmpOp.Gt'''
    p[0] = SimulationNode(p[4], p[5], p[6])


def p_map(p):  # M -> <Map> MapDetail <Map/>
    '''M : CmpOp.LT Map CmpOp.Gt MapDetail CmpOp.Lt AlgebraicOperators.Div Map CmpOp.Gt '''
    p[0] = MapNode(p[4])


def p_map_detail_row(p):
    # MapDetail -> row = number ; M'
    #    | col = number ; M'
    #    | eps
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
    # A' -> army_name = name ; ArmyDetail
    #    | amount = number ; ArmyDetail
    #    | eps
    '''ArmyDetail : ArmyName.am Equal.Eq Numeric.Int Semicolom.Semicolom ArmyDetail'''
    p[0] = [("army_name", p[3])] + p[5]


def p_army_detail_amount(p):
    '''ArmyDetail : Amount.amount Equal.Eq Numeric.Int Semicolom.Semicolom ArmyDetail '''
    p[0] = [("amount", p[3])] + p[5]


def p_army_detail_eps(p):
    '''ArmyDetail : empty '''
