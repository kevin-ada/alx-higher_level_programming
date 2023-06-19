#!/usr/bin/python3
"""Importing module base that will be inherited"""
from base import Base

class Rectangle(Base):
    """ Creating the Class Rectangle that inherits from Base
    Methods:
            __init()__
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """

        :return:width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter function for width.
        Args:
         value (int): value to be set.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        getter function for height
        Returns: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
         setter function for height
         Args:
            value (int): value to be set.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter function for x
        Args:
            :returns (int): value to be set
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter function for height
        Args:
            value (int): value to be set.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value <= 0 :
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter function for x
        Args:
            :returns (int): value to be set
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter function for height
        Args:
            value (int): value to be set.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """
              prints to stdout the Rectangle instance with '#'
              """
        rectangle = ""
        print_symbol = "#"

        #        for i in range(self.__height - 1):
        #            rectangle += print_symbol * self.__width + "\n"
        #        rectangle += print_symbol * self.__width
        #        print("{}".format(rectangle))

        print("\n" * self.y, end="")

        for i in range(self.height):
            rectangle += (" " * self.x) + (print_symbol * self.width) + "\n"
        print(rectangle, end="")

        def __str__(self):
            """
            returns a string format of the rectangle
            """
            return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                    self.__x, self.__y,
                                                    self.__width, self.__height)

        def update(self, *args, **kwargs):
            """
            assigns key and value argument to attributes
            kwargs is skipped if args is not empty
            Args:
                *args -  variable number of no-keyword args
                **kwargs - variable number of keyword args
            """
            if len(args) == 0:
                for key, val in kwargs.items():
                    self.__setattr__(key, val)
                return

            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError as e:
                print(e)

            def to_dictionary(self):
                """
        	returns the dictionary repr of the rectangle
                """
                return {'x': getattr(self, "x"), 'y': getattr(self, "y"),
                        'id': getattr(self, "id"), 'height': getattr(self, "height"),
                        'width': getattr(self, "width")}




