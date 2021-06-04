from token_parser import token_parser
from production import PRODUCTION
from SLR_parsing_table import SLR_PARSING_TABLE
import sys

if len(sys.argv) != 2:  # Lexical analyzer를 command 창에서 실행할 때, input file을 같이 명시해야 함
    print("Type input file name as an argument")
    sys.exit()

input_file_path = sys.argv[1]
TOKEN_LIST = token_parser(input_file_path)

def goto(state, input):
  options = SLR_PARSING_TABLE[state]
  if input not in options:
    print("Not acceptable! (unacceptable token in goto: at state ", state, ",", input, ")")
    return -1
  action = options[input]
  if action[0] == "s" or action[0] == "r":
    print("Not Expected Error")
    return -1
  return int(action)
    
  
def main():
  state_stack = [0]
  left_side = []
  next_pointer = 0
  next_input = TOKEN_LIST[next_pointer]
  while(True):
    current_state = state_stack[-1]
    options = SLR_PARSING_TABLE[current_state]
    print(state_stack, next_input)
    if next_input not in options:
      print("Not acceptable! (unacceptable token: ", next_pointer," token", next_input, ")")
      print(state_stack, next_input)
      return -1
    action = options[next_input]
    if action[0] == "s": # SHIFT AND GOTO
      left_side.append(next_input)
      next_pointer += 1
      next_input = TOKEN_LIST[next_pointer]
      state_stack.append(int(action[1:]))
    elif action[0] == "r": # REDUCTION
      prod = PRODUCTION[int(action[1:])]
      alpha = list(prod.keys())[0]
      pop_num = len(alpha.split(' '))
      if alpha == "":
        pop_num = 0
      for pop in range(pop_num):
        left_side.pop()
        state_stack.pop()
      left_side.append(list(prod.values())[0])
      new_state = goto(state_stack[-1], left_side[-1])
      if new_state == -1:
        print(state_stack)
        return -1
      state_stack.append(new_state)
    elif action == "acc": # ACCEPT
      print("Accept")
      return 0
    else: # GOTO
      state_stack.append(int(action))

if __name__ == "__main__":
    main()
