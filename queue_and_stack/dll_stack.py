import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.stack = DoublyLinkedList()
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def push(self, value):
        self.stack.add_to_tail(value)

    def pop(self):
        return self.stack.remove_from_tail()


    def len(self):
        return self.stack.length
