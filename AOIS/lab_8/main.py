from associatmemory import AssociatMemory


def main():
    memory = AssociatMemory()
    print('Memory in normal form: ')
    memory.print_normal_from()

    memory.convert_to_diagonal()

    print('\n\n\nMemory in diagonal form: ')
    print(memory)

    user_input = int(input('\n\n\nTake word by index: '))
    print(' '.join([str(i) for i in memory.read_word(user_input)]))

    user_input = int(input('\n\n\nTake line by index: '))
    print(' '.join([str(i) for i in memory.get_line(user_input)]))

    print('\n\n\nFunction: ')
    print('The function 1 for 1, 2 and 3 words: {}'.format(memory.f_1([1, 2, 3])))
    print('The function 3 for 1 word: {}'.format(memory.f_3([1, 2])))
    print('The function 12 for 4 word: {}'.format(memory.f_12([4, 2])))
    print('The function 14 for 1, 2 and 5 words: {}'.format(memory.f_14([1, 2, 5])))

    print('\n\n\nMemory in diagonal form:')
    print(memory)
    print('\n\n\nMemory in normal form: ')
    memory.print_normal_from()

    print('\n\n\nArifmetic operation: ')
    memory.arimetic_operation([0, 0, 1])

    print('\nMemory in diagonal form:')
    print(memory)
    print('\n\nMemory in normal form: ')
    memory.print_normal_from()

    print('\n\n\nSearch: ')
    print(memory.search([0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0]))


if __name__ == '__main__':
    main()