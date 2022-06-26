#!/usr/bin/python3

"""
class Node - A class for an element in a singly linked list
"""


class Node:
    """Class for a node element """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not (value is None or isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""
class SinglyLinkedList - A class for a singly linked list
"""


class SinglyLinkedList:
    """Class to a portary a singly linked list """
    def __init__(self):
        self.__head = None

    def __str__(self):
        tmp, str = self.__head, ""
        while tmp:
            str += "{:d}\n".format(tmp.data)
            tmp = tmp.next_node
        return str[:-1]

    def sorted_insert(self, value):
        """Inserting an integer into the singly linked list"""
        if self.__head is None:
            self.__head = Node(value)
            return

        node = Node(value)
        if self.__head.data > node.data:
            node.next_node = self.__head
            self.__head = node
            return

        tmp = self.__head
        while tmp.next_node and tmp.next_node.data < node.data:
            tmp = tmp.next_node

        tmp.next_node, node.next_node = node, tmp.next_node
