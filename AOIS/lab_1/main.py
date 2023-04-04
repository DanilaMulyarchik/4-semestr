from perevod import perevod, vozvrat
from summa import sum
from difference import difference
from multiplication import multiplication
from division import division
from floa import summ_of_floating, from_float_to_decimal, string_to_list

while True:
    num_float = int(input("Число ==> "))
    num_float_1 = int(input("Число ==> "))
    print('0-->Exit\n1-->Suuma\n2-->Raznost\n3-->Proizvedenie\n4->Delenie\n5->Pooit sum')
    a = input('-->')
    if a == '0':
        break
    elif a == '1':
        print(perevod(num_float), '+', perevod(num_float_1), '=', sum(num_float, num_float_1))
        print(num_float, '+', num_float_1, '=', vozvrat(sum(num_float, num_float_1)))
    elif a == '2':
        print(perevod(num_float), '-', perevod(num_float_1), '=', difference(num_float, num_float_1))
        print(num_float, '-', num_float_1, '=', vozvrat(difference(num_float, num_float_1)))
    elif a == '3':
        print(perevod(abs(num_float)), '*', perevod(abs(num_float_1)), '=', multiplication(int(abs(num_float)), int(abs(num_float_1))))
        print(abs(num_float), '*', abs(num_float_1), '=', vozvrat(multiplication(int(abs(num_float)), int(abs(num_float_1)))))
    elif a == '4':
        print(perevod(abs(num_float)), '/', perevod(abs(num_float_1)), '=', division(int(abs(num_float)), int(abs(num_float_1))))
        print(num_float, '/', num_float_1, '=', vozvrat(division(int(abs(num_float)), int(abs(num_float_1)))))
    elif a == '5':
        num_float = float(input("Число ==> "))
        num_float_1 = float(input("Число ==> "))
        print(string_to_list(summ_of_floating(max(num_float, num_float_1), min(num_float, num_float_1))))
        print(from_float_to_decimal(summ_of_floating(max(num_float, num_float_1), min(num_float, num_float_1))))