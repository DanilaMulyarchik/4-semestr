from calculation_table_metod import *
from table_metod import *
test = ['!((!x2+x3)*!(!x1*x3))', '!(!(x1+x2)*!x3)']


def main():
    for i in range(len(test)):
        print('\t\tTest № {}:{} '.format(i+1, test[i]))
        formula = test[i]
        Sknf = sknf(formula)
        Sdnf = sdnf(formula)
        print('Standart form\nSdnf ==> {}'.format(Sdnf))
        print('Sknf ==> {}'.format(Sknf))
        print('Calculation metod\nSdnf ==> {}'.format(calculation_method_sdnf(Sdnf)))
        print('Sknf ==> {}'.format(calculation_method_sknf(Sknf)))
        print('Calculation-table metod\nSdnf ==> {}\n{}'.format(ctm_sdnf(Sdnf)[0], ctm_sdnf(Sdnf)[1]))
        print('Sknf ==> {}\n{}'.format(ctm_sknf(Sknf)[0], ctm_sknf(Sknf)[1]))
        print('Table metod\n{}\nSdnf ==> {}'.format(table_metod(formula)[2], table_metod(formula)[0]))
        print('Sknf ==> {}'.format(table_metod(formula)[1]))


if __name__ == '__main__':
    main()