from sknf import *
from sdnf import *


def gluing_sdnf(parts: list):
    rez = list()
    change = int(0)
    parts_whith_check = list()
    for i in range(len(parts)):
        parts_whith_check.append(create_2(parts[i]))

    for i in range(len(parts_whith_check) - 1):
        for j in range(i + 1, len(parts_whith_check)):
            p1 = set(create(parts_whith_check[i][0]).split('*'))
            p2 = set(create(parts_whith_check[j][0]).split('*'))

            if len(p1) != len(p2):
                continue

            common = p1.intersection(p2)

            if len(common) == len(p1) - 1 and check(p1, p2, common):
                parts_whith_check[i][1] = True
                parts_whith_check[j][1] = True
                change += 1
                new_part = gluing(p1, p2, common)
                rez.append('*'.join(new_part))
        if not parts_whith_check[i][1] and not parts[i] in rez:
            rez.append(parts_whith_check[i][0])
    if not parts_whith_check[-1][1] and not parts[-1] in rez:
        rez.append(parts_whith_check[-1][0])
    if change >= 2:
        rez = gluing_sdnf(rez)
    return rez


def gluing_sknf(parts: list):
    rez = list()
    change = int(0)
    parts_whith_check = list()
    for i in range(len(parts)):
        parts_whith_check.append(create_2(parts[i]))

    for i in range(len(parts_whith_check) - 1):
        for j in range(i + 1, len(parts_whith_check)):
            p1 = set(create(parts_whith_check[i][0]).split('+'))
            p2 = set(create(parts_whith_check[j][0]).split('+'))

            if len(p1) != len(p2):
                continue

            common = p1.intersection(p2)

            if len(common) == len(p1) - 1 and check(p1, p2, common):
                parts_whith_check[i][1] = True
                parts_whith_check[j][1] = True
                change += 1
                new_part = gluing(p1, p2, common)
                rez.append('+'.join(new_part))
        if not parts_whith_check[i][1] and not parts[i] in rez:
            rez.append(parts[i])
    if not parts_whith_check[-1][1] and not parts[-1] in rez:
        rez.append(parts_whith_check[-1][0])
    if change >= 2:
        rez = gluing_sknf(rez)
    return rez


def gluing(p1: set, p2: set, common: set):

    different = list(set(p1.union(p2)) - common)

    for k in range(len(different) - 1):
        for t in range(k + 1, len(different)):
            if str(different[k]) == str('!' + different[t]) or str('!' + different[k]) == str(
                    different[t]):
                different.remove(different[t])
                different.remove(different[k])

    new_part = list()
    common = list(common)

    for q in range(len(common)):
        new_part.append(common[q])
    for q in range(len(different)):
        new_part.append(different[q])

    return new_part


def check(p1: set, p2: set, common: set):

    different = list(p1.union(p2) - common)
    for i in range(len(different) - 1):
        if str(different[i]) == str('!' + different[i+1]) or str('!' + different[i]) == str(
                different[i+1]):
            return True
    return False


def create(temp: str):
    if temp[0] == '(' and temp[-1] == ')':
        return temp[1:-1]
    else:
        return temp


def create_2(part: list):
    temp = list()
    temp.append(part)
    temp.append(False)
    return temp