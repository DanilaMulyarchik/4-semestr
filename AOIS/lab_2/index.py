from table import *


def index(formula):
    data_table = create_logic_table(formula)[1]
    index = 0
    for i in range(len(data_table)):
        if data_table[i]['f'] == 1:
            index += int(data_table[i]['i'])
    return index