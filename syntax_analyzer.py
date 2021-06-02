from token_parser import token_parser
import sys

if len(sys.argv) != 2:  # Lexical analyzer를 command 창에서 실행할 때, input file을 같이 명시해야 함
    print("Type input file name as an argument")
    sys.exit()

input_file_path = sys.argv[1]
TOKEN_LIST = token_parser(input_file_path)


def main():
  pass

if __name__ == "__main__":
    main()
