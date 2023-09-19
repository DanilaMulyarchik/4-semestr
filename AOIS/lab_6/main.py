from data import *
from table import *


table = Table(20)
data(table)

while True:
    print("Add->1\nDelete->2\nSearch->3\nPrint->4\n")

    choose = input("==>")
    if choose == '1':
        key = input("Key->  ")
        data = input("Data-> ")
        table.Add(key, data)
    elif choose == '2':
        key = input("Key-> ")
        table.delete(key)
    elif choose == '3':
        key = input("Key-> ")
        print(table.find(key))
    elif choose == '4':
        print(table.print_table())
    else:
        break