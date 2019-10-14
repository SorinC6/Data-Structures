#from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = []

    def push(self, value):
        self.size += 1
        self.storage.append(value)

    def pop(self):
        if self.size:
            pop_element = self.storage[-1]
            self.storage.pop()
            self.size -= 1
            return pop_element
        else:
            return

    def len(self):
        return self.size
