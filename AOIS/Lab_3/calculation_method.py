from gluing import *


def calculation_method_sdnf(formula: str):
    new_sdnf = (gluing_sdnf(formula.split('+')))
    a = False
    for i in range(len(new_sdnf)):
        if new_sdnf[i].find('*') == -1:
            a = True
    if not a:
        new_sdnf = check_for_redundant_implications_sdnf(new_sdnf)
    for i in range(len(new_sdnf)):
        new_sdnf[i] = '(' + new_sdnf[i] + ')'
    new_formula = '+'.join(new_sdnf[i] for i in range(len(new_sdnf)))
    return new_formula


def calculation_method_sknf(formula: str):
    new_sknf = check_for_redundant_implications_sknf(gluing_sknf(formula.split('*')))
    a = False
    for i in range(len(new_sknf)):
        if new_sknf[i].find('+') == -1:
            a = True
    if not a:
        new_sknf = check_for_redundant_implications_sdnf(new_sknf)
    for i in range(len(new_sknf)):
        new_sknf[i] = '(' + new_sknf[i] + ')'
    new_formula = '*'.join(new_sknf[i] for i in range(len(new_sknf)))
    return new_formula


def check_for_redundant_implications_sknf(parts: list):
    rez = list()

    for i in range(len(parts)):
        kit = make_variant_of_number(parts[i])

        temp_part = convert(parts[i])

        nabor = find_true_variant_sknf(temp_part, kit)

        if not check_for_needing_sknf(parts, nabor, parts[i]):
            rez.append(parts[i])
        else:
            continue
    return rez


def check_for_redundant_implications_sdnf(parts: list):
    rez = list()

    for i in range(len(parts)):
        kit = make_variant_of_number(parts[i])

        temp_part = convert(parts[i])

        nabor = find_true_variant_sdnf(temp_part, kit)

        if not check_for_needing_sdnf(parts, nabor, parts[i]):
            rez.append(parts[i])
        else:
            continue
    return rez

def convert(part: str):
    temp_part = str()
    for j in range(len(part)):
        if part[j] == '!':
            temp_part += ' not '
        elif part[j] == '+':
            temp_part += ' or '
        elif part[j] == '*':
            temp_part += ' and '
        else:
            temp_part += part[j]

    return temp_part


def find_true_variant_sdnf(part: str, kit: list):
    for k in range(1, len(kit)):
        temp_part = part
        for i in range(len(kit[0])):
            temp_part = temp_part.replace(kit[0][i], kit[k][i])
        if int(eval(temp_part)) == 1:
            return [kit[0], kit[k]]


def find_true_variant_sknf(part: str, kit: list):
    for k in range(1, len(kit)):
        temp_part = part
        for i in range(len(kit[0])):
            temp_part = temp_part.replace(kit[0][i], kit[k][i])
        if int(eval(temp_part)) == 0:
            return [kit[0], kit[k]]


def change_value(temp_rez: str, take: bool):
    rez = str()
    for i in range(len(temp_rez)):
        if temp_rez[i] == '!' and temp_rez[i + 1] == '0':
            rez += '1'
            take = True
        elif temp_rez[i] == '!' and temp_rez[i + 1] == '1':
            rez += '0'
            take = True
        elif temp_rez[i] == '1' and not take and temp_rez[i-1] != 'x':
            rez += '1'
        elif temp_rez[i] == '0' and not take:
            rez += '0'
        elif not take:
            rez += temp_rez[i]
        else:
            take = False
    return rez


def check_for_needing_sdnf(parts: list, nabor: list, part: str):
    temp_rez = ''

    for i in range(len(parts)):
        if parts[i] == part:
            continue
        temp_part = parts[i]
        for k in range(len(nabor[0])):
            temp_part = temp_part.replace(nabor[0][k], nabor[1][k])
        temp_rez += temp_part + '+'

    rez = change_value(temp_rez, False)

    rez = rez.split('+')
    for i in range(len(rez)):
        if rez[i].find('0') != -1:
            rez[i] = ''

    for i in range(len(rez) - 1):
        for j in range(i + 1, len(rez)):

            if rez[i] == '' or rez[j] == '':
                continue

            p1 = set(rez[i].split('*'))
            p2 = set(rez[j].split('*'))

            different = list(set(p1.union(p2) - p1.intersection(p2)))

            for k in range(len(different) - 1):
                for t in range(k + 1, len(different)):
                    if str(different[k]) == str('!' + different[t]) or str('!' + different[k]) == str(
                            different[t]):
                        different.remove(different[t])
                        different.remove(different[k])
            if len(different) == 0:
                return True
    return False


def check_for_needing_sknf(parts: list, nabor: list, part: str):
    temp_rez = ''

    for i in range(len(parts)):
        if parts[i] == part:
            continue
        temp_part = parts[i]
        for k in range(len(nabor[0])):
            temp_part = temp_part.replace(nabor[0][k], nabor[1][k])
        temp_rez += temp_part + '*'

    rez = change_value(temp_rez, False)

    rez = rez.split('*')
    for i in range(len(rez)):
        if rez[i].find('1') != -1 and rez[i][rez[i].find('1') - 1] != 'x':
            rez[i] = ''

    for i in range(len(rez) - 1):
        for j in range(i + 1, len(rez)):

            if rez[i] == '' or rez[j] == '':
                continue

            p1 = set(rez[i].split('+'))
            p2 = set(rez[j].split('+'))

            different = list(set(p1.union(p2) - p1.intersection(p2)))

            for k in range(len(different) - 1):
                for t in range(k + 1, len(different)):
                    if str(different[k]) == str('!' + different[t]) or str('!' + different[k]) == str(
                            different[t]):
                        different.remove(different[t])
                        different.remove(different[k])
            if len(different) == 0:
                return True
    return False


def make_variant_of_number(part):
    count = int(0)
    kit = []
    arg_kit = []
    for i in range(len(part)):
        if part[i] == 'x':
            count += 1
            arg_kit.append(str(part[i] + part[i + 1]))
    kit.append(arg_kit)
    for i in range(2 ** count):
        binary = bin(i)[2:].zfill(count)
        kit.append([str(x) for x in binary])

    return kit


