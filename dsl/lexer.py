from lib2to3.pgen2.token import RPAR
import re
from enum import Enum
import token

from sympy import true




class BoolEnum(Enum):
    false = 0 
    true = 1


class ComparisonOperator(Enum):
    gt = 0 #mayor que >
    lt = 1 # menor que <
    eqeq = 2 #igual igual ==
    noteq = 3 #distinto !=
    gte = 4 # mayor igual >=
    lte = 5 # menor igual <=
    Or = 6 # ó
    And = 7 # y
    Not = 8 # no


class AlgebraicOperators(Enum):
    plus = 0 # +
    minus = 1 # -
    star = 2 # *
    div = 3 # /
    mod = 4 # %


class AssignmentOperator(Enum):
    eq = 0


class GroupingOperators(Enum):
    opar = 0 #(
    cpar = 1 #)
    okey = 2 #{
    ckey = 3 #}
    ocor = 4 #[
    ccor = 5 #]


class Comma(Enum):
    comma = 0


class Dot(Enum):
    dot = 0


class Semicolom(Enum):
    semicolom = 0


class NumericEnum(Enum):
    float = 0
    int = 1


class Id(Enum):
    id = 0

class While(Enum):
    While = 0

class If(Enum):
    If = 0






class Lexer:
    pass
    

    def split_text(self,text):
        buffer =""
        splitted_text = []
        for c in text:
            if c == ' ' or c == '\n':
                if len(buffer) > 0:
                    splitted_text.append(buffer)
                buffer = ""
            else:
                buffer += c
        if len(buffer) > 0:
            splitted_text.append(buffer)
        return splitted_text

    def tokenize_text(self,text):
        result = []
        splitted_text = self.split_text(text)
        for i,cadena in enumerate(splitted_text):
            for j, rex in enumerate(regulars_expressions):
                mtch = re.match(rex,cadena)
                if mtch:
                    #en el sgt if se ve si la cadena q tngo hasta ahora no es una palabra clave, si lo es, anhado un token de palabra clave
                    subs = cadena[mtch.span()[0]:mtch.span()[1]]
                    if subs in key_words.keys():
                        result.append(Token(subs,key_words[subs]))
                        if len(cadena[mtch.span()[1]:]) > 1:
                            splitted_text.insert(i + 1,cadena[mtch.span()[1]:])
                        break
                    else:  
                        result.append(Token(cadena[:mtch.span()[1]],regulars_expressions[rex]))
                        if len(cadena[mtch.span()[1]:]) > 0:
                            splitted_text.insert(i + 1,cadena[mtch.span()[1]:])
                        break
        return result



class Token():
    def __init__(self,lex,token_type) -> None:
        self.lex = lex
        self.token_type = token_type

    def __str__(self) -> str:
        return self.lex
    
    def __repr__(self) -> str:
        return "Token(" + "'" +  self.lex + "'" + "," + str(self.token_type) + ")"

key_words = {
            'if' : If.If,
            'while' : While.While 
            }


regulars_expressions = { 
    r'([a-zA-z])+': Id.id,
    r'([0-9])+': NumericEnum.int,
    r'false': BoolEnum.false,
    r'true' : BoolEnum.true,
    r'>'    : ComparisonOperator.gt,
    r'<'    : ComparisonOperator.lt,
    r'>='   :  ComparisonOperator.gte,
    r'<='   :  ComparisonOperator.lte,
    r'=='   :  ComparisonOperator.eqeq,
    r'!='   :  ComparisonOperator.noteq,
    r'Not' :  ComparisonOperator.Not,
    r'Or'  : ComparisonOperator.Or,
    r'And' : ComparisonOperator.And,
    r'\+'    : AlgebraicOperators.plus,
    r'/'    : AlgebraicOperators.div,
    r'-'    : AlgebraicOperators.minus,
    r'%'    : AlgebraicOperators.mod,
    r'\*'    : AlgebraicOperators.star,
    r'='    : AssignmentOperator.eq,
    r'\('    : GroupingOperators.opar,
    r'\)'    : GroupingOperators.cpar,
    r'\{'    : GroupingOperators.okey,
    r'\}'    : GroupingOperators.ckey,
    r'\['    : GroupingOperators.ocor,
    r'\]'    : GroupingOperators.ccor,
    r'\.'    : Dot.dot,
    r';'    : Semicolom.semicolom,
    r'\,'    : Comma.comma
}

a = 'rainel=1 , int inta =asd while While'

my_lexe = Lexer()
TOKENS = my_lexe.tokenize_text(a)
print(a)
print(TOKENS)

