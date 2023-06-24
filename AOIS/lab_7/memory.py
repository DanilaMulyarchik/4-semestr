def show(list):
    for i in list:
        print(i)


def dec_to_bin(dec_list: int):
    bin_list = []
    while dec_list:
        bin_list.append(dec_list % 2)
        dec_list //= 2
    for i in range(8 - len(bin_list)):
        bin_list.append(0)
    bin_list = reversed(bin_list)
    return bin_list


def bin_to_dec(bin_list):
    decimal_number = []
    temp_decimal_number = 0

    for i in bin_list:
        for j in range(len(i)):
            temp_decimal_number += 2 ** (len(i) - j - 1) * i[j]
        decimal_number.append(temp_decimal_number)
        temp_decimal_number = 0
    return decimal_number


def sort(memory, sort_flag):
    for i in range(len(memory)):
        for j in range(len(memory)-1-i):
            if comparison(memory[j], memory[j+1], sort_flag):
                memory[j], memory[j+1] = memory[j+1], memory[j]
    return memory, bin_to_dec(memory)


def comparison(list1, list2, flag):
    greater_variable, less_variable = 0, 0
    previous_greater_variable, previous_less_variable = 0, 0

    for i in range(len(list1)):
        less_variable = previous_less_variable or (list1[i] and not list2[i] and not previous_greater_variable)
        greater_variable = previous_greater_variable or (not list1[i] and list2[i] and not previous_less_variable)
        previous_greater_variable, previous_less_variable = greater_variable, less_variable

    if greater_variable:
        return flag
    elif less_variable:
        return not flag


def split(argument):
    temp_mask = []
    for i in argument:
        temp_mask.append(int(i)) if i != 'x' else temp_mask.append(i)
    return temp_mask


def search(argument, memory):
    argument = split(argument)
    rez = []
    for i in memory:
        find = True
        for j in range(len(i)):
            if not ((argument[j] == 0 and not i[j] or (argument[j] == 1 and i[j])) or argument[j] == 'x'):
                find = False
                break
        if find:
            rez.append(i)
    print(*(list(i) for i in rez) if rez else '---')