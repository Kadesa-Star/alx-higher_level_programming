#!/usr/bin/python3
class Node:
    """this class defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialize a node with data and optional next nod.


        Args:
            data (int): the data to be stored in the node
            next_node (Node): next node in the linked list.

        Raises:
            TypeError: if data not int or next_node is not node object
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the dataa of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """ set the data of the node


        Args:
            value (int): the data to be set

        Raises:
            TypeError: if value is not an int
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ set the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ setter for next_node


        Args:
            value (Node): the next node to be set

        Raises:
            TypeError: if the value is not a node object
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A class that defines a singly linked list."""

    def __init__(self):
        """initialize an empty singly linked list"""
        self.head = None

    def __str__(self):
        """Return a st string representation of the linked list


        Returns:
            str: string representation of the linkedlist
        """

        result = ""
        current = self.head
        while current:
            result += str(current.data)
            if current.next_node is not None:
                result += "\n"
            current = current.next_node
        return result

    def sorted_insert(self, value):
        """insert a new node into the correct sorted postion in the list

        Args:
            value (int): the value of the new node to be inserted
        """

        new_node = Node(value)
        if not self.head or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
