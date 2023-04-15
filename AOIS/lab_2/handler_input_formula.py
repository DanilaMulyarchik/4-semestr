def convert_for_list(formula):
    rez = []
    for i in formula:
        rez.append(i)
    return rez


def handler_input_formula(formula: str):
    formula = convert_for_list(formula)
    for i in range(len(formula)):
        if formula[i] == '!':
            formula[i] = ' not '
        elif formula[i] == '+':
            formula[i] = ' or '
        elif formula[i] == '*':
            formula[i] = ' and '
    logic_formula = ''.join(formula)
    return logic_formula


def take_arguments(formula: str):
    arguments = set()
    for i in range(len(formula)):
        if formula[i] == 'x':
            arguments.add(formula[i] + formula[i+1])
    arguments = list(arguments)
    arguments.sort(key=lambda x: int(x[1]))
    return arguments