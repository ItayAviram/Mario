from character import Character
import pygame


class Mario(Character):
    def __init__(self, pos, image):
        self.x, self.y = pos[0], pos[1]
        self.image = image
