from random import choice
import copy


class ASM:
    def __init__(self) -> None:
        self.size = 16
        self.memory = [[choice([0, 1]) for i in range(self.size)] for j in range(self.size)]
        self.memory_diagonal = self.memory

    def f(self, number):
        new = []
        f_word = self.read_word(number[0])
        s_word = self.read_word(number[1])
        for i in range(self.size):
            rez = f_word[i] and s_word[i]
            new.append(rez)
        self.set_word(new, number[2])
        return self.join_str(new)

    def print_normal_from(self):
        if self.memory_diagonal != self.memory:
            for i in self.to_normal():
                memory_row = ' '.join([str(j) for j in i])
                print(memory_row)
        else:
            for i in self.memory:
                memory_row = ' '.join([str(j) for j in i])
                print(memory_row)

    def join_str(self, info):
        return ''.join([str(i) for i in info])

    def f_1(self, number):
        return self.f(number)

    def f_3(self, number):
        new = self.read_word(number[0])
        return self.join_str(new)

    def f_12(self, number):
        new = self.read_word(number[0])
        new = [0 if x == 1 else 1 for x in new]
        self.set_word(new, number[0])
        return self.join_str(new)

    def f_14(self, number):
        return self.f(number)

    def _transposed_memory(self):
        transposed_memory = []
        for j in range(self.size):
            row = []
            for i in range(self.size):
                row.append(self.memory_diagonal[i][j])
            transposed_memory.append(row)
        self.memory_diagonal = transposed_memory

    def _s_word(self, first, second):
        word = first + second
        return word

    def read_word(self, column):
        self._transposed_memory()
        first_part = self.memory_diagonal[column][column:]
        second_part = self.memory_diagonal[column][:column]
        word = self._s_word(first_part, second_part)
        self._transposed_memory()
        return word

    def set_word(self, word, column):
        self._transposed_memory()
        first_part = word[self.size - column:]
        second_part = word[:self.size - column]
        self.memory_diagonal[column] = self._s_word(first_part, second_part)
        self._transposed_memory()

    def __str__(self):
        for i in self.memory_diagonal:
            memory_row = ' '.join([str(j) for j in i])
            print(memory_row)
        return ''

    def get_line(self, column):
        return self.to_normal()[column]

    def convert_to_diagonal(self):
        self.memory_diagonal = [[self.memory_diagonal[i][j] for i in range(self.size)] for j in range(self.size)]
        for i in range(self.size):
            self.memory_diagonal[i] = self.memory_diagonal[i][self.size - i:] + self.memory_diagonal[i][:self.size - i]
        self.memory_diagonal = [[self.memory_diagonal[i][j] for i in range(self.size)] for j in range(self.size)]

    def search(self, word):
        memory = self.to_normal()
        memory = [[memory[i][j] for i in range(self.size)] for j in range(self.size)]

        print('Input word: {}'.format(word))
        print('\n')

        more_then_input_word = []
        less_then_input_word = []

        for i in memory:
            if self.comp(word, i):
                more_then_input_word.append(i)
            else:
                less_then_input_word.append(i)

        print('The words, that more then input word')
        smallest_word = self.compare_words(more_then_input_word, False)
        print('\n\n\nThe words, that less then input word')
        biggest_word = self.compare_words(less_then_input_word, True)
        print('Result: ')
        return ' '.join([str(i) for i in biggest_word]) + '\n' + ' '.join([str(i) for i in smallest_word])

    def compare_words(self, words, flag):
        for i in words:
            word = i
            print(self.join_str(i))
            for j in words:
                if not flag:
                    if not self.comp(word, j):
                        word = j
                else:
                    if self.comp(word, j):
                        word = j
        return word

    def comp(self, f_word, s_word):
        g_variable = 0
        l_variable = 0
        prev_g_var = 0
        prev_l_var = 0

        for i in range(len(f_word)):
            if prev_g_var:
                g_variable = prev_g_var
            elif not f_word[i] and s_word[i] and not prev_l_var:
                g_variable = not f_word[i] and s_word[i] and not prev_l_var
            if prev_l_var:
                l_variable = prev_l_var
            elif f_word[i] and not s_word[i] and not prev_g_var:
                l_variable = f_word[i] and not s_word[i] and not prev_g_var
            prev_g_var, prev_l_var = g_variable, l_variable

        return g_variable

    def to_normal(self):
        normal_form = []
        self.memory_diagonal = [[self.memory_diagonal[i][j] for i in range(self.size)] for j in range(self.size)]
        matrix = copy.deepcopy(self.memory_diagonal)
        self.memory_diagonal = [[self.memory_diagonal[i][j] for i in range(self.size)] for j in range(self.size)]
        for i in range(len(matrix)):
            normal_form.append(self.read_word(i))
        return [[normal_form[i][j] for i in range(self.size)] for j in range(self.size)]

    def arimetic_operation(self, mask):
        memory = [[self.to_normal()[i][j] for i in range(self.size)] for j in range(self.size)]
        pass_val_by_mask = [x for x in memory if x[:3] == mask]
        print('Mask: {}'.format(self.join_str(mask)))
        print('Words that pass validation: ')
        new = []
        for i in pass_val_by_mask:
            memory_row = self.join_str(i)
            print('{}, index - {}'.format(memory_row, memory.index(i)))
            new.append((memory.index(i), self.addiction(i)))

        print('Words after arifmetic operation: ')
        for i in new:
            memory_row = self.join_str(i[1])
            print(memory_row)
            self.set_word(i[1], i[0])

    def addiction(self, word):
        A = word[3:7]
        B = word[7:11]
        S = []
        bit = 0
        for j in range(1, 5):
            S.append(A[-j] + B[-j] + bit)
            if S[-1] == 2:
                S[-1] = 0
                bit = 1
            elif S[-1] == 1:
                S[-1] = 1
                bit = 0
            elif S[-1] == 3:
                S[-1] = 1
                bit = 1
            else:
                S[-1] = 0
        S.append(bit)

        S = list(S[::-1])
        return word[:11] + S