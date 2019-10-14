import sys
sys.path.append('../doubly_linked_list')
#from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = []

    def enqueue(self, value):
        self.size += 1
        self.storage.insert(0, value)

    def dequeue(self):
        if self.size:
            front_el = self.storage[-1]
            del self.storage[-1]
            self.size -= 1
            return front_el
        else:
            return

    def len(self):
        return self.size
