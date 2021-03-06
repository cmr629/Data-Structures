import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.queue = DoublyLinkedList()

    def enqueue(self, value):
        self.queue.add_to_head(value)

    def dequeue(self):
        return self.queue.remove_from_tail()
     

    def len(self):
        return self.queue.length
       