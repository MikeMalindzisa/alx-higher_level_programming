#!/usr/bin/python3
"""
This module defines the Node and SinglyLinkedList classes.
"""


class Node:
    """
    Represents a node of a singly linked list.

    Attributes:
        data (int): The data stored in the node.
        next_node (Node): The next node in the linked list.
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a new Node instance.

        Args:
            data (int): The data stored in the node.
            next_node (Node): The next node in the linked list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data stored in the node.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data stored in the node.

        Args:
            value (int): The new data value.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the next node in the linked list.

        Returns:
            Node: The next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node in the linked list.

        Args:
            value (Node): The new next node.

        Raises:
            TypeError: If value is not None or a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Represents a singly linked list.

    Attributes:
        head: The first node in the linked list.
    """
    def __init__(self):
        """
        Initializes a new SinglyLinkedList instance.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the linked list.

        Args:
            value (int): The value to be inserted.
        """
        new_node = Node(value)

        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Converts the linked list to a string for printing.

        Returns:
            str: The linked list as a string.
        """
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
