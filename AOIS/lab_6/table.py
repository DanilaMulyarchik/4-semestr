from elemrnt_class import Element
from prettytable import PrettyTable
from typing import List, Optional


INCREASE = 10
LENGTH = 100


class Table:
    def __init__(self, size: int):
        self.size = size
        self.count = 0
        self.table: List[Optional[Element]] = [None] * size

    def __take_hash_address(self, key):
        hash_adress = hash(key) % self.size
        return hash_adress

    def insert(self, key: str, value: str):
        if self.count == self.size:
            self.change_length()
        hash_address = self.__take_hash_address(key)
        node = self.table[hash_address]
        while node is not None:
            if node.key == key:
                node.value = value
                return
            node = node.next
        if self.table[hash_address] is None:
            self.table[hash_address] = Element(key, value)
            self.count += 1
        else:
            self._push_to_same_hash_list(self.table[hash_address], key, value)
            self.count += 1

    def find(self, key: str):
        hash_address = self.__take_hash_address(key)
        node = self.table[hash_address]
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next
        print("{} no such element in hash table".format(key))
        return ""

    def delete(self, key: str):
        hash_address = self.__take_hash_address(key)
        curr_node = self.table[hash_address]

        if curr_node is None:
            return
        elif curr_node.key == key and curr_node.next is None:
            self.table[hash_address] = None
            self.count -= 1
            return
        elif curr_node.key == key and curr_node.next is not None:
            self.table[hash_address] = curr_node.next
            self.count -= 1
            return

        while curr_node is not None:
            if curr_node.key == key:
                curr_node.previous.next = curr_node.next
                if curr_node.next is not None:
                    curr_node.next.previous = curr_node.previous
                return
            curr_node = curr_node.next

    def _push_to_same_hash_list(self, node: Element, key: str, value: str):
        new_node = Element(key, value)
        node.previous = new_node
        new_node.next = node
        self.table[hash(key) % self.size] = new_node

    def change_length(self):
        self.size += INCREASE
        new_table = [None] * self.size
        for i in range(self.size - INCREASE):
            if self.table[i] is not None:
                node = self.table[i]
                while node is not None:
                    next_node = node.next
                    hash = hash(node.key)
                    pos = hash % self.size
                    if new_table[pos] is None:
                        new_table[pos] = node
                        node.next = None
                        node.previous = None
                    else:
                        self._push_to_hash_list_copy(new_table[pos], node.key,
                                                     node.value, new_table)
                    node = next_node
        self.table = new_table

    def _push_to_hash_list_copy(self, node: Element, key: str, value: str, new_table):
        new = Element(key, value)
        node.previous = new
        new.next = node
        new_table[hash(key) % self.size] = new

    def print_table(self):
        table = PrettyTable()
        table.field_names = ["Address", "Key", "Value"]

        for i in range(self.size):
            if self.table[i] is not None:
                curr_node = self.table[i]
                while curr_node is not None:
                    table.add_row([
                        hash(curr_node.key) % self.size,
                        curr_node.key,
                        curr_node.value if len(curr_node.value) < LENGTH else curr_node.value[:LENGTH] + '...'
                    ])
                    curr_node = curr_node.next

        return table