from ply import lex


tokens = (
    'SCHEMA',
    'DOMAIN',
    'TLD',
)


def t_SCHEMA(t):
    r'ftp:\/\/'
    return t

def t_DOMAIN(t):
    r'[a-zA-Z0-9]{1,20}\.'
    return t

def t_TLD(t):
    r'[a-zA-Z]{1,5}'
    return t

def t_newline(t):
    r'\n+'
    pass

def t_error(t):
    pass


lexer = lex.lex(optimize=1)

