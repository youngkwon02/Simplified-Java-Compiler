from dfa_table import LETTER, WHITESPACE
from dfa import DFA, is_comparison
import sys
import string
DIGIT = string.digits
DIGIT_1TO9 = string.digits[1:9]

if len(sys.argv) != 2:
    print("Type input file name as an argument")
    sys.exit()

input_file_path = sys.argv[1]

def read_input_file():
    file = open(input_file_path, mode='r', encoding='utf-8')
    return file

def init_success_dfa():
    return ["KEYWORD", "BOOLEAN_STRING", "ASSIGNMENT_OPERATOR", "COMPARISON_OPERATOR", "ARITHMETIC_OPERATOR", "SIGNED_INTEGER", "TERMINATING_SYMBOL", "LEFT_PAREN", "RIGHT_PAREN",
    "LEFT_BRACE", "RIGHT_BRACE", "LEFT_BRANKET", "RIGHT_BRANKET", "COMMA", "WHITESPACE", "VTYPE", "IDENTIFIER", "SINGLE_CHARACTER", "LITERAL_STRING"]


def init_each_dfa(DFA_list):
    for dfa in DFA_list:
        dfa.initialize()

def check_before_input(index, content):
    while(index > 0):
        if(content[index] not in string.whitespace):
            return content[index]
        index -= 1

    return("")

def is_before_lparen(index, content):
    while(index > 0):
        if(content[index] == "("):
            return True
        elif(content[index] == ")"):
            return False
        index -= 1
    return False

def get_line_number(index, content):
    check_index = 0
    line = 1
    while(check_index < index):
        if content[check_index] == "\n":
            line += 1
        check_index += 1
    return line

