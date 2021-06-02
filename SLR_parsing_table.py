SLR_PARSING_TABLE = [
  # State 0
  {
    "vtype": "s5",
    "class": "s6",
    "$": "r4",
    "CODE": "1",
    "VDECL": "2",
    "FDECL": "3",
    "CDECL": "4"
  },
  # State 1
  {
    "$": "acc"
  },
  # State 2
  {
    "vtype": "s5",
    "class": "s6",
    "$": "r4",
    "CODE": "7",
    "VDECL": "2",
    "FDECL": "3",
    "CDECL": "4"
  },
  # State 3
  {
    "vtype": "s5",
    "class": "s6",
    "$": "r4",
    "CODE": "8",
    "VDECL": "2",
    "FDECL": "3",
    "CDECL": "4"
  },
  # State 4
  {
    "vtype": "s5",
    "class": "s6",
    "$": "r4",
    "CODE": "9",
    "VDECL": "2",
    "FDECL": "3",
    "CDECL": "4"
  },
  # State 5
  {
    "id": "s10",
    "ASSIGN": "11"
  },
  # State 6
  {
    "id": "s12"
  },
  # State 7
  {
    "$": "r1"
  },
  # State 8
  {
    "$": "r2"
  },
  # State 9
  {
    "$": "r3"
  },
  # State 10
  {
    "semi": "s13",
    "assign": "s15",
    "lparen": "s14"
  },
  # State 11
  {
    "semi": "s16"
  },
  # State 12
  {
    "lbrace": "s17"
  },
  # State 13
  {
    "vtype": "r5",
    "id": "r5",
    "rbrace": "r5",
    "if": "r5",
    "while": "r5",
    "return": "r5",
    "class": "r5",
    "$": "r5"
  },
  # State 14
  {
    "vtype": "s19",
    "rparen": "r21",
    "ARG": "18"
  },
  # State 15
  {
    "id": "s28",
    "literal": "s22",
    "character": "s23",
    "boolstr": "s24",
    "lparen": "s27",
    "num": "s29",
    "RHS": "20",
    "EXPR": "21",
    "T": "25",
    "F": "26",
  },
  # State 16
  {
    "vtype": "r6",
    "id": "r6",
    "rbrace": "r6",
    "if": "r6",
    "while": "r6",
    "return": "r6",
    "class": "r6",
    "$": "r6"
  },
  # State 17
  {
    "vtype": "s5",
    "rbrace": "r39",
    "VDECL": "31",
    "FDECL": "32",
    "ODECL": "30"
  },
  # State 18
  {
    "rparen": "s33"
  },
  # State 19
  {
    "id": "s34"
  },
  # State 20
  {
    "semi": "r7"
  },
  # State 21
  {
    "semi": "r8"
  },
  # State 22
  {
    "semi": "r9"
  },
  # State 23
  {
    "semi": "r10"
  },
  # State 24
  {
    "semi": "r11"
  },
  # State 25
  {
    "semi": "r13",
    "addsub": "s35",
    "rparen": "r13"
  },
  # State 26
  {
    "semi": "r15",
    "addsub": "r15",
    "multdiv": "s36",
    "rparen": "r15"
  },
  # State 27
  {
    "id": "s28",
    "lparen": "s27",
    "num": "s29",
    "EXPR": "37",
    "T": "25",
    "F": "26"
  },
  # State 28
  {
    "semi": "r17",
    "addsub": "r17",
    "multdiv": "r17",
    "rparen": "r17"
  },
  # State 29
  {
    "semi": "r18",
    "addsub": "r18",
    "multdiv": "r18",
    "rparen": "r18"
  },
  # State 30
  {
    "rbrace": "s38"
  },
  # State 31
  {
    "vtype": "s5",
    "rbrace": "r39",
    "VDECL": "31",
    "FDECL": "32",
    "ODECL": "39"
  },
  # State 32
  {
    "vtype": "s5",
    "rbrace": "r39",
    "VDECL": "31",
    "FDECL": "32",
    "ODECL": "40"
  },
  # State 33
  {
    "lbrace": "s41"
  },
  # State 34
  {
    "rparen": "r23",
    "comma": "s43",
    "MOREARGS": "42"
  },
  # State 35
  {
    "id": "s28",
    "lparen": "s27",
    "num": "s29",
    "EXPR": "44",
    "T": "25",
    "F": "26"
  },
  # State 36
  {
    "id": "s28",
    "lparen": "s27",
    "num": "s29",
    "T": "45",
    "F": "26"
  },
  # State 37
  {
    "rparen": "s46"
  },
  # State 38
  {
    "vtype": "r36",
    "class": "r36",
    "$": "r36"
  },
  # State 39
  {
    "rbrace": "r37"
  },
  # State 40
  {
    "rbrace": "r38"
  },
  # State 41
  {
    "vtype": "s53",
    "id": "s54",
    "rbrace": "r25",
    "if": "s51",
    "while": "s52",
    "return": "r25",
    "VDECL": "49",
    "ASSIGN": "50",
    "BLOCK": "47",
    "STMT": "48"
  },
  # State 42
  {
    "rparen": "r20"
  },
  # State 43
  {
    "vtype": "s55"
  },
  # State 44
  {
    "semi": "r12",
    "rparen": "r12"
  },
  # State 45
  {
    "semi": "r14",
    "addsub": "r14",
    "rparen": "r14"
  },
  # State 46
  {
    "semi": "r16",
    "addsub": "r16",
    "multdiv": "r16",
    "rparen": "r16"
  },
  # State 47
  {
    "return": "s57",
    "RETURN": "56"
  },
  # State 48
  {
    "vtype": "s53",
    "id": "s54",
    "rbrace": "r25",
    "if": "s51",
    "while": "s52",
    "return": "r25",
    "VDECL": "49",
    "ASSIGN": "50",
    "BLOCK": "58",
    "STMT": "48"
  },
  # State 49
  {
    "vtype": "r26",
    "id": "r26",
    "rbrace": "r26",
    "if": "r26",
    "while": "r26",
    "return": "r26"
  },
  # State 50
  {
    "semi": "s59"
  },
  # State 51
  {
    "lparen": "s60"
  },
  # State 52
  {
    "lparen": "s61"
  },
  # State 53
  {
    "id": "s62",
    "ASSIGN": "11"
  },
  # State 54
  {
    "assign": "s15"
  },
  # State 55
  {
    "id": "s63"
  },
  # State 56
  {
    "rbrace": "s64"
  },
  # State 57
  {
    "id": "s28",
    "literal": "s22",
    "character": "s23",
    "boolstr": "s24",
    "lparen": "s27",
    "num": "s29",
    "RHS": "65",
    "EXPR": "21",
    "T": "25",
    "F": "26"
  },
  # State 58
  {
    "rbrace": "r24",
    "return": "r24"
  },
  # State 59
  {
    "vtype": "r27",
    "id": "r27",
    "rbrace": "r27",
    "if": "r27",
    "while": "r27",
    "return": "r27"
  },
  # State 60
  {
    "boolstr": "s68",
    "COND": "66",
    "B": "67"
  },
  # State 61
  {
    "boolstr": "s68",
    "COND": "69",
    "B": "67"
  },
  # State 62
  {
    "semi": "s13",
    "assign": "s15"
  },
  # State 63
  {
    "rparen": "r23",
    "comma": "s43",
    "MOREARGS": "70"
  },
  # State 64
  {
    "vtype": "r19",
    "rbrace": "r19",
    "class": "r19",
    "$": "r19"
  },
  # State 65
  {
    "semi": "s71"
  },
  # State 66
  {
    "rparen": "s72"
  },
  # State 67
  {
    "rparen": "r31",
    "comp": "s73"
  },
  # State 68
  {
    "rparen": "r32",
    "comp": "r32"
  },
  # State 69
  {
    "rparen": "s74"
  },
  # State 70
  {
    "rparen": "r22"
  },
  # State 71
  {
    "rbrace": "r35"
  },
  # State 72
  {
    "lbrace": "s75"
  },
  # State 73
  {
    "boolstr": "s68",
    "COND": "76",
    "B": "67"
  },
  # State 74
  {
    "lbrace": "s77"
  },
  # State 75
  {
    "vtype": "s53",
    "id": "s54",
    "rbrace": "r25",
    "if": "s51",
    "while": "s52",
    "return": "r25",
    "VDECL": "49",
    "ASSIGN": "50",
    "BLOCK": "78",
    "STMT": "48"
  },
  # State 76
  {
    "rparen": "r30"
  },
  # State 77
  {
    "vtype": "s53",
    "id": "s54",
    "rbrace": "r25",
    "if": "s51",
    "while": "s52",
    "return": "r25",
    "VDECL": "49",
    "ASSIGN": "50",
    "BLOCK": "79",
    "STMT": "48"
  },
  # State 78
  {
    "rbrace": "s80"
  },
  # State 79
  {
    "rbrace": "s81"
  },
  # State 80
  {
    "vtype": "r34",
    "id": "r34",
    "rbrace": "r34",
    "if": "r34",
    "while": "r34",
    "else": "s83",
    "return": "r34",
    "ELSE": "82"
  },
  # State 81
  {
    "vtype": "r29",
    "id": "r29",
    "rbrace": "r29",
    "if": "r29",
    "while": "r29",
    "return": "r29"
  },
  # State 82
  {
    "vtype": "r28",
    "id": "r28",
    "rbrace": "r28",
    "if": "r28",
    "while": "r28",
    "return": "r28"
  },
  # State 83
  {
    "lbrace": "s84"
  },
  # State 84
  {
    "vtype": "s54",
    "id": "s54",
    "rbrace": "r25",
    "if": "s51",
    "while": "s52",
    "return": "r25",
    "VDECL": "49",
    "ASSIGN": "50",
    "BLOCK": "85",
    "STMT": "48"
  },
  # State 85
  {
    "rbrace": "s86"
  },
  # State 86
  {
    "vtype": "r33",
    "id": "r33",
    "rbrace": "r33",
    "if": "r33",
    "while": "r33",
    "return": "r33"
  }
]