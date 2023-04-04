from perevod import *


def back_to_direct_code(rez: list):

    num = peremennie.STR_ONE

    for i in reversed(range(len(rez))):
        if rez[i] == peremennie.STR_ONE:
            rez[i] = peremennie.STR_ZERO
        elif rez[i] == peremennie.STR_ZERO:
            rez[i] = peremennie.STR_ONE

    for i in reversed(range(len(rez))):
        if rez[i] == peremennie.STR_ZERO and num == peremennie.STR_ONE:
            rez[i] = peremennie.STR_ONE
            num = peremennie.STR_ZERO
        elif rez[i] == peremennie.STR_ONE and num == peremennie.STR_ONE:
            rez[i] = peremennie.STR_ZERO
    rez[0] = peremennie.STR_ONE

    return rez


def length_equalization(bin_num1: list, bin_num2: list):
    size = max(len(bin_num1), len(bin_num2))

    if len(bin_num1) == size:
        bin_num2 = bin_num2[::-1]
        while not len(bin_num2) == size:
            bin_num2 += peremennie.STR_ZERO
        bin_num2 = bin_num2[::-1]
    elif len(bin_num2) == size:
        bin_num1 = bin_num1[::-1]
        while not len(bin_num1) == size:
            bin_num1 += peremennie.STR_ZERO
        bin_num1 = bin_num1[::-1]

    return bin_num1, bin_num2, size


def sum(dec_num1: int, dec_num2: int):

    bin_num1, bin_num2, size = length_equalization(perevod(dec_num1), perevod(dec_num2))

    rez = []
    number = peremennie.STR_ZERO

    for i in reversed(range(size)):
        if bin_num1[i] == peremennie.STR_ZERO and bin_num2[i] == peremennie.STR_ZERO:
            if number == peremennie.STR_ONE:
                rez += peremennie.STR_ONE
                number = peremennie.STR_ZERO
                continue
            rez += peremennie.STR_ZERO
            number = peremennie.STR_ZERO
        elif bin_num1[i] == peremennie.STR_ONE and bin_num2[i] == peremennie.STR_ONE:
            if number == peremennie.STR_ONE:
                rez += peremennie.STR_ONE
                number = peremennie.STR_ONE
                continue
            rez += peremennie.STR_ZERO
            number = peremennie.STR_ONE
        elif (bin_num1[i] == peremennie.STR_ZERO and bin_num2[i] == peremennie.STR_ONE) or (bin_num1[i] == peremennie.STR_ONE and bin_num2[i] == peremennie.STR_ZERO):
            if number == peremennie.STR_ONE:
                rez += peremennie.STR_ZERO
                number = peremennie.STR_ONE
                continue
            rez += peremennie.STR_ONE
            number = peremennie.STR_ZERO

    rez = rez[::-1]

    return rez if rez[0] == peremennie.STR_ZERO else back_to_direct_code(rez)