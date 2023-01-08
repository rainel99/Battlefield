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
    'STRING',
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
t_STRING = r'\"([a-zA-z])+\"'
ID = r'([a-zA-z])+'


reserved = {
    "if": 'IF',
    "while": 'WHILE',
    "and": 'AND',
    "or": 'OR',
    "row": 'ROW',
    "col": 'COL',
    "else": "ELSE",
    "army_name": 'ARMY_name',
    "amount": 'AMOUNT',
    "Sim": "SIMULATION",
    "Army": "ARMY",
    "Map": "MAP",
    "func": "FUNC",
    "return": "RETURN",
    "print": "PRINT",
    "true": "TRUE",
    "false": "FALSE",
    "nil": "NIL",
    "int": "INT",
    "str": "STR",
    "void": "VOID",
    "bool": "BOOL"
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
