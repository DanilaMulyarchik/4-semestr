from gluing import *
from prettytable import PrettyTable


def ctm_sdnf(formula: str):
    table, data_table = create_table_ctm(gluing_sdnf(formula.split('+')), formula.split('+'), 'sdnf')
    rez_list = processing_table_data(data_table, gluing_sdnf(formula.split('+')))
    for i in range(len(rez_list)):
        rez_list[i] = '(' + rez_list[i] + ')'
    rez = '+'.join(rez_list)
    return rez, table


def ctm_sknf(formula: str):
    table, data_table = create_table_ctm(gluing_sknf(formula.split('*')), formula.split('*'), 'sknf')
    rez_list = processing_table_data(data_table, gluing_sknf(formula.split('*')))
    for i in range(len(rez_list)):
        rez_list[i] = '(' + rez_list[i] + ')'
    rez = '*'.join(rez_list)
    return rez, table


def create_table_ctm(implicants: list, konstituant: list, tipe_formula: str):
    table_data = list()
    table = PrettyTable()
    table.field_names = [
       'impl/kon', *konstituant]
    value_for_arguments = []
    if tipe_formula == 'sdnf':
        for i in range(len(implicants)):
            value_for_arguments.append(put_label_sdnf(konstituant, implicants[i]))
    else:
        for i in range(len(implicants)):
            value_for_arguments.append(put_label_sknf(konstituant, implicants[i]))

    for i in range(len(value_for_arguments)):
        table.add_row([
            implicants[i],
            *value_for_arguments[i]
        ])
        data_for_row = {konstituant[x]: value_for_arguments[i][x]
                        for x in range(len(konstituant))}
        data_for_row = {**data_for_row,
                        'impl': implicants[i]
                        }
        table_data.append(data_for_row)

    return table, table_data


def put_label_sdnf(konstituant: list, part: str):
    rez = list()
    if part[0] == '(' and part[-1] == ')':
        part = part[1:-1]
    for i in range(len(konstituant)):
        count = 0
        for j in range(len(part.split('*'))):
            if not part.split('*')[j] in konstituant[i][1:-1].split('*'):
                rez.append('')
                break
            else:
                count += 1
        if count == len(part.split('*')):
            rez.append('X')

    return rez


def put_label_sknf(konstituant: list, part: str):
    rez = list()
    if part[0] == '(' and part[-1] == ')':
        part = part[1:-1]
    for i in range(len(konstituant)):
        count = 0
        for j in range(len(part.split('+'))):
            if not part.split('+')[j] in konstituant[i][1:-1].split('+'):
                rez.append('')
                break
            else:
                count += 1
        if count == len(part.split('+')):
            rez.append('X')

    return rez


def processing_table_data(data_table, parts):
    rez = list()
    temp = list()
    for i in range(len(parts)):
        for j in data_table[0]:
            if j == 'impl':
                continue
            temp.clear()
            for k in range(len(data_table)):
                if data_table[k]['impl'] == parts[i]:
                    continue
                temp.append(data_table[k][j])
            if not 'X' in temp:
               rez.append(parts[i])
               break
    return rez

