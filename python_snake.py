from character import Character
from config import *
import pygame


class Snake(Character):
    # noinspection PyMissingConstructor
    def __init__(self, pos, image, level):
        self.x, self.y = pos[0], pos[1]  # (x, y)
        self.image = image  # type: pygame.Surface
        self.rect = self.image.get_rect(topleft=pos)
        self.level = level

        self.direction = -1  # left
        self.yvel = 0
        self.xvel = 4

    def set_x(self, val):
        self.x = val
        self.set_rect_left(val)

    def set_y(self, val):
        self.y = val
        self.set_rect_top(val)

    def move_y(self):
        self.set_y(self.y + self.yvel)

    def move_x(self):
        self.set_x(self.x + self.xvel * self.direction)

    def stop(self):
        self.stop_x()
        self.stop_y()

    def stop_y(self):
        self.yvel = 0

    def accelerate(self):
        self.yvel += gravity

    def draw(self, surface):
        if self.direction == -1:
            surface.blit(self.image, (self.x, self.y))
        elif self.direction == 1:
            surface.blit(pygame.transform.flip(self.image, True, False), (self.x, self.y))

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

    def check_collision_horizontal(self, tiles):
        for tile in tiles:
            col = tile.check_collision_horizontal(self)
            if col:  # col != None
                return col

    def check_collision_princess(self, princess):
        princess_rect = princess.get_rect()
        if self.rect.colliderect(princess_rect):
            if abs(self.rect.top - princess_rect.bottom) <= collision_tolerance:
                return "top"
            return "not top"
        return -1

    def update(self, tiles, princess):
        self.move_y()
        ver_col = self.check_collision_vertical(tiles)
        self.move_x()
        hor_col = self.check_collision_horizontal(tiles)
        if hor_col:
            self.direction *= -1
        self.accelerate()
        col = self.check_collision_princess(princess)
        if col == "top":
            self.die()
            princess.stop()
        elif col != -1:
            princess.die()

    def speak(self, what_to_say):
        pass

    def die(self):
        self.level.enemies.remove(self)

    def stop_x(self):
        pass

    def jump(self):
        pass
