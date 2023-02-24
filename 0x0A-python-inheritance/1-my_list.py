#!/usr/bin/python3
# 1-my_list.py
"""Defines an inherited list class Mylist"""


classs Mylist(list):
    """Implements sorted printing for the built-in list class"""

    def printed_sorted(self):
        """Prints a list in sorted ascending order"""
        print (sorted(self))
