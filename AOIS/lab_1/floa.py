import peremennie


def summ_of_floating(number_1, number_2):
    number_1 = perevod_flout_to_bin_for_sun(number_1)
    number_2 = perevod_flout_to_bin_for_sun(number_2)
    exp_1 = number_1.find(".") - number_1.find(peremennie.STR_ONE, 0, number_1.find(".")) - 1 if not number_1.find(peremennie.STR_ONE, 0, number_1.find(".")) == -1 else 0
    exp_2 = number_2.find(".") - number_1.find(peremennie.STR_ONE, 0, number_1.find(".")) - 1 if not number_1.find(peremennie.STR_ONE, 0, number_2.find(".")) == -1 else 0
    if exp_1 >= exp_2:
        diff_exp = exp_1 - exp_2
        number_summ2 = peremennie.STR_ZERO * diff_exp + number_2[:(number_2.find("."))] + number_2[(number_2.find(".") + 1):(
                len(number_2) - diff_exp)]
        number_summ1 = number_1[:(number_1.find("."))] + number_1[(number_1.find(".") + 1):]
    else:
        diff_exp = exp_2 - exp_1
        number_summ1 = peremennie.STR_ZERO * diff_exp + number_1[:(number_1.find("."))] + number_1[(number_1.find(".") + 1):(len(number_1) - diff_exp)]
        number_summ2 = number_2[:(number_2.find("."))] + number_2[(number_2.find(".") + 1):]
    temp_floating_summ = sum_diff_of_numbers(number_summ1, number_summ2)
    add_numbers = len(temp_floating_summ) - len(number_summ2)
    rez = temp_floating_summ[:(max(number_1.find("."), number_2.find("."))) + add_numbers] + "." + temp_floating_summ[(max(exp_1, exp_2) + add_numbers + 1):]
    rez = from_decimal_to_float(rez)
    return rez


def perevod_flout_to_bin_for_sun(number):
    if number == peremennie.INT_ZERO:
        return peremennie.INT_ZERO
    first_part = int(number)
    iterator = peremennie.INT_ZERO
    mantissa_size = peremennie.INT_TF
    point_part = number - float(first_part)
    second_part = dec_to_bin_add(first_part)
    if second_part.find(peremennie.STR_ONE) == -1:
        result = peremennie.STR_ZERO + "."
    else:
        result = second_part[second_part.find(peremennie.STR_ONE):] + "."
    while iterator <= (mantissa_size - len(result)):
        point_part *= peremennie.INT_TWO
        if int(point_part) == peremennie.INT_ZERO:
            result += peremennie.STR_ZERO
        elif int(point_part) == peremennie.INT_ONE:
            point_part -= peremennie.INT_ONE
            result += peremennie.STR_ONE
            if point_part == peremennie.INT_ZERO:
                result = result.ljust(23, peremennie.STR_ZERO)
    return result


def sum_diff_of_numbers(bin_num_1, bin_num_2):
    rez = ""
    number = peremennie.INT_ZERO
    bin_num_1, bin_num_2 = (comparing_length(bin_num_1, bin_num_2))
    for i in reversed(range(0, len(bin_num_1))):
        if (int(bin_num_1[i]) + int(bin_num_2[i]) == peremennie.INT_ONE) and (number == peremennie.INT_ZERO):
            rez = peremennie.STR_ONE + rez
        elif (int(bin_num_1[i]) + int(bin_num_2[i]) == peremennie.INT_ONE) and (number > peremennie.INT_ZERO):
            rez = peremennie.STR_ZERO + rez
        elif (int(bin_num_1[i]) + int(bin_num_2[i]) == peremennie.INT_TWO) and (number > peremennie.INT_ZERO):
            rez = peremennie.STR_ONE + rez
        elif (int(bin_num_1[i]) + int(bin_num_2[i]) == peremennie.INT_ZERO) and (number > peremennie.INT_ZERO):
            rez = peremennie.STR_ONE + rez
            number -= peremennie.INT_ONE
        elif (int(bin_num_1[i]) + int(bin_num_2[i]) == peremennie.INT_ZERO) and (number == peremennie.INT_ZERO):
            rez = peremennie.STR_ZERO + rez
        elif (int(bin_num_1[i]) + int(bin_num_2[i]) == peremennie.INT_TWO) and (number == peremennie.INT_ZERO):
            rez = peremennie.STR_ZERO + rez
            number += peremennie.INT_ONE

    if number > peremennie.INT_ZERO:
        rez = peremennie.STR_ONE + rez

    return rez


def from_decimal_to_float(float_num):
    if peremennie.STR_ONE in float_num[:float_num.find(".")]:
        exp_sign = peremennie.INT_ONE
    else:
        exp_sign = -peremennie.INT_ONE
    sign_bit = peremennie.STR_ZERO
    if float_num.find(peremennie.STR_ONE, peremennie.INT_ZERO, float_num.find(".")) == -peremennie.INT_ONE:
        exp_bits = dec_to_bin_straight(peremennie.INT_OTS + ((float_num.find(peremennie.STR_ONE) - float_num.find(".")) * exp_sign))[-peremennie.INT_EIGHT:]
    else:
        exp_bits = dec_to_bin_straight(peremennie.INT_OTS + ((float_num.find(".") - float_num.find(peremennie.STR_ONE) - peremennie.INT_ONE) * exp_sign))[-peremennie.INT_EIGHT:]
    float_num = float_num[:float_num.find(".")] + float_num[float_num.find(".") + 1:]
    mantissa = float_num[float_num.find(peremennie.STR_ONE) + peremennie.INT_ONE:]
    rez = sign_bit + " " + exp_bits + " " + mantissa
    return rez


