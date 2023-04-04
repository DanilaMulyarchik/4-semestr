from summa import *


def sum(bin_num1: list, bin_num2: list):
    number = peremennie.STR_ZERO
    rez = []
    for i in reversed(range(len(bin_num1))):
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

    return rez[::-1]


def multiplication(dec_num1: int, dec_num2: int):
    bin_num1, bin_num2, size = length_equalization(perevod(dec_num1), perevod(dec_num2))
    rez = []
    for i in range(size):
        rez += peremennie.STR_ZERO
    null = peremennie.INT_ZERO
    for i in reversed(range(size)):
        num = []
        if bin_num2[i] == peremennie.STR_ZERO:
            null += 1
        elif bin_num2[i] == peremennie.STR_ONE:
            for j in range(null):
                num += peremennie.STR_ZERO
            num += bin_num1[::-1]
            num = num[::-1]
            rez = rez[::-1]
            for t in range(len(num)-len(rez)):
                rez += peremennie.STR_ZERO
            rez = rez[::-1]
            rez = sum(rez, num)
            null += 1

    return rez