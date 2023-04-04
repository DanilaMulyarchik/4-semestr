import peremennie


def perevod(num):
    if num >= peremennie.INT_ZERO:
        return pramoi(num)
    else:
        return dop(abs(num))


def pramoi(num):
    b = []

    while num > peremennie.INT_ZERO:
        b += str(num % peremennie.INT_TWO)
        num //= peremennie.INT_TWO

    while not len(b) % peremennie.INT_EIGHT == peremennie.INT_ZERO:
        b += peremennie.STR_ZERO

    b = b[::-1]

    return b


def dop(num):

    b = []

    while num > peremennie.INT_ZERO:
        b += str(num % peremennie.INT_TWO)
        num //= peremennie.INT_TWO

    while not len(b) % peremennie.INT_EIGHT == peremennie.INT_ZERO:
        b += peremennie.STR_ZERO

    b = b[::-1]

    b_1 = []

    for i in reversed(range(len(b))):
        if b[i] == peremennie.STR_ZERO:
            b_1 += peremennie.STR_ONE
        elif b[i] == peremennie.STR_ONE:
            b_1 += peremennie.STR_ZERO

    b_1 = b_1[::-1]

    number = peremennie.STR_ONE

    for i in reversed(range(len(b_1))):
        if b_1[i] == peremennie.STR_ZERO and number == peremennie.STR_ONE:
            b_1[i] = peremennie.STR_ONE
            number = peremennie.STR_ZERO
        elif b_1[i] == peremennie.STR_ONE and number == peremennie.STR_ONE:
            b_1[i] = peremennie.STR_ZERO

    return b_1


def vozvrat(b: list):
    a = peremennie.INT_ZERO
    for i in reversed(range(1, len(b))):
        a += (peremennie.INT_TWO ** (len(b) - i - 1)) * int(b[i])
    if b[0] == peremennie.STR_ONE:
        a = peremennie.INT_ZERO - a
    return a