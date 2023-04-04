import peremennie
from perevod import *
from multiplication import sum
from summa import length_equalization


def count(bin_num: list):
    dec_num = peremennie.INT_ZERO
    for i in range(len(bin_num)):
        if bin_num[i] == peremennie.STR_ZERO:
            dec_num += peremennie.INT_ONE
        elif bin_num[i] == peremennie.STR_ONE:
            break
    return dec_num


def division(dec_num1: int, dec_num2: int):
    bin_temp1, bin_num2, size = length_equalization(perevod(dec_num1), perevod(dec_num2))
    bin_temp2 = dop(vozvrat(bin_num2))
    if not len(bin_temp2) == size:
        bin_temp2 = bin_temp2[::-1]
        while not len(bin_temp2) == size:
            bin_temp2 += peremennie.STR_ZERO
        bin_temp2 = bin_temp2[::-1]
    rez = []
    for i in range(size):
        rez += peremennie.STR_ZERO
    ed = []
    for i in range(size - 1):
        ed += peremennie.STR_ZERO
    ed += peremennie.STR_ONE
    first = count(bin_temp1)
    second = count(bin_num2)
    while first <= second:
        bin_temp1 = sum(bin_temp1, bin_temp2)
        rez = sum(ed, rez)
        first = count(bin_temp1)
    return rez
