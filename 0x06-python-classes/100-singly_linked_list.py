#!/usr/bin/python3
"""
"""


class Node:
    """
    """

    def __init__(self, data, next_node=None):
        """
        """
        self.data = data
        self.next_node = next_node

    @property
    def next_node(self):
        return self.__next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        if value != None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value



class SinglyLinkedList:
    """
    """

    def __init__(self):
        """
        """
        self.__head = None

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)
        else:
            curt = self.__head
            prev = None

            while curt and value > curt.data:
                prev = curt
                curt = curt.next_node
            if curt is None:
                prev.next_node = Node(value)
            elif curt is self.__head and prev is None:
                self.__head = Node(value, curt)
            else:
                nNode = Node(value, curt)
                prev.next_node = nNode

    def __repr__(self):
        curt = self.__head
        nList = ""

        while True:
            nList += str(curt.data)
            curt = curt.next_node
            if curt.next_node is None:
                break
            else:
                nList += "\n"
        return nList

sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)
