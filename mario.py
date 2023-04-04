from character import Character
import pygame


class Princess(Character):
    def __init__(self, pos, image, leaves, throws=3, health=3):
        self.x, self.y = pos[0], pos[1]
        self.image = image
