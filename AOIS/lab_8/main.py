from ASM import ASM


def main():
    memory = ASM()

    normal_form(memory)

    memory.convert_to_diagonal()
    dioganal_form(memory)

    input_word('word', memory)
    input_word('line', memory)

    function(memory)

    dioganal_form(memory)
    normal_form(memory)

    arifmetica(memory)
    dioganal_form(memory)
    normal_form(memory)

    search(memory)


def search(memory):
    print('\n\n\nSearch: ')
    print(memory.search([0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0]))


def arifmetica(memory):
    print('арифметические операции: ')
    memory.arimetic_operation([0, 0, 1])


def input_word(parametr, memory):
    user_input = int(input('\n\n\nTake {} by index: '.format(parametr)))
    print(' '.join([str(i) for i in memory.read_word(user_input)]))


def function(memory):
    print('Функции:')
    print('Функция 1 для 1, 2 и 3 слов:', end=' ')
    print(memory.f_1([1, 2, 3]))
    print('Функция 3 для 1 слова:', end=' ')
    print(memory.f_3([1, 2]))
    print('Функция 12 для 4 слов:', end=' ')
    print(memory.f_12([4, 2]))
    print('Функция 14 для 1, 2 и 5 слов:', end=' ')
    print(format(memory.f_14([1, 2, 5])))


def normal_form(memory):
    print('Память в нормальной форме:')
    memory.print_normal_from()


def dioganal_form(memory):
    print('Память в диогональной форме ')
    print(memory)


if __name__ == '__main__':
    main()