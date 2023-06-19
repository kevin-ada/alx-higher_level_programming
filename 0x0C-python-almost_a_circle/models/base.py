#!/usr/bin/python3
class Base:
    """Initializing a class name called base
     Attributes:
            __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0
    def __init__(self, id):
        if id is not None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects

