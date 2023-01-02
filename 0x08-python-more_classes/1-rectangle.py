#!/usr/bin/python3
# 1-rectangle.py
"""Defines a rectangle class"""


class Rectangle:
    """Represents a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializze a new rectangle.

        Args:
            width(int): width of new rectangle.
            height(int): height of new rectangle.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set height of rectangle"""
        return self.__height

    @height.setter
    def height(self,value):
        """ set height of rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
