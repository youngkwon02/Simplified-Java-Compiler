from dfa_table import LETTER
from dfa import DFA
import sys
import string
DIGIT = string.digits
DIGIT_1TO9 = string.digits[1:9]

if len(sys.argv) != 2:  # Lexical analyzer를 command 창에서 실행할 때, input file을 같이 명시해야 함
    print("Type input file name as an argument")
    sys.exit()

input_file_path = sys.argv[1]


def read_input_file():
    file = open(input_file_path, mode='r', encoding='utf-8')
    return file


def init_success_dfa():  # 해당 함수는 main function에서, 특정 input에 대한 token이 결정된 후, success_DFA라는 변수를 초기화 하는 역할
    return ["KEYWORD", "BOOLEAN_STRING", "ASSIGNMENT_OPERATOR", "COMPARISON_OPERATOR", "ARITHMETIC_OPERATOR", "SIGNED_INTEGER", "TERMINATING_SYMBOL", "LEFT_PAREN", "RIGHT_PAREN",
            "LEFT_BRACE", "RIGHT_BRACE", "LEFT_BRACKET", "RIGHT_BRACKET", "COMMA", "WHITESPACE", "VTYPE", "IDENTIFIER", "SINGLE_CHARACTER", "LITERAL_STRING"]


# 각각의 DFA를 모두 initializing, DFA의 current state와 input record를 초기화한다
def init_each_dfa(DFA_list):
    for dfa in DFA_list:
        dfa.initialize()


# Whitespace가 아닌 이전 input 글자를 return한다.
def check_before_input(index, content):
    # 이 함수는 - 가 입력되었을 때, 이를 SIGNED_INTEGER로 해석할 것인지, ARITHMETIC_OPER로 해석할 것인지 판단에 도움을 준다.
    while(index > 0):
        if(content[index] not in [" ", "\t"]):
            return content[index]
        index -= 1

    return("")


# Comma(,)가 입력되었을 때, function의 Args를 구분하는 comma인지 확인하기 위해, 이전의 input에 LEFT_PAREN이 있는지 확인한다
def is_before_lparen(index, content):
    while(index > 0):
        if(content[index] == "("):
            return True
        elif(content[index] == ")"):
            return False
        index -= 1
    return False


# 처리할 수 없는 input이 입력되었을 때, Error message를 출력할텐데, Error가 발생한 Line number를 return하는 함수
def get_line_number(index, content):
    check_index = 0
    line = 1
    while(check_index < index):
        if content[check_index] == "\n":
            line += 1
        check_index += 1
    return line


