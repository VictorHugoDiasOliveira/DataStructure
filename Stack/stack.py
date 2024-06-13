from node import Node

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, element):
        node = Node(element)
        node.next = self.top
        self.top = node
        self._size = self._size+1

    def pop(self):
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size = self._size-1
            return node.data
        raise IndexError("The stack is empty")

    def peek(self):
        if self._size > 0:
            return self.top.data
        raise IndexError("The stack is empty")

    def __len__(self):
        return self._size

    def __repr__(self):
        string = ""
        pointer = self.top
        while(pointer):
            string = string + str(pointer.data) + "\n"
            pointer = pointer.next
        return string

    def __str__(self):
        return self.__repr__()