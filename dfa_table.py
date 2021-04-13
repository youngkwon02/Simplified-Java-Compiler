import string
LETTER = string.ascii_letters
DIGIT = string.digits
DIGIT_1TO9 = string.digits[1:9]
WHITESPACE = string.whitespace
SYMBOL_FOR_CHAR = ""
for symbol in string.printable:
    if len(symbol) == 1 and symbol != "'" and symbol not in WHITESPACE and symbol not in DIGIT:
        SYMBOL_FOR_CHAR += symbol

SYMBOL_FOR_STR = ""
for symbol in string.printable:
    if len(symbol) == 1 and symbol != '"' and symbol not in WHITESPACE and symbol not in DIGIT:
        SYMBOL_FOR_STR += symbol

dfa_table = {
    "VTYPE": {
        "T0": {"i":"T1", "c":"T2", "b":"T3", "S":"T4", "FINAL":False},
        "T1": {"n":"T5", "FINAL":False},
        "T2": {"h":"T6", "FINAL":False},
        "T3": {"o":"T7", "FINAL":False},
        "T4": {"t":"T8", "FINAL":False},
        "T5": {"t":"T9", "FINAL":False},
        "T6": {"a":"T10", "FINAL":False},
        "T7": {"o":"T11", "FINAL":False},
        "T8": {"r":"T12", "FINAL":False},
        "T9": {"FINAL":True},
        "T10": {"r":"T13", "FINAL":False},
        "T11": {"l":"T14", "FINAL":False},
        "T12": {"i":"T15", "FINAL":False},
        "T13": {"FINAL":True},
        "T14": {"e":"T16", "FINAL":False},
        "T15": {"n":"T17", "FINAL":False},
        "T16": {"a":"T18", "FINAL":False},
        "T17": {"g":"T19", "FINAL":False},
        "T18": {"n":"T20", "FINAL":False},
        "T19": {"FINAL":True},
        "T20": {"FINAL":True}
    },
    "SIGNED_INTEGER": {
        "T0": {"0":"T3", "-":"T1", DIGIT_1TO9:"T2", "FINAL":False},
        "T1": {DIGIT_1TO9:"T2", "FINAL":False},
        "T2": {DIGIT:"T2", "FINAL":True},
        "T3": {"FINAL":True}
    },
    "SINGLE_CHARACTER": {
        "T0": {"'":"T1", "FINAL":False},
        "T1": {SYMBOL_FOR_CHAR:"T2", DIGIT:"T3", " ":"T4", "FINAL":False},
        "T2": {"'":"T5", "FINAL":False},
        "T3": {"'":"T5", "FINAL":False},
        "T4": {"'":"T5", "FINAL":False},
        "T5": {"FINAL": True}
    },
    "BOOLEAN": {
        "T0": {"t":"T1", "f":"T5", "FINAL":False},
        "T1": {"r":"T2", "FINAL":False},
        "T2": {"u":"T3", "FINAL":False},
        "T3": {"e":"T4", "FINAL":False},
        "T4": {"FINAL":True},
        "T5": {"a":"T6", "FINAL":False},
        "T6": {"l":"T7", "FINAL":False},
        "T7": {"s":"T8", "FINAL":False},
        "T8": {"e":"T9", "FINAL":False},
        "T9": {"FINAL":True}
    },
    "LITERAL_STRING": {
        "T0": {'"':"T1", "FINAL":False},
        "T1": {'"':"T2", SYMBOL_FOR_STR:"T1", DIGIT:"T1", WHITESPACE:"T1", "FINAL":False},
        "T2": {"FINAL":True}
    },
    "IDENTIFIER": {
        "T0": {LETTER:"T1", "_":"T1", "FINAL":False},
        "T1": {LETTER:"T1", DIGIT:"T1", "_":"T1", "FINAL":True}
    },
    "KEYWORD": {
        "T0": {"i":"T1", "e":"T3", "w":"T6", "c":"T10", "r":"T14", "p":"T19", "s":"T24", "m":"T29", "FINAL":False},
        "T1": {"f":"T2", "FINAL":False},
        "T2": {"FINAL":True},
        "T3": {"l":"T4", "FINAL":False},
        "T4": {"s":"T5", "FINAL":False},
        "T5": {"e":"T2", "FINAL":False},
        "T6": {"h":"T7", "FINAL":False},
        "T7": {"i":"T8", "FINAL":False},
        "T8": {"l":"T9", "FINAL":False},
        "T9": {"e":"T2", "FINAL":False},
        "T10": {"l":"T11", "FINAL":False},
        "T11": {"a":"T12", "FINAL":False},
        "T12": {"s":"T13", "FINAL":False},
        "T13": {"s":"T2", "FINAL":False},
        "T14": {"e":"T15", "FINAL":False},
        "T15": {"t":"T16", "FINAL":False},
        "T16": {"u":"T17", "FINAL":False},
        "T17": {"r":"T18", "FINAL":False},
        "T18": {"n":"T2", "FINAL":False},
        "T19": {"u":"T20", "FINAL":False},
        "T20": {"b":"T21", "FINAL":False},
        "T21": {"l":"T22", "FINAL":False},
        "T22": {"i":"T23", "FINAL":False},
        "T23": {"c":"T2", "FINAL":False},
        "T24": {"t":"T25", "FINAL":False},
        "T25": {"a":"T26", "FINAL":False},
        "T26": {"t":"T27", "FINAL":False},
        "T27": {"i":"T28", "FINAL":False},
        "T28": {"c":"T2", "FINAL":False},
        "T29": {"a":"T30", "FINAL":False},
        "T30": {"i":"T31", "FINAL":False},
        "T31": {"n":"T2", "FINAL":False},

    },
    "ARITHMETIC_OPERATOR": {
        "T0": {"+":"T1", "-":"T1", "*":"T1", "/":"T1", "FINAL":False},
        "T1": {"FINAL": True}
    },
    "ASSIGNMENT_OPERATOR": {
        "T0": {"=":"T1", "FINAL":False},
        "T1": {"FINAL": True}
    },
    "COMPARISON_OPERATOR": {
        "T0": {"<":"T1", ">":"T2", "=":"T3", "!":"T4", "FINAL":False},
        "T1": {"=":"T5", "FINAL":True},
        "T2": {"=":"T5", "FINAL":True},
        "T3": {"=":"T5", "FINAL":False},
        "T4": {"=":"T5", "FINAL":False},
        "T5": {"FINAL":True}
    },
    "TERMINATING_SYMBOL": {
        "T0": {";":"T1", "FINAL":False},
        "T1": {"FINAL": True}
    },
    "LEFT_PAREN": {
        "T0": {"(":"T1", "FINAL":False},
        "T1": {"FINAL": True}
    },
    "RIGHT_PAREN": {
        "T0": {")":"T1", "FINAL":False},
        "T1": {"FINAL": True}
    },
    "LEFT_BRACE": {
        "T0": {"{":"T1", "FINAL":False},
        "T1": {"FINAL": True}
    },
    "RIGHT_BRACE": {
        "T0": {"}":"T1", "FINAL":False},
        "T1": {"FINAL": True}
    },
    "LEFT_BRANKET": {
        "T0": {"[":"T1", "FINAL":False},
        "T1": {"FINAL": True}
    },
    "RIGHT_BRANKET": {
        "T0": {"]":"T1", "FINAL":False},
        "T1": {"FINAL": True}
    },
    "COMMA": {
        "T0": {",":"T1", "FINAL":False},
        "T1": {"FINAL": True}
    },
    "WHITESPACE": {
        "T0": {WHITESPACE:"T1", "FINAL":False},
        "T1": {"FINAL": True}
    }
}