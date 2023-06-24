import memory
from random import randint

numbet_list = []
for i in range(10):
    numbet_list.append(randint(0, 50))
mem = []
for i in range(len(numbet_list)):
    mem.append(list(memory.dec_to_bin(numbet_list[i])))
print(numbet_list)
memory.show(mem)
while True:
    user_input = input('1 - sort;\n2 - find;\n')
    if user_input == '1':
        print('По возростанию\n', memory.sort(mem, False)[1])
        memory.show(memory.sort(mem, False)[0])
        print('По убыванию\n', memory.sort(mem, True)[1])
        memory.show(memory.sort(mem, True)[0])
    elif user_input == '2':
        argument = input('Enter mask(use "x" instead spaces): ')
        print('\nFind by mask: {}'.format(argument))
        memory.search(argument, mem)
    else:
        break