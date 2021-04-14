from dfa_table import *

class DFA:
    token_name = ""
    current_state = ""
    input_record = ""

    def __init__(self, token_name):
        self.token_name = token_name
        self.current_state = "T0"

    def initialize(self):
        self.current_state = "T0"
        self.input_record = ""

    def get_name(self):
        return self.token_name

    def is_final_state(self):
        if dfa_table[self.token_name][self.current_state]["FINAL"]:
            return "True"
        else:
            return "False"

    def cond_vtype_identifier(self, success_DFA, index, file_content):
        return self.get_name() != "VTYPE" or (self.get_name() == "VTYPE" and file_content[index] == " ")

    def get_record(self):
        return self.input_record

    def run(self, input_char):
        try:
            self.input_record += input_char
            self.current_state = dfa_table[self.token_name][self.current_state][input_char]
            return ("going", "mess")

        except KeyError:
            for key in dfa_table[self.token_name][self.current_state].keys():
                if key == "FINAL":
                    break
                if input_char in key:
                    self.current_state = dfa_table[self.token_name][self.current_state][key]
                    return ("going", "mess")
            if self.is_final_state() == "True":
                self.input_record = self.input_record[0:len(self.input_record) - 1]
                return ("end", self.input_record, "back")
            else:
                return ("fail", "mess")

def is_comparison(curr_state, next_input):
    try:
        dfa_table["COMPARISON_OPERATOR"][curr_state][next_input]
        return True
    except KeyError:
        return False