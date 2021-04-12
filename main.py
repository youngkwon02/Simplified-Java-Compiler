from dfa import DFA, is_comparison, is_identifier

def read_input_file():
    file = open("./test_code/test2.java", mode='r', encoding='utf-8')
    return file

def init_success_dfa():
    return ["KEYWORD", "BOOLEAN", "ASSIGNMENT_OPERATORS", "COMPARISON_OPERATORS", "SIGNED_INTEGER", "ARITHMETIC_OPERATORS", "TERMINATING_SYMBOL", "LEFT_PAREN", "RIGHT_PAREN",
    "LEFT_BRACE", "RIGHT_BRACE", "LEFT_BRANKET", "RIGHT_BRANKET", "COMMA", "WHITESPACE", "VTYPE", "IDENTIFIER", "SINGLE_CHARACTER", "LITERAL_STRING"]


def init_each_dfa(DFA_list):
    for dfa in DFA_list:
        dfa.initialize()

def main():
    DFA_vtype = DFA("VTYPE")
    DFA_identifier = DFA("IDENTIFIER")
    DFA_signedInteger = DFA("SIGNED_INTEGER")
    DFA_singleCharacter = DFA("SINGLE_CHARACTER")
    DFA_boolean = DFA("BOOLEAN")
    DFA_literalString = DFA("LITERAL_STRING")
    DFA_keyword = DFA("KEYWORD")
    DFA_arithmeticOperators = DFA("ARITHMETIC_OPERATORS")
    DFA_assignmentOperators = DFA("ASSIGNMENT_OPERATORS")
    DFA_comparisonOperators = DFA("COMPARISON_OPERATORS")
    DFA_terminatingSymbol = DFA("TERMINATING_SYMBOL")
    DFA_leftParen = DFA("LEFT_PAREN")
    DFA_rightParen = DFA("RIGHT_PAREN")
    DFA_leftBrace = DFA("LEFT_BRACE")
    DFA_rightBrace = DFA("RIGHT_BRACE")
    DFA_leftBranket = DFA("LEFT_BRANKET")
    DFA_rightBranket = DFA("RIGHT_BRANKET")
    DFA_comma = DFA("COMMA")
    DFA_whitespace = DFA("WHITESPACE")
    DFA_list = [DFA_keyword, DFA_boolean, DFA_assignmentOperators, DFA_comparisonOperators, DFA_signedInteger, DFA_arithmeticOperators, 
    DFA_terminatingSymbol, DFA_leftParen, DFA_rightParen, DFA_leftBrace, DFA_rightBrace, DFA_leftBranket, DFA_rightBranket, DFA_comma, DFA_whitespace,
    DFA_vtype, DFA_identifier, DFA_singleCharacter, DFA_literalString
    ] # 모든 DFA List, Ordered by priority
    success_DFA = ["KEYWORD", "BOOLEAN", "ASSIGNMENT_OPERATORS", "COMPARISON_OPERATORS", "SIGNED_INTEGER", "ARITHMETIC_OPERATORS", "TERMINATING_SYMBOL", "LEFT_PAREN", "RIGHT_PAREN",
    "LEFT_BRACE", "RIGHT_BRACE", "LEFT_BRANKET", "RIGHT_BRANKET", "COMMA", "WHITESPACE", "VTYPE", "IDENTIFIER", "SINGLE_CHARACTER", "LITERAL_STRING"]

    f = read_input_file()
    file_content = f.read()
    f_output = open("./output.txt", 'w')
    index = 0
    keyword_flag = False
    while(True):
        input_char = file_content[index]
        # print(index, "/", input_char)
        for dfa in DFA_list:
            if dfa.get_name() in success_DFA:
                result = dfa.run(input_char)
                if result[0] == "fail":
                    success_DFA.remove(dfa.get_name())
                elif result[0] == "end":
                    if dfa.cond_arithmetic_signedint(success_DFA):
                        for success in success_DFA:
                            if success == "KEYWORD":
                                if not is_identifier(DFA_identifier.current_state, file_content[index]):
                                    text = "<KEYWORD> " + result[1] + "\n"
                                    f_output.write(text)
                                    index -= 1
                                    keyword_flag = True
                                    break
                                else:
                                    success_DFA.remove("KEYWORD")
                                    continue
                            elif success == "ASSIGNMENT_OPERATORS":
                                if not is_comparison(DFA_comparisonOperators.current_state, file_content[index]):
                                    text = "<ASSIGNMENT_OPERATORS> " + result[1] + "\n"
                                    f_output.write(text)
                                    index -= 1
                                    break
                                else:
                                    text = "<COMPARISON_OPERATORS> " + "==" + "\n"
                                    f_output.write(text)
                                    break
                            else:
                                if success != "WHITESPACE":
                                    text = "<" + success + "> " + result[1] + "\n"
                                    f_output.write(text)
                                index -= 1
                                break
                        if (dfa.get_name() != "KEYWORD" or keyword_flag == True):
                            init_each_dfa(DFA_list)
                            success_DFA = init_success_dfa()
                            keyword_flag = False
                            break
                else:
                    if index == len(file_content) - 1:
                        if result[0] == "going":
                            for success in success_DFA:
                                if success != "WHITESPACE":
                                    text = "<" + success + "> " + dfa.get_record() + "\n"
                                    f_output.write(text)
                                init_each_dfa(DFA_list)
                                success_DFA = init_success_dfa()
                                break


        if index == len(file_content) - 1:
            break

        index += 1
    
if __name__ == "__main__":
    main()