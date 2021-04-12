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

    def cond_arithmetic_signedint(self, success_DFA):
        return self.get_name() != "ARITHMETIC_OPERATORS" or (self.get_name() == "ARITHMETIC_OPERATORS" and "SIGNED_INTEGER" not in success_DFA)

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

def is_identifier(curr_state, next_input):
    try:
        dfa_table["IDENTIFIER"][curr_state][next_input]
        return True
    except KeyError:
        for key in dfa_table["IDENTIFIER"][curr_state].keys():
                if key == "FINAL":
                    break
                if next_input in key:
                    if dfa_table["IDENTIFIER"][curr_state][key] == "T1":
                        return True
        return False

def is_comparison(curr_state, next_input):
    try:
        dfa_table["COMPARISON_OPERATORS"][curr_state][next_input]
        return True
    except KeyError:
        return False

# test_dfa = DFA("SIGNED_INTEGER")
# result = test_dfa.run("-")
# print("-: ", result)
# print(test_dfa.current_state)
# print(test_dfa.is_final_state(), test_dfa.input_record)
# result = test_dfa.run("1")
# print("1: ", result)
# result = test_dfa.run("+")
# print("+: ", result)
# result = test_dfa.run("a")
# print("a: ", result)
# result = test_dfa.run("t")
# print("t: ", result)
# result = test_dfa.run("i")
# print("i: ", result)
# result = test_dfa.run("c")
# print("c: ", result)
# print(test_dfa.current_state)
# print(test_dfa.is_final_state(), test_dfa.input_record)