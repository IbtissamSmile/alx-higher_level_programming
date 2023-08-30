#!/usr/bin/python3
'''
square class defination
'''


class Square:
    '''Square class declaratiion'''

    def __init__(self, size=0, position=(0, 0)):
        '''class initialization

        Args:
            size:size of the square
            position:coordinates
        '''
        self.__size = size
        self.__position = position

    @property
    def size(self):
        '''Retrives size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Sets size
        Args:
            value:value to be manipulated
        Raises:
            TypeError: if the value is not an integer.
            ValueError: If value is less than 0.
        '''
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        '''Retrives position'''
        return self.__position

    @position.setter
    def position(self, value):
        '''Sets position
         Args:
             value:value to be manipulated
        Raises:
            TypeError: if the value is not a tuple.
        '''
        if isinstance(value, tuple) is not True:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        '''Calculates area'''
        return self.__size ** 2

    def my_print(self):
        '''Square representaion module'''
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("\n")
        if self.__size == 0:
            print("")
