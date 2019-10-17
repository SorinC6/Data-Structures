from doubly_linked_list import DoublyLinkedList
# import sys
# sys.path.append('../doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = []
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        #self.size += 1
        # self.storage.insert(0, value)
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.storage.length:
            #front_el = self.storage[-1]
            #del self.storage[-1]
            #self.size -= 1
            # return front_el
            return self.storage.remove_from_head()
        else:
            return

    def len(self):
        return self.storage.length
