from data import *
from table import *


table = Table(20)
data(table)

while True:
    print("Add - press 1")
    print("Delete - press 2")
    print("Search - press 3")
    print("Print - press 4")

    print("To exit - press 0")
    choose = input("Enter choise: ")
    if choose == '1':
        key = input("Enter key: ")
        data = input("Enter data: ")
        table.insert(key, data)
    elif choose == '2':
        word = input("Enter key: ")
        table.delete(word)
    elif choose == '3':
        word = input("Enter key: ")
        print(table.find(word))
    elif choose == '4':
        print(table.print_table())
    else:
        break
