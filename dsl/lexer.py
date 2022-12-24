from matplotlib.pyplot import close
import re
from enum import Enum
<< << << < HEAD


class BoolEnum(Enum):
    false = 0
    true = 1


class ComparisonOperator(Enum):
    Gt = 0  # mayor que >
    Lt = 1  # menor que <
    Eqeq = 2  # igual igual ==
    Noteq = 3  # distinto !=
    Gte = 4  # mayor igual >=
    Lte = 5  # menor igual <=
    Or = 6  # ó
    And = 7  # y
    Not = 8  # no


class AlgebraicOperators(Enum):
    Plus = 0  # +
    Minus = 1  # -
    Star = 2  # *
    Div = 3  # /
    Mod = 4  # %


class AssignmentOperator(Enum):
    Eq = 0


class GroupingOperators(Enum):
    Opar = 0  # (
    Cpar = 1  # )
    Okey = 2  # {
    Ckey = 3  # }
    Ocor = 4  # [
    Ccor = 5  # ]


== == == =


class BoolTok(Enum):
    false = 0
    true = 1


class CmpOp(Enum):
    Gt = 0  # mayor que >
    Lt = 1  # menor que <
    Eqeq = 2  # igual igual ==
    Noteq = 3  # distinto !=
    Gte = 4  # mayor igual >=
    Lte = 5  # menor igual <=
    Or = 6  # ó
    And = 7  # y
    Not = 8  # no


class AlgOp(Enum):
    Plus = 0  # +
    Minus = 1  # -
    Star = 2  # *
    Div = 3  # /
    Mod = 4  # %


class Equal(Enum):
    Eq = 0


class GroOp(Enum):
    Opar = 0  # (
    Cpar = 1  # )
    Okey = 2  # {
    Ckey = 3  # }
    Ocor = 4  # [
    Ccor = 5  # ]


>>>>>> > strategy_combat


class Comma(Enum):
    Comma = 0


class Dot(Enum):
    Dot = 0


class Semicolom(Enum):
    Semicolom = 0


class Numeric(Enum):
    Int = 0


class Id(Enum):
    Id = 0


class While(Enum):
    While = 0


class If(Enum):
    If = 0


class Eps(Enum):
    esp = 0


class Lexer:

    def tokenize_text(self, text):
        row = 0
        col = 0
        result = []

        splitted_text = text.split()
        for i, cadena in enumerate(splitted_text):
            if cadena == '\n':
                row += 1
                continue
            for rex in regulars_expressions:
                mtch = re.match(rex, cadena)
                if mtch:
                    # en el sgt if se ve si la cadena q tngo hasta ahora no es una palabra clave, si lo es, anhado un token de palabra clave
                    subs = cadena[mtch.span()[0]:mtch.span()[1]]
                    if subs in key_words.keys():
                        result.append(Token(subs, key_words[subs]))
                        if len(cadena[mtch.span()[1]:]) > 1:
                            splitted_text.insert(
                                i + 1, cadena[mtch.span()[1]:])
                        break
                    else:
                        result.append(
                            Token(cadena[:mtch.span()[1]], regulars_expressions[rex]))
                        if len(cadena[mtch.span()[1]:]) > 0:
                            splitted_text.insert(
                                i + 1, cadena[mtch.span()[1]:])
                        break
        return result


class Token():
    def __init__(self, value, token_type) -> None:
        self.value = value
        self.token_type = token_type
        self.row = -1
        self.col = -1

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return "Token(" + "'" + self.value + "'" + "," + str(self.token_type) + ")"


key_words = {
    'if': If.If,
    'while': While.While,
    'and': CmpOp.And,
    'or': CmpOp.Or,
    'not': CmpOp.Not,
    'eps': Eps.esp,
}


regulars_expressions = {
    r'([0-9])+': Numeric.Int,
    r'>=':  CmpOp.Gte,
    r'<=':  CmpOp.Lte,
    r'==':  CmpOp.Eqeq,
    r'!=':  CmpOp.Noteq,
    r'false': BoolTok.false,
    r'true': BoolTok.true,
    r'=': Equal.Eq,
    r'>': CmpOp.Gt,
    r'<': CmpOp.Lt,
    # r'Not' :  CmpOp.Not,
    # r'Or'  : CmpOp.Or,
    # r'And' : CmpOp.And,
    r'\+': AlgOp.Plus,
    r'/': AlgOp.Div,
    r'-': AlgOp.Minus,
    r'%': AlgOp.Mod,
    r'\*': AlgOp.Star,
    r'\(': GroOp.Opar,
    r'\)': GroOp.Cpar,
    r'\{': GroOp.Okey,
    r'\}': GroOp.Ckey,
    r'\[': GroOp.Ocor,
    r'\]': GroOp.Ccor,
    r'\.': Dot.Dot,
    r';': Semicolom.Semicolom,
    r'\,': Comma.Comma,
    r'([a-zA-z])+': Id.Id
}

a = '<Simulacion> body <Simualacion/>'
file = open("dsl/test.txt", 'r')
text = file.read()
file.close()


my_lexe = Lexer()
TOKENS = my_lexe.tokenize_text(text)
print(a)
print(TOKENS)
