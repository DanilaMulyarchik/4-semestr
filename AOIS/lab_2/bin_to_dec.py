from handler_input_formula import *


def bin_to_dec(form, formula):
    rez = [0]
    arguments = take_arguments(formula)
    bin_power = len(arguments) - 1
    index = 0
    for i in form:
        if i == '*' or i == '+':
            bin_power = len(arguments) - 1
            rez.append(0)
            index += 1
            continue
        rez[index] += int(i) * (2**bin_power)
        bin_power -= 1
    return rez