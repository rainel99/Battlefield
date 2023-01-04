from re import T
import ply.lex as lex

tokens = (
    'PLUS',
    'MINUS',
    'NUMERIC',
    'STAR',
    'DIV',
    'GT',
    'LT',
    'EQEQ',
    'NOTEQ',
    'GTE',
    'LTE',
    'EQ',
    'OPP',
    'CLP',
    'OKEY',
    'CKEY',
    'COMMA',
    'DOT',
    'SEMICOLOM',
    'ID',
    'NOT',
)

t_NOT = r'\!'
t_PLUS = r'\+'
t_MINUS = r'-'
t_EQEQ = r'=='
t_GTE = r'>='
t_LTE = r'<='
r_NOTEQ = r'!='
t_EQ = r'='
t_GT = r'>'
t_LT = r'<'
t_DIV = r'/'
t_STAR = r'\*'
t_OPP = r'\('
t_CLP = r'\)'
t_OKEY = r'\{'
t_CKEY = r'\}'
t_DOT = r'\.'
t_COMMA = r'\,'
t_SEMICOLOM = r';'
t_NIL = r'NIL'
ID = r'([a-zA-z])+'


reserved = {
    "if": 'IF',
    "while": 'WHILE',
    "and": 'AND',
    "or": 'OR',
    "row": 'ROW',
    "col": 'COL',
    "army_name": 'ARMY_name',
    "amount": 'AMOUNT',
    "Sim": "SIMULATION",
    "Army": "ARMY",
    "Map": "MAP",
    "return": "RETURN",
    "func": "FUNC",
    "return": "RETURN",
    "print": "PRINT",
    "true": "TRUE",
    "false": "FALSE",
    "nil": "NIL",
    "int": "INT",
}


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')    # Check for reserved words
    return t


def t_NUMERIC(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_COMMENT(t):
    r'\#.*'
    pass


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


tokens = list(reserved.values()) + list(tokens)


# file = open("dsl/test.txt", 'r')
# text = file.read()
# file.close()
# a = '<Simulacion> body <Simualacion/>'
lexer = lex.lex()
# lexer.input(text)

# # Tokenize
# while True:
#     tok = lexer.token()
#     if not tok:
#         break      # No more input
#     print(tok)


# class BoolTok(Enum):
#     false = 0
#     true = 1


# class CmpOp(Enum):
#     Gt = 0  # mayor que >
#     Lt = 1  # menor que <
#     Eqeq = 2  # igual igual ==
#     Noteq = 3  # distinto !=
#     Gte = 4  # mayor igual >=
#     Lte = 5  # menor igual <=
#     Or = 6  # ó
#     And = 7  # y
#     Not = 8  # no


# class AlgOp(Enum):
#     Plus = 0  # +
#     Minus = 1  # -
#     Star = 2  # *
#     Div = 3  # /
#     Mod = 4  # %


# class Equal(Enum):
#     Eq = 0


# class GroOp(Enum):
#     Opar = 0  # (
#     Cpar = 1  # )
#     Okey = 2  # {
#     Ckey = 3  # }
#     Ocor = 4  # [
#     Ccor = 5  # ]


# class Comma(Enum):
#     Comma = 0


# class Dot(Enum):
#     Dot = 0


# class Semicolom(Enum):
#     Semicolom = 0


# class Numeric(Enum):
#     Int = 0


# class Id(Enum):
#     Id = 0


# class While(Enum):
#     While = 0


# class If(Enum):
#     If = 0


# class Eps(Enum):
#     esp = 0


# class Row(Enum):
#     row = 0


# class Col(Enum):
#     col = 0


# class ArmyName(Enum):
#     am = 0


# class Amount(Enum):
#     amount = 0


# class Lexer:

#     def tokenize_text(self, text):
#         row = 0
#         col = 0
#         result = []

#         splitted_text = text.split()
#         for i, cadena in enumerate(splitted_text):
#             if cadena == '\n':
#                 row += 1
#                 continue
#             for rex in regulars_expressions:
#                 mtch = re.match(rex, cadena)
#                 if mtch:
#                     # en el sgt if se ve si la cadena q tngo hasta ahora no es una palabra clave, si lo es, anhado un token de palabra clave
#                     subs = cadena[mtch.span()[0]:mtch.span()[1]]
#                     if subs in key_words.keys():
#                         result.append(Token(subs, key_words[subs]))
#                         if len(cadena[mtch.span()[1]:]) > 1:
#                             splitted_text.insert(
#                                 i + 1, cadena[mtch.span()[1]:])
#                         break
#                     else:
#                         result.append(
#                             Token(cadena[:mtch.span()[1]], regulars_expressions[rex]))
#                         if len(cadena[mtch.span()[1]:]) > 0:
#                             splitted_text.insert(
#                                 i + 1, cadena[mtch.span()[1]:])
#                         break
#         return result


# class Token():
#     def __init__(self, value, token_type) -> None:
#         self.value = value
#         self.token_type = token_type
#         self.row = -1
#         self.col = -1

#     def __str__(self) -> str:
#         return self.value

#     def __repr__(self) -> str:
#         return "Token(" + "'" + self.value + "'" + "," + str(self.token_type) + ")"
# a = '<Simulacion> body <Simualacion/>'
# file = open("dsl/test.txt", 'r')
# text = file.read()
# file.close()


# my_lexe = Lexer()
# TOKENS = my_lexe.tokenize_text(text)
# print(a)
# print(TOKENS)
