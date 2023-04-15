from table import *
from bin_to_dec import *


def sknf(formula):
    formula_sknf = ''
    data_table = create_logic_table(formula)[1]
    for i in data_table:
        if i['f'] == 0:
            part = ' + '.join([values * '!' + keys for keys, values in i.items() if keys != 'f' and keys != 'i'])
            formula_sknf += '( ' + str(part) + ' )' + ' * '
    formula_sknf = formula_sknf[:-2]
    return formula_sknf


def sknf_number_form(formula):
    split_sknf = sknf(formula).split()
    sknf_bin = list()
    for i in range(0, len(split_sknf)):
        if split_sknf[i][0] == 'x':
            sknf_bin.append('0')
        elif split_sknf[i][0] == '!':
            sknf_bin.append('1')
        elif split_sknf[i][0] == ')':
            sknf_bin.append('*')
    sknf_bin = ''.join(sknf_bin[:-1])
    sknf_dec = bin_to_dec(sknf_bin, formula)
    sknf_dec = map(str, sknf_dec)
    sknf_dec = '*(' + ', '.join(sknf_dec) + ')'

    return sknf_bin, sknf_dec


