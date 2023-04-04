from abc import ABC, abstractmethod


class Character(ABC):
    """
    this class represents the characters in the game
    """
    @abstractmethod
    def __init__(self, pos, image, leaves, throws=3, health=3):
        """
        :param tuple pos: character position (x, y)
        :param image: image of the character
        :param int leaves: ranges 0 - 4, is a counter for the leaves the character picked up
        :param throws: ranges 0 - 3, is a counter for how many throws does the character have
        :param health: ranges 1 - 3, is the number of hearts the character has until it dies
        (you can't have a character with 0 health)
        """
        pass

    @abstractmethod
    def left(self):
        pass

    @abstractmethod
    def right(self):
        pass

    @abstractmethod
    def jump(self):
        pass

    @abstractmethod
    def stop(self):
        """
        this method should be called when the character throws a projectile
        :return:
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


if __name__ == "__main__":
    print(Character.__init__.__doc__)