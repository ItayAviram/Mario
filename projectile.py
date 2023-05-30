from config import *
from movement import Movement
import pygame
from banana_peel import BananaPeel


class Projectile(Movement):
    # noinspection PyMissingConstructor
    def __init__(self, pos, xvel, yvel, image, level, type):
        self.x, self.y = pos[0], pos[1]  # (x, y)
        self.xvel = xvel
        self.yvel = yvel
        self.level = level
        self.image = image  # type: pygame.Surface
        self.rect = self.image.get_rect(topleft=pos)
        self.type = type  # "cone" / "stone"
        if not (self.type == "cone" or self.type == "stone"):
            raise TypeError("Projectile type must be 'cone' or 'stone'")

    def set_x(self, val):
        self.x = val
        self.rect.left = val

    def set_y(self, val):
        self.y = val
        self.rect.top = val

    def move_x(self):
        self.x += self.xvel
        self.rect.left = self.x

    def move_y(self):
        self.y += self.yvel
        self.rect.top = self.y

    def jump(self):
        # can't jump
        pass

    def accelerate(self):
        self.yvel += gravity

    def stop_x(self):
        self.xvel = 0

    def stop_y(self):
        self.yvel = 0

    def stop(self):
        self.stop_x()
        self.stop_y()

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def get_rect(self):
        return self.rect

    def update(self, tiles, enemies, princess):
        self.move_x()
        self.move_y()
        self.accelerate()
        for tile in tiles:
            if self.is_colliding_with(tile):
                self.die()
                break
        if self.type == "cone":
            for enemy in enemies:
                if self.is_colliding_with(enemy):
                    self.die()
                    if not isinstance(enemy, BananaPeel):
                        enemy.die()
                    break
        elif self.type == "stone":
            if self.is_colliding_with(princess):
                self.die()
                princess.die()

    def die(self):
        self.level.projectiles.remove(self)

    def is_colliding_with(self, obj):
        return self.rect.colliderect(obj.get_rect())
