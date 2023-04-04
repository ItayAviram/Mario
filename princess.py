from character import Character
import pygame


class Princess(Character):
    def __init__(self, pos, image, leaves, throws=3, health=3):
        self.x, self.y = pos[0], pos[1]
        self.image = image
        self.leaves = leaves
        self.throws = throws
        self.health = health

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

    def update_health(self, val):
        self.health = val

    def update_leaves(self, val):
        self.leaves = val
