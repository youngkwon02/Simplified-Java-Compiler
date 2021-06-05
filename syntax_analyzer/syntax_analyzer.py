from token_parser import token_parser
from production import PRODUCTION
from SLR_parsing_table import SLR_PARSING_TABLE
import sys


if len(sys.argv) != 2:  # Lexical analyzer를 command 창에서 실행할 때, input file을 같이 명시해야 함
    print("Type input file name as an argument")
    sys.exit()


input_file_path = sys.argv[1]
TOKEN_LIST = token_parser(input_file_path)


def goto(state, input): # Reduction 이후 GOTO를 위한 함수, 잘못되었을 경우 에러 메시지를 띄우고 -1을 return
  options = SLR_PARSING_TABLE[state]
  if input not in options: # 잘못된 경우
    print("Reject with an input: ", input)
    print("(The last state was ", state, ")")
    return -1
  action = options[input]
  if action[0] == "s" or action[0] == "r": # GOTO는 Shift나 Reduce 없이 Only state change
    print("Not Expected Error at the GOTO part") # 만약 GOTO에서 Shift나 Reduction을 요구한다면 Table error
    return -1
  return int(action)
    
  
def main():
  state_stack = [0] # State를 누적 보관하는 Stack
  left_side = []
  next_pointer = 0 # 처리할 Input의 index 값 보관
  next_input = TOKEN_LIST[next_pointer] # next_pointer의 값을 통해 처리할 Input token에 접근
  counter = 1 # Error message 구체화를 위한 counter
  while(True):
    current_state = state_stack[-1] # Current State는 State_stack의 top value
    options = SLR_PARSING_TABLE[current_state] # SLR Parsing Table에서 current state에서 선택할 수 있는 모든 option을 읽어옴 (e.g: vtype일 경우 s5)
    if next_input not in options: # 하지만 next_input이 처리할 수 없는 input일 경우
      print("Reject with an", counter, "th input: ", next_input) # 처리할 수 없는 Input과, 해당 Input이 몇 번째 Input인지 에러메시지로 출력 
      return -1
    action = options[next_input] # next_input이 current_state에서 처리 가능한 input이라면 action에 저장
    if action[0] == "s": # action이 s로 시작한다면, shift and goto
      left_side.append(next_input) # shift
      next_pointer += 1 # shift
      next_input = TOKEN_LIST[next_pointer] # shift
      counter += 1
      state_stack.append(int(action[1:])) # State Change
    elif action[0] == "r": # action이 r로 시작한다면, reduction
      prod = PRODUCTION[int(action[1:])] # 처리할 Production number를 prod에 저장
      alpha = list(prod.keys())[0] # Reduction할 Target terminal(or non-terminal)
      pop_num = len(alpha.split(' ')) # T->a라는 Production에서 |a|만큼 state를 pop하므로 pop할 횟수 저장
      if alpha == "": # |a| == 0인 예외적인 경우 처리
        pop_num = 0
      for pop in range(pop_num): # Pop 처리
        left_side.pop()
        state_stack.pop()
      left_side.append(list(prod.values())[0]) # Reduction result update
      new_state = goto(state_stack[-1], left_side[-1]) # Reduction 이후 GOTO 과정을 통해 correct한지 확인하는 과정
      if new_state == -1: # GOTO 결과가 정상이 아니라면
        print("Reject with an", counter, "th input: ", next_input) # 처리할 수 없는 Input과, 해당 Input이 몇 번째 Input인지 에러메시지로 출력 
        return -1
      state_stack.append(new_state) # new_state를 state_stack에 update
    elif action == "acc": # ACCEPT
      print("Accept")
      return 0
    else: # action이 s 혹은 r로 시작하지 않는다면 only state change
      state_stack.append(int(action)) # state_stack update


if __name__ == "__main__":
    main()
