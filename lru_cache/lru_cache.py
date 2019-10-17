from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.max_number_of_nodes = limit
        self.current_nodes = 0
        self.cache = {}
        self.order = DoublyLinkedList()

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        value = None
        # if it's in the cache, move the node to the front of our DLL
        if key in self.cache:
            node = self.cache[key]
            value = node.value[1]
            self.order.move_to_front(node)
        return value

    """
    Case 1: Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache.
​
    Case 2: If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room.
    ​
    Case 3: Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):

        # 3
        if key in self.cache:
            node = self.cache[key]
            self.order.move_to_front(node)
            node.value = (key, value)

        else:
            # 2
            if self.current_nodes == self.max_number_of_nodes:
                del self.cache[self.order.tail.value[0]]
                self.order.remove_from_tail()
                self.current_nodes -= 1

            # 1
            self.order.add_to_head((key, value))
            self.cache[key] = self.order.head
            self.current_nodes += 1
