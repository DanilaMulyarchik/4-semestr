from table import *
from bin_to_dec import *


def sdnf(formula):
    formula_sdnf = ''
    data_table = create_logic_table(formula)[1]
    for i in data_table:
        if i['f'] == 1:
            part = ' * '.join([abs(values - 1) * '!' + keys for keys, values in i.items() if keys != 'f' and keys != 'i'])
            formula_sdnf += '( ' + str(part) + ' )' + ' + '
    formula_sdnf = formula_sdnf[0:-2]
    return formula_sdnf


def sdnf_number_form(formula):
    split_sdnf = sdnf(formula).split()
    sdnf_bin = list()
    for i in range(0, len(split_sdnf)):
        if split_sdnf[i][0] == 'x':
            sdnf_bin.append('1')
        elif split_sdnf[i][0] == '!':
            sdnf_bin.append('0')
        elif split_sdnf[i][0] == ')':
            sdnf_bin.append('+')
    sdnf_bin = ''.join(sdnf_bin[:-1])
    sdnf_dec = bin_to_dec(sdnf_bin, formula)
    sdnf_dec = map(str, sdnf_dec)
    sdnf_dec = '+(' + ', '.join(sdnf_dec) + ')'
    return sdnf_bin, sdnf_dec
