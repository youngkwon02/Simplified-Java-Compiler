from dfa_table import *


class DFA:
    token_name = ""  # DFA의 이름을 저장하는 필드
    current_state = ""  # DFA의 현재 State를 보관하는 필드
    input_record = ""  # DFA가 지금까지 읽어오며 처리한 input들을 기록하는 필드

    def __init__(self, token_name):
        self.token_name = token_name
        self.current_state = "T0"  # 모든 DFA의 초기 state는 T0

    def initialize(self):
        self.current_state = "T0"  # 모든 DFA의 초기 state는 T0
        self.input_record = ""

    def get_name(self):  # DFA의 이름을 반환하는 함수
        return self.token_name

    def is_final_state(self):  # DFA의 현재 상태가 Final state인지 확인하는 함수
        if dfa_table[self.token_name][self.current_state]["FINAL"]:
            return "True"
        else:
            return "False"

    def get_record(self): # DFA의 지금까지 처리한 input record를 반환하는 함수
        return self.input_record

    def run(self, input_char): # 새로운 input을 처리하느는 함수
        try:
            self.input_record += input_char
            self.current_state = dfa_table[self.token_name][self.current_state][input_char] # 처리를 시도하며
            return ("going", self.input_record) # Key error가 발생하지 않는다면 처리 가능한 input이였던 것

        except KeyError: # Key error가 발생하면 해당 DFA에서 처리할 수 없는 input을 받은 것
            for key in dfa_table[self.token_name][self.current_state].keys():
                if key == "FINAL": # Final은 처리하기 위한 값이 아니고, Final state인지를 명시하는 key 이므로 생략
                    break
                if input_char in key: # input이 특정 key에 포함된다면 (e.g. input k는 LETTER라는 key에 포함됨)
                    self.current_state = dfa_table[self.token_name][self.current_state][key] # DFA의 State update
                    return ("going", "mess") # Equal realtionship이 아니기 때문에 KeyError가 발생하였지만, 결국 처리 가능한 input이므로 going을 return
            if self.is_final_state() == "True": # 처리를 실패하였는데, 현재 머물러있는 state가 Final state라면
                self.input_record = self.input_record[0:len(
                    self.input_record) - 1]
                return ("end", self.input_record, "back") # 결국 처리 완료, end를 return
            else:
                return ("fail", "mess") # KeyError가 발생하였지만, 어느 경우에도 포함되지 않으면 fail return
                