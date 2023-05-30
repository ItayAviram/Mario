from character import Character
from config import *
import pygame


class Snake(Character):
    # noinspection PyMissingConstructor
    def __init__(self, pos, image):
        self.x, self.y = pos[0], pos[1]  # (x, y)
        self.image = image  # type: pygame.Surface
        self.rect = self.image.get_rect(topleft=pos)

        self.yvel = 0

    def set_x(self, val):
        self.x = val
        self.set_rect_left(val)

    def set_y(self, val):
        self.y = val
        self.set_rect_top(val)

    def move_y(self):
        self.set_y(self.y + self.yvel)

    def stop(self):
        self.stop_x()
        self.stop_y()

    def stop_y(self):
        self.yvel = 0

    def accelerate(self):
        self.yvel += gravity

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def set_rect_bottom(self, val):
        self.rect.bottom = val
        self.y = self.rect.top

    def set_rect_left(self, val):
        self.rect.left = val
        self.x = self.rect.left

    def set_rect_right(self, val):
        self.rect.right = val
        self.x = self.rect.left

    def set_rect_top(self, val):
        self.rect.top = val
        self.y = self.rect.top

    def get_rect(self):
        return self.rect

    def check_collision_vertical(self, tiles):
        for tile in tiles:
            col = tile.check_collision_vertical(self)
            if col:  # col != None
                return col

    def update(self, tiles, princess):
        self.move_y()
        self.check_collision_vertical(tiles)
        self.accelerate()
        if self.rect.colliderect(princess.get_rect()):
            princess.die()

    def speak(self, what_to_say):
        pass

    def die(self):
        pass

    def stop_x(self):
        pass

    def move_x(self):
        pass

    def jump(self):
        pass
