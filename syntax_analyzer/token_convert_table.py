# Token Convert Table
# It convert the lexical analyzer output tokens to syntax input tokens (e.g. Convert SIGNED_INTEGER to num)

TOKEN_CONVERT_TABLE = {
  "VTYPE": "vtype",
  "SIGNED_INTEGER": "num",
  "SINGLE_CHARACTER": "character",
  "BOOLEAN_STRING": "boolstr",
  "LITERAL_STRING": "literal",
  "IDENTIFIER": "id",
  "KEYWORD": {
    "if":"if",
    "else":"else",
    "while":"while",
    "return":"return",
    "class":"class"
  },
  "ARITHMETIC_OPERATOR": {
    "+":"addsub",
    "-":"addsub",
    "*":"multdiv",
    "/":"multdiv",
  },
  "ASSIGNMENT_OPERATOR": "assign",
  "COMPARISON_OPERATOR": "comp",
  "TERMINATING_SYMBOL": "semi",
  "ARGS_SEPERATING_COMMA": "comma",
  "COMMA": "comma",
  "LEFT_PAREN": "lparen",
  "RIGHT_PAREN": "rparen",
  "LEFT_BRACE": "lbrace",
  "RIGHT_BRACE": "rbrace",
  "LEFT_BRANKET": "lbranket",
  "RIGHT_BRANKET": "rbranket"
}