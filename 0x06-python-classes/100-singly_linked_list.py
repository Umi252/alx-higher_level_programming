#!/usr/bin/python3

"""
This is the SinglyLinkedList module.
It defines the Node and SinglyLinkedList classes for a singly linked list.
"""


class Node:
    """
    This class represents a node of a singly linked list.
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a Node instance.

        :param data: The data to be stored in the node.
        :type data: int
        :param next_node: The next node in the linked list, defaults to None.
        :type next_node: Node, optional
        :raises TypeError: If data is not an integer.
        :raises TypeError: If next_node is not None or a Node object.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieve the data stored in the node.

        :return: The data stored in the node.
        :rtype: int
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data stored in the node.

        :param value: The data to be stored in the node.
        :type value: int
        :raises TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieve the next node in the linked list.

        :return: The next node in the linked list.
        :rtype: Node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node in the linked list.

        :param value: The next node in the linked list.
        :type value: Node
        :raises TypeError: If value is not None or a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be None or a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    This class represents a singly linked list.
    """
    def __init__(self):
        """
        Initializes an empty SinglyLinkedList instance.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list.

        :param value: The data to be stored in the new Node.
        :type value: int
        """
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and
            current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        :return: The linked list as a string.
        :rtype: str
        """
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)
