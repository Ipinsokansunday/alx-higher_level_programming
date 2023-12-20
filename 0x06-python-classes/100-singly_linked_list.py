#!/usr/bin/python3
"""
Class Node that defines a node of a singly linked list.
Class SinglyLinkedList that defines a singly linked list.
"""

class Node:
    """
    Class Node that defines a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new instance of the Node class.

        Parameters:
        - data: The data for the node.
        - next_node: The next node in the linked list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method for retrieving the value of data.

        Returns:
        - int: The data of the node.
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        """
        Setter method for setting the value of data.

        Parameters:
        - value: The data value to be set.

        Raises:
        - TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter method for retrieving the value of next_node.

        Returns:
        - Node or None: The next node in the linked list.
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """
        Setter method for setting the value of next_node.

        Parameters:
        - value: The next_node value to be set.

        Raises:
        - TypeError: If next_node is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Class SinglyLinkedList that defines a singly linked list.
    """

    def __init__(self):
        """
        Initializes a new instance of the SinglyLinkedList class.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (increasing order).

        Parameters:
        - value: The data value for the new Node.
        """
        new_node = Node(value)

        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node

            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Converts the linked list to a string for printing.

        Returns:
        - str: The string representation of the linked list.
        """
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return (result)
