import re

TOKEN_SPECIFICATION = [
    ('KEYWORD', r'\bint\b'),       #int
    ('IDENTIFIER', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),  #x
    ('ASSIGN', r'='),              #=
    ('NUMBER', r'\b\d+\b'),        #20
    ('SEMICOLON', r';'),           #;
    ('WHITESPACE', r'\s+'),        # Whitespace (ignored)
]

def lexer(code):
    tokens = []
    combined_regex = '|'.join(f'(?P<{name}>{regex})' for name, regex in TOKEN_SPECIFICATION)
    for match in re.finditer(combined_regex, code):
        kind = match.lastgroup
        value = match.group()
        if kind != 'WHITESPACE': #whitespace
            tokens.append((kind, value))
    return tokens


source_code = "int x = 20;"
tokens = lexer(source_code)

for token in tokens:
    print(token)