def main():
    DFA_vtype = DFA("VTYPE")
    DFA_identifier = DFA("IDENTIFIER")
    DFA_signedInteger = DFA("SIGNED_INTEGER")
    DFA_singleCharacter = DFA("SINGLE_CHARACTER")
    DFA_BOOLEAN_STRING = DFA("BOOLEAN_STRING")
    DFA_literalString = DFA("LITERAL_STRING")
    DFA_keyword = DFA("KEYWORD")
    DFA_arithmeticOperators = DFA("ARITHMETIC_OPERATOR")
    DFA_assignmentOperators = DFA("ASSIGNMENT_OPERATOR")
    DFA_comparisonOperators = DFA("COMPARISON_OPERATOR")
    DFA_terminatingSymbol = DFA("TERMINATING_SYMBOL")
    DFA_leftParen = DFA("LEFT_PAREN")
    DFA_rightParen = DFA("RIGHT_PAREN")
    DFA_leftBrace = DFA("LEFT_BRACE")
    DFA_rightBrace = DFA("RIGHT_BRACE")
    DFA_leftBranket = DFA("LEFT_BRANKET")
    DFA_rightBranket = DFA("RIGHT_BRANKET")
    DFA_comma = DFA("COMMA")
    DFA_whitespace = DFA("WHITESPACE")
    DFA_list = [DFA_keyword, DFA_BOOLEAN_STRING, DFA_assignmentOperators, DFA_comparisonOperators, DFA_arithmeticOperators, DFA_signedInteger,
    DFA_terminatingSymbol, DFA_leftParen, DFA_rightParen, DFA_leftBrace, DFA_rightBrace, DFA_leftBranket, DFA_rightBranket, DFA_comma, DFA_whitespace,
    DFA_vtype, DFA_identifier, DFA_singleCharacter, DFA_literalString
    ] # 모든 DFA List, Ordered by priority
    success_DFA = ["KEYWORD", "BOOLEAN_STRING", "ASSIGNMENT_OPERATOR", "COMPARISON_OPERATOR", "ARITHMETIC_OPERATOR", "SIGNED_INTEGER", "TERMINATING_SYMBOL", "LEFT_PAREN", "RIGHT_PAREN",
    "LEFT_BRACE", "RIGHT_BRACE", "LEFT_BRANKET", "RIGHT_BRANKET", "COMMA", "WHITESPACE", "VTYPE", "IDENTIFIER", "SINGLE_CHARACTER", "LITERAL_STRING"]

    f = read_input_file()
    file_content = f.read()
    output_file_name = input_file_path + "_output.txt"
    f_output = open(output_file_name, 'w')
    index = 0
    while(True):
        input_char = file_content[index]
        for dfa in DFA_list:
            if dfa.get_name() in success_DFA: # 현재까지 입력을 처리 가능했던 DFA를 순차적으로 돌면서
                result = dfa.run(input_char) # input_char를 처리 가능한지 확인

                if dfa.get_name() == "VTYPE" and result[0] == "end" and (input_char in LETTER or input_char in "_" or input_char in DIGIT): 
                    # VTYPE DFA에서 input을 더 이상 처리할 수 없고 최종 상태가 Final state일 때, 처리 불가능한 input이 Identifier에서 허용하는 input이라면 이는 Variable Type이 아니다
                    # (e.g. inte: VTYPE_DFA에서 처리 불가능한 e라는 문자를 입력받으면, int를 Variable Type으로 표현할텐데, Identifier DFA에서 처리 가능한 e라는 문자로 인해 처리할 수 없는 경우가 되었기에 이는 VTYPE이 아니다)
                    result = ("fail", "mess")
                
                if dfa.get_name() == "ARITHMETIC_OPERATOR" and dfa.get_record() == "-" and result[0] == "end" and input_char in DIGIT_1TO9:
                    # 위와 마찬가지로 ARITH_OPER DFA에서 처음에 -를 입력 받고 처리할 수 없는 input을 입력 받았을 때, state가 Final이지만, 이는 ARITH_OPER가 아니라 SIGNED_INTEGER 이다
                    # (e.g. -1: -를 읽은 후 1을 읽었을 때, Arithmetic oper DFA에서 처리할 수 없고, 누적 입력이 -이므로 Arithmetic 조건을 만족하지만, 이후 입력이 숫자이므로 SIGNED_INTEGER에 포함된다)
                    result = ("fail", "mess")

                if dfa.get_name() == "KEYWORD" and result[0] == "end" and (input_char in LETTER or input_char in "_" or input_char in DIGIT):
                    result = ("fail", "mess")

                if result[0] == "fail": # 해당 DFA가 주어진 값을 처리할 수 없고, State가 Final state도 아니라면,
                    success_DFA.remove(dfa.get_name()) # 현재까지 입력을 처리 가능했던 DFA list인 Success_DFA에서 삭제
                    if len(success_DFA) == 0: # 만약 삭제한 이후, 현재까지의 입력을 처리 가능한 DFA가 남아있지 않다면
                        text = "ERROR_DETECTED: line " + str(get_line_number(index, file_content)) + ", in " + input_file_path + "\n" # ERROR로 판단 및 메시지 출력
                        f_output.write(text)
                        sys.exit()

                elif result[0] == "end": # 해당 DFA가 주어진 값을 처리할 수 없는데, 이미 Final state에 도달해 있다면,
                        for success in success_DFA: # 지금까지의 입력을 처리 가능했던 DFA의 항목들
                            if success == "KEYWORD":
                                text = "<KEYWORD> " + result[1] + "\n"
                                f_output.write(text)
                                index -= 1
                                break
                            elif success == "ASSIGNMENT_OPERATOR":
                                if not is_comparison(DFA_comparisonOperators.current_state, file_content[index]):
                                    text = "<ASSIGNMENT_OPERATOR> " + result[1] + "\n"
                                    f_output.write(text)
                                    index -= 1
                                    break
                                else:
                                    text = "<COMPARISON_OPERATOR> " + "==" + "\n"
                                    f_output.write(text)
                                    break

                            elif success == "COMMA":
                                if is_before_lparen(index-2, file_content):
                                    text = "<ARGS_SEPERATING_COMMA> ,\n"
                                    f_output.write(text)
                                else:
                                    text = "<COMMA> ,\n"
                                    f_output.write(text)
                                break
                            else:
                                if success != "WHITESPACE":
                                    if result[1][0] == "-" and not (index-1 - len(result[1])) < 0 and check_before_input(index-1 - len(result[1]), file_content) in DIGIT:
                                        # Start with - symbol, so we check it's used for ARITHMETIC_OPER or SIGNED_INT
                                        text = "<ARITHMETIC_OPERATOR> -\n"
                                        index -= (len(result[1]) - 1)
                                        f_output.write(text)
                                    else: # Normal case such as a VTYPE or IDENTIFIER, ...
                                        text = "<" + success + "> " + result[1] +"\n"
                                        f_output.write(text)
                                index -= 1
                                break
                        init_each_dfa(DFA_list)
                        success_DFA = init_success_dfa()
                        break

                else: # Status가 Going일때, 즉 다음 input을 더 받아야 판단이 가능한데
                    if index == len(file_content) - 1: # 다음 input이 없을 경우(EOF)의 token name과 value 출력
                        if result[0] == "going":
                            for success in success_DFA:
                                if success != "WHITESPACE":
                                    # 아래 line에서 Index는 마지막 글자라서 보통 case보다 이미 1이 작음, index에서 1을 따로 빼지 않고 check_before_input
                                    if dfa.get_record()[0] == "-" and check_before_input(index - len(dfa.get_record()), file_content) in DIGIT:
                                        text = "<ARITHMETIC_OPERATOR> " + "-" + "\n"
                                        index -= (len(dfa.get_record()) - 1)
                                        f_output.write(text)
                                    else:
                                        text = "<" + success + "> " + dfa.get_record() + "\n"
                                        f_output.write(text)
                                init_each_dfa(DFA_list)
                                success_DFA = init_success_dfa()
                                break


        if index == len(file_content) - 1: # 파일의 모든 내용을 읽었다면 동작을 마침
            break

        index += 1
    
if __name__ == "__main__":
    main()