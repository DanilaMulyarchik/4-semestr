from sdnf import *
from sknf import *
from index import *

# !((!x2+!x3)*!(!x1*!x3))


formula = input('==>')
print('Формула: {}'.format(formula))
print('СКНФ ==> ', sknf(formula))
print('CКНФ в бинорном виде ==>', sknf_number_form(formula)[0])
print('СКНФ в числовой форме ==>', sknf_number_form(formula)[1])
print('СДНФ ==> ', sdnf(formula))
print('CДНФ в бинорном виде ==>', sdnf_number_form(formula)[0])
print('СДНФ в числовой форме ==>', sdnf_number_form(formula)[1])
print('Индекс = ', index(formula))
print('Таблица:\n', create_logic_table(formula)[0])