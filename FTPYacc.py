from ply import yacc
from FTPLex import *


def p_url(t):
    "url : SCHEMA DOMAIN secondaryDomains TLD"

    #if len(t[1]+t[2]+t[3]+t[4]) > 64:
    #    raise Error()

    t[0] = t[2][:-1].lower()
    return t

def p_secondaryDomains(t):
    """secondaryDomains : DOMAIN secondaryDomains
                        | empty"""
    if t[1] == '':
        t[0] = str()
        return t

    t[0] = t[1] + t[2]
    return t

def p_empty(t):
    "empty : "

    t[0] = str()
    return t

def p_error(t):
    pass


parser = yacc.yacc(optimize=1)
