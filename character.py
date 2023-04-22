from abc import ABC, abstractmethod
from movement import Movement
import pygame


class Character(Movement):
    # Character is abstract because it inherits from Movement which is also abstract
    """
    This is an abstract class that represents the characters in the game
    """

    # noinspection PyMissingConstructor
    @abstractmethod
    def __init__(self, pos, image, leaves, throws=3, health=3):
        """
        :param tuple pos: character position (x, y)
        :param pygame.Surface image: image of the character
        :param int leaves: ranges 0 - 4, is a counter for the leaves the character picked up
        :param int throws: ranges 0 - 3, is a counter for how many throws does the character have
        :param int health: ranges 1 - 3, is the number of hearts the character has until it dies
        (health != 0)
        """
        pass

    @abstractmethod
    def die(self):
        pass

    @abstractmethod
    def speak(self, what_to_say):
        """
        Creates a speech bubble with given text

        :param str what_to_say: the content of the speech bubble
        """
        pass

    @abstractmethod
    def draw(self, surface):
        """
        draw the image on the screen.

        :param pygame.Surface surface: the screen
        :return: None
        """

    @abstractmethod
    def get_rect(self):
        """
        this method returns the character's rect in the form of pygame.Surface
        (used for collisions)
        :return: self.rect
        """
        pass


if __name__ == "__main__":
    print(Character.__mro__)
