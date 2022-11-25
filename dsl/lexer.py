from argparse import _ArgumentGroup
import re
from enum import Enum
from shutil import register_unpack_format
import token

from cv2 import split



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
    or_ = 6 # ó
    and_ = 7 # y
    not_ = 8 # no


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


class Var(Enum):
    var = 0






class Lexer:
    def __init__(self,text) -> None:
        self.text = text
        self.tokens = self.tokenize_text()

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
        return splitted_text

    def tokenize_text(self):
        result = []
        splitted_text = self.split_text(self.text)
        for cadena in splitted_text:
            if cadena in convert_tokens.keys():
                result.append(convert_tokens[cadena])
                continue
            for i, rex in enumerate(regulars_expressions):
                if re.fullmatch(rex,cadena):
                    if i == 0:
                        result.append(Token(cadena,Var.var))
                    if i == 1:
                        result.append(Token(cadena,NumericEnum.int))
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

regulars_expressions = [r'([a-zA-z])+',
                        r'([0-9])+']


convert_tokens = { 
    'false': Token('false',BoolEnum.false),
    'true' : Token('true', BoolEnum.true),
    '>'    : Token('>', ComparisonOperator.gt),
    '<'    : Token('<', ComparisonOperator.lt),
    '>='   : Token('>=', ComparisonOperator.gte),
    '<='   : Token('<=', ComparisonOperator.lte),
    '=='   : Token('==', ComparisonOperator.eqeq),
    '!='   : Token('!=', ComparisonOperator.noteq),
    'not_' : Token('not_', ComparisonOperator.not_),
    'or_'  : Token('or_', ComparisonOperator.or_),
    'and_' : Token('and_', ComparisonOperator.and_),
    '+'    : Token('+', AlgebraicOperators.plus),
    '/'    : Token('/', AlgebraicOperators.div),
    '-'    : Token('-', AlgebraicOperators.minus),
    '%'    : Token('%', AlgebraicOperators.mod),
    '*'    : Token('*', AlgebraicOperators.star),
    '='    : Token('=', AssignmentOperator.eq),
    '('    : Token('(', GroupingOperators.opar),
    ')'    : Token(')', GroupingOperators.cpar),
    '{'    : Token('{', GroupingOperators.okey),
    '}'    : Token('}', GroupingOperators.ckey),
    '['    : Token('[', GroupingOperators.ocor),
    ']'    : Token(']', GroupingOperators.ccor),
    '.'    : Token('.', Dot.dot),
    ';'    : Token(';', Semicolom.semicolom),
    '.'    : Token('.', Dot.dot)
}

a = "products ( ) false  * + ;. 145 "

string_list = a.split('"')
word_list = []
for i in range(len(string_list)):
    if i % 2 == 0:
        word_list.extend(string_list[i].split())
    else:
        word_list.append(f'"{string_list[i]}"')

print(word_list)

my_lexe = Lexer(a)
tokens = my_lexe.tokenize_text()


print(tokens)


print(re.match("int", "inta"))