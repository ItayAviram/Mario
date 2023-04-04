from abc import ABC, abstractmethod


class Movement(ABC):
    @abstractmethod
    def __init__(self, pos, xvel, yvel, yacc=0):
        """
        :param pos: position on screen (x, y)
        :param xvel: velocity of object on the x axis
        :param yvel: velocity of object on the y axis
        :param yacc: acceleration of object on the *y axis* (0 by default)
        """
        pass

    @abstractmethod
    def move_x(self):
        """
        changes the x position according to the x velocity
        :return: x pos: float
        """
        pass

    @abstractmethod
    def move_y(self):
        """
        changes the y position according to the y velocity
        :return: y pos: float
        """
        pass

    @abstractmethod
    def jump(self):
        """
        sets speed to negative (up)
        sets acceleration to down (positive)
        :return: None
        """
        pass

    @abstractmethod
    def stop(self):
        """
        this method should be called when the character throws a projectile
        :return: None
        """
        pass

    @abstractmethod
    def accelerate(self):
        """
        changes the y velocity according to the acceleration
        :return: y vel: float
        """
        pass
