from character import Character
import pygame


class Mario(Character):
    def __init__(self, pos, image, leaves=None):
        self.x, self.y = pos[0], pos[1]
        self.image = image

    def move_x(self):
        pass

    def move_y(self):
        pass

    def jump(self):
        pass

    def stop(self):
        pass

    def accelerate(self):
        pass

    def die(self):
        pass

    def draw(self):
        pass
    
    def speak(self, what_to_say):
        pass

