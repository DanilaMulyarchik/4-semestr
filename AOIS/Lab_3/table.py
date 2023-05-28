from prettytable import PrettyTable
from itertools import product
from typing import *
from handler_input_formula import *


def replace_argument_on_number(set_of_values, arguments, temp_logic_formula):
    counter = 0
    for i in arguments:
        temp_logic_formula = temp_logic_formula.replace(i, str(set_of_values[counter]))
        counter += 1
    return temp_logic_formula


def create_logic_table(formula):
    arguments = take_arguments(formula)
    logic_formula = handler_input_formula(formula)
    table_data = list()
    table = PrettyTable()
    table.field_names = [
        *arguments, 'f(sknf)', 'f(sdnf)', 'i']
    value_for_arguments: List[Tuple(int)] = product(range(2), repeat=len(arguments))
    start_index = 2 ** (2 ** (len(arguments)) - 1)

    for i in value_for_arguments:
        temp_logic_formula = logic_formula
        temp_logic_formula = replace_argument_on_number(i, arguments, temp_logic_formula)
        table.add_row([
                            *i,
                            int(eval(temp_logic_formula)),
                            int(eval(temp_logic_formula)),
                            start_index,
                            ])
        data_for_row = {arguments[x]: i[x]
                        for x in range(len(arguments))}
        data_for_row = {**data_for_row,
                        'f': int(eval(temp_logic_formula)),
                        'i': start_index,
                        }
        table_data.append(data_for_row)
        start_index //= 2
    return table, table_data

