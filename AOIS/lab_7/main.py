from memory import *


mem, number_list = create_list()


print(number_list)
show(mem)
while True:
    choose = input('1 - sort;\n2 - find;\n')
    if choose == '1':
        print('По возростанию\n', sort(mem, False)[1])
        show(sort(mem, False)[0])
        print('По убыванию\n', sort(mem, True)[1])
        show(sort(mem, True)[0])
    elif choose == '2':
        argument = input('Введите маску, используя "." вместо пробела ')
        print('\nFind by mask: {}'.format(argument))
        search(argument, mem)
    else:
        break