import re
from enum import Enum

from matplotlib.pyplot import close


class BoolEnum(Enum):
    false = 0 
    true = 1


class ComparisonOperator(Enum):
    Gt = 0 #mayor que >
    Lt = 1 # menor que <
    Eqeq = 2 #igual igual ==
    Noteq = 3 #distinto !=
    Gte = 4 # mayor igual >=
    Lte = 5 # menor igual <=
    Or = 6 # ó
    And = 7 # y
    Not = 8 # no


class AlgebraicOperators(Enum):
    Plus = 0 # +
    Minus = 1 # -
    Star = 2 # *
    Div = 3 # /
    Mod = 4 # %


class AssignmentOperator(Enum):
    Eq = 0


class GroupingOperators(Enum):
    Opar = 0 #(
    Cpar = 1 #)
    Okey = 2 #{
    Ckey = 3 #}
    Ocor = 4 #[
    Ccor = 5 #]


class Comma(Enum):
    Comma = 0


class Dot(Enum):
    Dot = 0


class Semicolom(Enum):
    Semicolom = 0


class NumericEnum(Enum):
    Int = 1


class Id(Enum):
    Id = 0

class While(Enum):
    While = 0

class If(Enum):
    If = 0




class Lexer:


    def tokenize_text(self,text):
        row = 0
        col = 0
        result = []
        
        splitted_text = text.split()
        for i,cadena in enumerate(splitted_text):
            if cadena == '\n':
                row += 1
                continue
            for rex in regulars_expressions:
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
        self.row = -1
        self.col = -1

    def __str__(self) -> str:
        return self.lex
    
    def __repr__(self) -> str:
        return "Token(" + "'" +  self.lex + "'" + "," + str(self.token_type) + ")"

key_words = {
            'if' : If.If,
            'while' : While.While, 
            'and' : ComparisonOperator.And,
            'or' : ComparisonOperator.Or,
            'not' : ComparisonOperator.Not,
            }


regulars_expressions = { 
    r'([0-9])+': NumericEnum.Int,
    r'>='   :  ComparisonOperator.Gte,
    r'<='   :  ComparisonOperator.Lte,
    r'=='   :  ComparisonOperator.Eqeq,
    r'!='   :  ComparisonOperator.Noteq,
    r'false': BoolEnum.false,
    r'true' : BoolEnum.true,
    r'='    : AssignmentOperator.Eq,
    r'>'    : ComparisonOperator.Gt,
    r'<'    : ComparisonOperator.Lt,
    # r'Not' :  ComparisonOperator.Not,
    # r'Or'  : ComparisonOperator.Or,
    # r'And' : ComparisonOperator.And,
    r'\+'    : AlgebraicOperators.Plus,
    r'/'    : AlgebraicOperators.Div,
    r'-'    : AlgebraicOperators.Minus,
    r'%'    : AlgebraicOperators.Mod,
    r'\*'    : AlgebraicOperators.Star,
    r'\('    : GroupingOperators.Opar,
    r'\)'    : GroupingOperators.Cpar,
    r'\{'    : GroupingOperators.Okey,
    r'\}'    : GroupingOperators.Ckey,
    r'\['    : GroupingOperators.Ocor,
    r'\]'    : GroupingOperators.Ccor,
    r'\.'    : Dot.Dot,
    r';'    : Semicolom.Semicolom,
    r'\,'    : Comma.Comma,
    r'([a-zA-z])+': Id.Id
}

a = '<Simulacion> body <Simualacion/>'
file = open("dsl/test.txt",'r')
text = file.read()
file.close()


my_lexe = Lexer()
TOKENS = my_lexe.tokenize_text(text)
print(a)
print(TOKENS)

