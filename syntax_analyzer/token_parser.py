from token_convert_table import TOKEN_CONVERT_TABLE

def read_input_file(file_path):
    file = open(file_path, mode='r', encoding='utf-8')
    return file
  

def write_output_file(file_name, token_list):
  f_output = open(file_name, 'w')
  for token in token_list:
    f_output.write(token+"\n")
  f_output.close()
  
  
def token_parser(file_path):
  f = read_input_file(file_path)
  parsed_token = []
  while(True):
    line = f.readline()
    if not line:
      break
    split_list = line.split(' ')
    split_list[-1] = split_list[-1].strip()
    raw_token = split_list[0]
    token_value = split_list[1]
    if raw_token in TOKEN_CONVERT_TABLE:
      if raw_token == "KEYWORD": # if, else, while, return 등의 keyword는 syntax analyzer에서 각각의 명칭을 token으로 사용
        parsed_token.append(token_value)
      elif raw_token == "ARITHMETIC_OPERATOR":
        parsed_token.append(TOKEN_CONVERT_TABLE.get(raw_token).get(token_value))
      else:
        parsed_token.append(TOKEN_CONVERT_TABLE.get(raw_token))
  f.close()
  parsed_token.append("$")
  output_file = file_path + "_syntax_input.txt"
  write_output_file(output_file, parsed_token)
  return parsed_token 