from random import randint


def show(list):
    for i in list:
        print(i)


def create_list():
    numbet_list = []
    for i in range(10):
        numbet_list.append(randint(0, 50))
    mem = []
    for i in range(len(numbet_list)):
        mem.append(list(dec_to_bin(numbet_list[i])))
    return mem, numbet_list


def dec_to_bin(dec_list: int):
    bin_list = []
    while dec_list:
        bin_list.append(dec_list % 2)
        dec_list //= 2
    for i in range(8 - len(bin_list)):
        bin_list.append(0)
    bin_list = bin_list[::-1]
    return bin_list


def bin_to_dec(bin_list):
    dec_number = []
    temp_dec_number = 0

    for i in bin_list:
        for j in range(len(i)):
            temp_dec_number += 2 ** (len(i) - j - 1) * i[j]
        dec_number.append(temp_dec_number)
        temp_dec_number = 0
    return dec_number


def sort(memory, sort_flag):
    for i in range(len(memory)):
        for j in range(len(memory)-1-i):
            if comparison(memory[j], memory[j+1], sort_flag):
                memory[j], memory[j+1] = memory[j+1], memory[j]
    return memory, bin_to_dec(memory)


def comparison(number1, number2, f):
    g_var, l_var = 0, 0
    prev_g_var, prev_l_var = 0, 0

    for i in range(len(number1)):
        if prev_l_var:
            l_var = prev_l_var
        elif number1[i] and not number2[i] and not prev_g_var:
            l_var = number1[i] and not number2[i] and not prev_g_var
        if prev_g_var:
            g_var = prev_g_var
        elif not number1[i] and number2[i] and not prev_l_var:
            g_var = (not number1[i] and number2[i] and not prev_l_var)
        prev_g_var, prev_l_var = g_var, l_var

    return f if g_var else not f


def split(argument):
    temp_mask = []
    for i in argument:
        temp_mask.append(int(i)) if i != '.' else temp_mask.append(i)
    return temp_mask


def search(argument, memory):
    argument = split(argument)
    rez = []
    for i in memory:
        find = True
        for j in range(len(i)):
            if not ((argument[j] != 0 and i[j]) or (argument[j] != 1 and not i[j])) and argument[j] != '.':
                find = False
                break
        if find:
            rez.append(i)
    print(*(list(i) for i in rez) if rez else 'No')