def main():
    # Defined Token을 처리하기 위한 각각의 DFA를 생성한다
    # 생성자의 Parameter는 DFA의 name
    DFA_vtype = DFA("VTYPE")
    DFA_identifier = DFA("IDENTIFIER")
    DFA_signedInteger = DFA("SIGNED_INTEGER")
    DFA_singleCharacter = DFA("SINGLE_CHARACTER")
    DFA_booleanString = DFA("BOOLEAN_STRING")
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
    DFA_leftBracket = DFA("LEFT_BRACKET")
    DFA_rightBracket = DFA("RIGHT_BRACKET")
    DFA_comma = DFA("COMMA")
    DFA_whitespace = DFA("WHITESPACE")
    DFA_list = [DFA_keyword, DFA_booleanString, DFA_assignmentOperators, DFA_comparisonOperators, DFA_arithmeticOperators, DFA_signedInteger,
                DFA_terminatingSymbol, DFA_leftParen, DFA_rightParen, DFA_leftBrace, DFA_rightBrace, DFA_leftBracket, DFA_rightBracket, DFA_comma, DFA_whitespace,
                DFA_vtype, DFA_identifier, DFA_singleCharacter, DFA_literalString]  # 모든 DFA List, Ordered by priority
    # success_DFA는 리스트 형태로써, 후에 input을 입력받은 후 각각의 DFA에 해당 input을 넘겨서 처리할 때, 처리할 수 없는 DFA를 remove하며, 최종적으로 선택될 수 있는 DFA만 보관한다
    success_DFA = init_success_dfa()
    f = read_input_file()
    file_content = f.read()
    output_file_name = input_file_path + "_output.txt"
    f_output = open(output_file_name, 'w')
    index = 0
    while(True):
        # Input_file의 전체 내용에 index를 통해 access하여 한 글자씩 반복해서 읽는다
        input_char = file_content[index]
        for dfa in DFA_list:  # Priority 순으로 DFA를 가져와서
            if dfa.get_name() in success_DFA:  # 해당 DFA가 최근 init 이후부터 현재까지 입력을 처리 가능했던 DFA라면
                result = dfa.run(input_char)  # 새로운 input_char를 처리 가능한지 확인,
                # result[0]은 fail, going, end 중 하나이며, 처리할 수 없는데 final state가 아니라면 fail, 처리할 수 없지만 final state라면 end, 처리할 수 있다면 going
                # result[1]은 fail일 때는 더미 값을 return하며, going과 end일 때는, 지금까지 처리해온 input들을 return

                if dfa.get_name() == "VTYPE" and result[0] == "end" and (input_char in LETTER or input_char in "_" or input_char in DIGIT):
                    # VTYPE DFA에서 input을 더 이상 처리할 수 없고 최종 상태가 Final state일 때, 처리 불가능한 input이 Identifier에서 허용하는 input이라면 이는 Variable Type이 아니다
                    # (e.g. inte라는 코드 내용 중, VTYPE_DFA에서 처리 불가능한 e라는 문자를 입력받으면, int를 Variable Type으로 표현할텐데,
                    # Identifier DFA에서 처리 가능한 e라는 문자로 인해 처리할 수 없는 경우가 되었기에 이는 VTYPE이 아니다)
                    # VTYPE이 아닌, VTYPE value를 첫 부분에 포함하는 IDENTIFIER이므로, VTYPE의 result를 fail로 변경
                    result = ("fail", "mess")

                if dfa.get_name() == "ARITHMETIC_OPERATOR" and dfa.get_record() == "-" and result[0] == "end" and input_char in DIGIT_1TO9:
                    # 위와 마찬가지로 ARITH_OPER DFA에서 처음에 -를 입력 받고 처리할 수 없는 input을 입력 받았을 때, state가 Final이지만, 이는 ARITH_OPER가 아니라 SIGNED_INTEGER 이다
                    # (e.g. -1: -를 읽은 후 1을 읽었을 때, Arithmetic oper DFA에서 처리할 수 없고, 누적 입력이 -이므로 Arithmetic 조건을 만족하지만, 이후 입력이 숫자이므로 SIGNED_INTEGER에 포함된다)
                    result = ("fail", "mess")

                if dfa.get_name() == "KEYWORD" and result[0] == "end" and (input_char in LETTER or input_char in "_" or input_char in DIGIT):
                    # 위와 마찬가지로, KEYWORD를 변수 이름의 첫 부분에 포함하는 IDENTIFIER를 방지
                    result = ("fail", "mess")

                if result[0] == "fail":  # 해당 DFA가 주어진 값을 처리할 수 없고, State가 Final state도 아니라면,
                    # 해당 DFA를 현재까지 입력을 처리 가능했던 DFA list인 Success_DFA에서 삭제
                    success_DFA.remove(dfa.get_name())
                    if len(success_DFA) == 0:  # 만약 삭제한 이후, 현재까지의 입력을 처리 가능한 DFA가 남아있지 않다면
                        text = "ERROR_DETECTED: line " + \
                            str(get_line_number(index, file_content)) + ", in " + \
                            input_file_path + "\n"  # ERROR로 판단하여 프로그램 종료 및 message 출력
                        f_output.write(text)
                        sys.exit()

                elif result[0] == "end":  # 해당 DFA가 주어진 값을 처리할 수 없는데, 이미 Final state에 도달해 있다면,
                    for success in success_DFA:  # 지금까지의 입력을 처리 가능했던 DFA의 항목들 중
                        if success == "ASSIGNMENT_OPERATOR": # 해당 DFA가 ASSIGNMENT OPERATOR DFA인데
                            if input_char == "=": # 새로운 Input이 '='라면, 이는 Assignment Oper가 아닌 Comparison Oper
                                text = "<COMPARISON_OPERATOR> " + "==" + "\n"
                                f_output.write(text)
                                break
                                
                            else: # 새로운 Input이 '='가 아니라면, 이는 Assignment Oper
                                text = "<ASSIGNMENT_OPERATOR> " + \
                                    result[1] + "\n"
                                f_output.write(text)
                                index -= 1
                                break

                        elif success == "COMMA": # Comma DFA라면
                            if is_before_lparen(index-2, file_content): # 이전에 LEFT_PAREN이 나왔는지 확인하여, 나왔다면
                                text = "<ARGS_SEPERATING_COMMA> ,\n" # 함수의 인자를 구분하는 Comma로 판단
                                f_output.write(text)
                                break
                            else: # LEFT_PAREN이 나오지 않았거나, LEFT_PAREN보다 RIGHT_PAREN이 뒤에 나왔다면, 이는 Seperating comma가 아니므로 처리할 수 없다고 판단
                                # 왜냐하면 Lexical Analyzer가 일반적인 Comma를 처리할 수 있다고 언급되지 않았음
                                text = "ERROR_DETECTED: line " + \
                                    str(get_line_number(index, file_content)) + ", in " + \
                                    input_file_path + "\n"  # ERROR로 판단하여 프로그램 종료 및 message 출력
                                f_output.write(text)
                                sys.exit()
                        else:
                            if success != "WHITESPACE": # Whitespace는 출력 생략
                                if (result[1][0] == "-" and not (index-1 - len(result[1])) < 0 and check_before_input(index-1 - len(result[1]), file_content) not in ["=", '+', '-', '*', '/', "", '\n', ',', '(', '{', '[']):
                                    # -로 시작할 경우, 이는 ARITHMETIC OPER인지, SIGNED_INTEGER인지 판단 필요
                                    # 만약 -로 시작할 경우, Whitespace를 제외한 바로 직전의 문자가 +, -, *, /, =, '\n', ',', '(', '{', '[' 가 아니라면 이는 ARITH OPER
                                    text = "<ARITHMETIC_OPERATOR> -\n"
                                    index -= (len(result[1]) - 1)
                                    f_output.write(text)
                                else:  # SIGNED_INTEGER를 포함한 일반적인 case such as an IDENTIFIER, ...
                                    text = "<" + success + \
                                        "> " + result[1] + "\n"
                                    f_output.write(text)
                            index -= 1
                            break
                    init_each_dfa(DFA_list) # Token을 Decide한 후, 모든 DFA를 초기화 (current_state, input_record)
                    success_DFA = init_success_dfa() # success_DFA 역시 초기화
                    break

                else:  # Status가 Going일때, 즉 다음 input을 더 받아야 판단이 가능한데
                    if index == len(file_content) - 1: # 다음 input이 없을 경우(EOF)의 token name과 value 출력
                        for success in success_DFA:
                            if success != "WHITESPACE" and dfa.is_final_state() == "True":
                                # 아래 line에서 Index는 마지막 글자라서 보통 case보다 이미 1이 작음, index에서 1을 따로 빼지 않고 check_before_input
                                if success == "COMMA":
                                    if is_before_lparen(index-1, file_content):
                                        text = "<ARGS_SEPERATING_COMMA> ,\n"
                                        f_output.write(text)
                                        break
                                    else:
                                        text = "ERROR_DETECTED: line " + \
                                            str(get_line_number(index, file_content)) + ", in " + \
                                            input_file_path + "\n"  # ERROR로 판단 및 메시지 출력
                                        f_output.write(text)
                                        sys.exit()
                                else:
                                    text = "<" + success + \
                                        "> " + result[1] + "\n"
                                    f_output.write(text)
                            else:
                                text = "ERROR_DETECTED: line " + \
                                str(get_line_number(index, file_content)) + ", in " + \
                                input_file_path + "\n"  # ERROR로 판단 및 메시지 출력
                                f_output.write(text)
                                sys.exit()
                            init_each_dfa(DFA_list)
                            success_DFA = init_success_dfa()
                            break

        if index == len(file_content) - 1:  # 파일의 모든 내용을 읽었다면 동작을 마침
            break

        index += 1


if __name__ == "__main__":
    main()
