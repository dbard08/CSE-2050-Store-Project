from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add_first(self, item):
        new_node = Node(item, self.head)
        self.head = new_node
        if self.count == 0:
            self.tail = new_node
        self.count += 1

    def add_last(self, item):
        new_node = Node(item)
        if self.count == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def remove_first(self):
        if self.is_empty():
            return None
        data = self.head.data
        self.head = self.head.next
        self.count -= 1
        if self.count == 0:
            self.tail = None
        return data

    def get_first(self):
        if self.is_empty():
            return None
        return self.head.data

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count
