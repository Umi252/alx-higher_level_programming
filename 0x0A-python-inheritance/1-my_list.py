#!/usr/bin/python3
"""
This module defines the MyList class, which inherits from the built-in list class.
"""

class MyList(list):
    """
    MyList inherits from the built-in list class.

    Public Methods:
        print_sorted(self): Print the list in ascending order.
    """

    def print_sorted(self):
        """
        Print the list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
