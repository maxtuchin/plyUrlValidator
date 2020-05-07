# lextab.py. This file automatically created by PLY (version 3.11). Don't edit!
_tabversion   = '3.10'
_lextokens    = set(('DOMAIN', 'SCHEMA', 'TLD'))
_lexreflags   = 64
_lexliterals  = ''
_lexstateinfo = {'INITIAL': 'inclusive'}
_lexstatere   = {'INITIAL': [('(?P<t_SCHEMA>ftp:\\/\\/)|(?P<t_DOMAIN>[a-zA-Z0-9]{1,20}\\.)|(?P<t_TLD>[a-zA-Z]{1,5})|(?P<t_newline>\\n+)', [None, ('t_SCHEMA', 'SCHEMA'), ('t_DOMAIN', 'DOMAIN'), ('t_TLD', 'TLD'), ('t_newline', 'newline')])]}
_lexstateignore = {'INITIAL': ''}
_lexstateerrorf = {'INITIAL': 't_error'}
_lexstateeoff = {}
