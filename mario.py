from character import Character
import pygame


class Mario(Character):
    def __init__(self, pos, image):
        self.x, self.y = pos[0], pos[1]
        self.image = image

    def left(self):
        pass

    def right(self):
        pass

    def jump(self):
        pass

    def stop(self):
        pass

    def die(self):
        pass

    def speak(self, what_to_say):
        pass