def dec_to_bin_straight(float_num):
    bin = ""
    tick_of_actions, clone_of_dec_num, tick_of_bits = peremennie.INT_ZERO, float_num, peremennie.INT_ZERO
    rez = ""
    if abs(float_num) < peremennie.INT_ONE_HANGRED:
        bit_size = peremennie.INT_EIGHT
    else:
        bit_size = peremennie.INT_EIGHT * peremennie.INT_TWO
    if float_num < peremennie.INT_ZERO:
        clone_of_dec_num = -float_num
    if float_num == peremennie.INT_ZERO:
        bin = str(peremennie.INT_ZERO)
    while clone_of_dec_num >= peremennie.INT_ONE:
        symbol = str(int(clone_of_dec_num % peremennie.INT_TWO))
        bin = bin + symbol
        tick_of_bits += peremennie.INT_ONE
        clone_of_dec_num /= peremennie.INT_TWO
        tick_of_actions += peremennie.INT_ONE
        rez = bin[::-1]
    if tick_of_bits < bit_size:
        rez = rez.zfill(bit_size)
    if float_num < peremennie.INT_ZERO:
        rez = str(1) + rez[1:]
    else:
        rez = str(0) + rez[1:]
    return rez


def dec_to_bin_add(float_num):
    if float_num < peremennie.INT_ZERO:
        rez = dec_to_bin_rev(float_num)
        iterator = peremennie.INT_ONE
        help_add = True
        while help_add:
            temp_rez = rez[-iterator:len(rez)]
            if rez[-iterator] == peremennie.STR_ZERO:
                temp_rez = temp_rez.replace(peremennie.STR_ONE, peremennie.STR_ZERO)
                temp_rez = temp_rez.replace(peremennie.STR_ZERO, peremennie.STR_ONE)
                temp_rez = temp_rez.replace(peremennie.STR_TWO, peremennie.STR_ZERO)
                rez = rez[:-iterator] + temp_rez
                help_add = False
            else:
                iterator += peremennie.INT_ONE
    else:
        rez = dec_to_bin_straight(float_num)
    return rez


def dec_to_bin_rev(float_num):
    sign = ''
    if float_num < peremennie.INT_ZERO:
        sign += peremennie.STR_ONE
        rez = dec_to_bin_straight(float_num)
        rez = rez.replace(peremennie.STR_ONE, peremennie.STR_ZERO)
        rez = rez.replace(peremennie.STR_ZERO, peremennie.STR_ONE)
        rez = rez.replace(peremennie.STR_TWO, peremennie.STR_ZERO)
    else:
        sign += peremennie.STR_ZERO
        rez = dec_to_bin_straight(float_num)
    rez = sign + rez[1:]
    return rez


def comparing_length(bin_num1, bin_num2):
    max_size = max(len(bin_num1), len(bin_num2))
    if bin_num1[0] and bin_num2[0] == peremennie.STR_ZERO:
        bin_num1 = bin_num1.zfill(max_size)
        bin_num2 = bin_num2.zfill(max_size)
    if bin_num1[0] == peremennie.STR_ONE:
        bin_num1 = bin_num1.rjust(max_size, peremennie.STR_ONE)
    if bin_num2[0] == peremennie.STR_ONE:
        bin_num2 = bin_num2.rjust(max_size, peremennie.STR_ONE)
    return bin_num1, bin_num2


def from_float_to_decimal(float_num: str):
    float_num = float_num[:float_num.find(" ")] + \
                float_num[(float_num.find(" ") + peremennie.INT_ONE):float_num.rfind(" ")] + \
                float_num[float_num.rfind(" ") + peremennie.INT_ONE:]
    decimal_mantissa = peremennie.FLOAT_ZERO
    for i in range(9, len(float_num)):
        decimal_mantissa += int(float_num[i]) * pow(peremennie.INT_TWO, -(i - peremennie.INT_EIGHT))
    exp = int(from_binary_to_decimal(peremennie.STR_ZERO + float_num[peremennie.INT_ONE:peremennie.INT_NINE])) - peremennie.INT_OTS
    if float_num[0] == peremennie.STR_ONE:
        sign_before = "-"
    else:
        sign_before = ""
    rez = sign_before + str((peremennie.INT_ONE + decimal_mantissa) * pow(peremennie.INT_TWO, exp))
    return rez


def from_binary_to_decimal(bin_num):
    rez = peremennie.INT_ZERO
    if bin_num.startswith(peremennie.STR_ONE):
        rez += ((-int(bin_num[1])) * pow(peremennie.INT_TWO, (len(bin_num) - peremennie.INT_TWO)))
        for iterator in range(2, len(bin_num)):
            rez += ((int(bin_num[iterator])) * pow(peremennie.INT_TWO, (len(bin_num) - (iterator + peremennie.INT_ONE))))
    elif bin_num.startswith(peremennie.STR_ZERO):
        for iterator in range(0, len(bin_num)):
            rez += (int(bin_num[iterator]) * pow(peremennie.INT_TWO, (len(bin_num) - (iterator + peremennie.INT_ONE))))
    return rez


def string_to_list(bin_num: str):
    rez = []
    for i in range(len(bin_num)):
        if bin_num[i] == ' ':
            continue
        rez += bin_num[i]
    return rez


