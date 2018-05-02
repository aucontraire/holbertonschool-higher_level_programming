#!/usr/bin/python3
"""Node and Singly Linked List.

This module provides a Node and a Linked List Class which adds sorted nodes

"""


class Node:
    """Node class. """

    def __init__(self, data, next_node=None):
        """__init__ method that sets data and next_node of node.
        Args:
            data (int): integer data of node
            next_node (Node, optional): next node, default is None
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets the data of the Node.
        Returns:
            data
        """
        return self.__data

    @property
    def next_node(self):
        """Gets the next_node of the Node.
        Returns:
            Node or None
        """
        return self.__next_node

    @data.setter
    def data(self, value):
        """data setter method that sets the data of node.
        Args:
            value (int): data of node
        Raises:
            TypeError: If `value` is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """next_node setter method that sets the next node.
        Args:
            value (Node, optional): Node or None
        Raises:
            TypeError: If `value` is not a Node object or None.
        """
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Singly linked list class."""

    def __init__(self):
        """__init__ method for singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """ sorted_insert method - inserts node in order
        Args:
            value (int): data of new node
        """
        new = Node(value)
        if self.__head is None:
            self.__head = new
        else:
            curr = self.__head
            while curr.next_node:
                if new.data >= curr.data and new.data <= curr.next_node.data:
                    new.next_node = curr.next_node
                    curr.next_node = new
                    break
                elif new.data < curr.data:
                    new.next_node = curr
                    self.__head = new
                    break
                curr = curr.next_node
            if new.data >= curr.data:
                curr.next_node = new
            else:
                new.next_node = curr
                self.__head = new

    def __str__(self):
        """string representation of singly linked list
        Returns:
            llstr: new-line separated list string
        """
        curr = self.__head
        llstr = ''
        if curr is None:
            llstr = ''
        elif curr.next_node is None:
            llstr += str(curr.data)
        else:
            while curr.next_node:
                llstr += str(curr.data) + '\n'
                curr = curr.next_node
            llstr += str(curr.data)
        return llstr


if __name__ == '__main__':
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
