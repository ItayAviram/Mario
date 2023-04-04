from abc import ABC, abstractmethod
from movement import Movement
import pygame


class Character(Movement, ABC):
    """
    this class represents the characters in the game
    """
    @abstractmethod
    def __init__(self, pos, image, leaves, throws=3, health=3):
        """
        :param tuple pos: character position (x, y)
        :param pygame.Surface image: image of the character
        :param int leaves: ranges 0 - 4, is a counter for the leaves the character picked up
        :param int throws: ranges 0 - 3, is a counter for how many throws does the character have
        :param int health: ranges 1 - 3, is the number of hearts the character has until it dies
        (you can't have a character with 0 health)
        """
        pass

    @abstractmethod
    def die(self):
        pass

    @abstractmethod
    def speak(self, what_to_say):
        """
        :param str what_to_say: the content of what the character is saying
        """
        pass

    @abstractmethod
    def draw(self, surface):
        """
        draw the image on the screen.

        :param pygame.Surface surface: the screen
        :return: None
        """


if __name__ == "__main__":
    print(Character.__mro__)