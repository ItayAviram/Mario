from config import *
from character import Character
from projectile import Projectile
import pygame


class Princess(Character):
    # noinspection PyMissingConstructor
    def __init__(self, pos, image, level, leaves=0, throws=3, health=3):
        self.x, self.y = pos[0], pos[1]  # (x, y)
        self.image = image  # type: pygame.Surface
        self.rect = self.image.get_rect(topleft=pos)
        self.level = level
        self.leaves = leaves
        self.throws = throws
        self.health = health
        # movement:
        #   constants:
        self.xvel = 8
        self.jump_height = 10
        self.gravity = 0.25
        #   changeables:
        self.x_speed_mul = self.xvel
        self.direction = 0  # direction of x
        self.yvel = 0

        self.pressed_space = False
        self.can_jump = False

    def set_x(self, val):
        self.x = val
        self.rect.left = val

    def set_y(self, val):
        self.y = val
        self.rect.top = val

    def move_x(self):
        self.set_x(self.x + self.direction * self.x_speed_mul)

    def move_y(self):
        self.set_y(self.y + self.yvel)

    def jump(self):
        self.yvel = self.jump_height * (-1)

    def stop_x(self):
        self.direction = 0

    def stop_y(self):
        self.yvel = 0

    def stop(self):
        self.stop_x()
        self.stop_y()

    def accelerate(self):
        self.yvel += gravity

    def die(self):
        self.level.die()
        # if self.health > 0:
        #     self.update_health(self.health - 1)

    def speak(self, what_to_say):
        pass

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def throw(self):
        if self.throws > 0:
            self.stop()
            self.level.projectiles.append(Projectile((self.x, self.y), cone_x_vel, cone_y_vel, cone_image, self.level, "cone")
                                )
            self.throws -= 1

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.direction = 1
        elif keys[pygame.K_a]:
            self.direction = -1
        else:
            self.direction = 0
        if keys[pygame.K_w] and self.can_jump:
            self.jump()

        if keys[pygame.K_SPACE]:
            if not self.pressed_space:
                self.throw()
            self.pressed_space = True
        else:
            self.pressed_space = False

    def update(self, tiles):
        self.get_input()
        self.move_x()
        self.check_collision_horizontal(tiles)  # x
        self.move_y()
        ver_col = self.check_collision_vertical(tiles)  # y
        if ver_col == "top":
            self.can_jump = True
        else:
            self.can_jump = False

        self.accelerate()
        if self.rect.top > height:
            self.die()

    def update_health(self, val):
        self.health = val

    def update_leaves(self, val):
        self.leaves = val

    def get_rect(self):
        return self.rect

    def check_collision_horizontal(self, tiles):
        for tile in tiles:
            col = tile.check_collision_horizontal(self)
            if col:  # col != None
                return col

    def check_collision_vertical(self, tiles):
        for tile in tiles:
            col = tile.check_collision_vertical(self)
            if col:  # col != None
                return col

    def set_rect_left(self, val):
        self.rect.left = val
        self.x = self.rect.left

    def set_rect_right(self, val):
        self.rect.right = val
        self.x = self.rect.left

    def set_rect_top(self, val):
        self.rect.top = val
        self.y = self.rect.top

    def set_rect_bottom(self,val):
        self.rect.bottom = val
        self.y = self.rect.top
