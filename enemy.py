from character import Character
import pygame


class Enemy(Character):
    # noinspection PyMissingConstructor
    def __init__(self, pos: tuple, size: tuple, image: pygame.Surface, leaves: int, throws=3, health=3):
        self.x, self.y = pos[0], pos[1]  # (x, y)

        self.image = image
        self.image = pygame.transform.scale(image, size)
        self.rect = pygame.Rect(self.x, self.y, size[0], size[1])

        self.leaves = leaves
        self.throws = throws
        self.health = health
        # movement:
        #   constants:
        self.xvel = 2
        self.jump_height = 0
        self.gravity = 0.25
        #   changeables:
        self.direction = 0  # direction of x
        self.yvel = 0

    def move_x(self):
        self.x += self.direction * self.xvel

    def move_y(self):
        self.y += self.yvel

    def jump(self):
        pass
        # enemies can't jump

    def stop(self):
        self.yvel = 0
        self.direction = 0

    def accelerate(self):
        self.yvel += self.gravity

    def die(self):
        pass
        # if self.health > 0:
        #     self.update_health(self.health - 1)

    def speak(self, what_to_say):
        pass

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def update(self):
        self.move_x()
        self.move_y()
        self.accelerate()

    def update_health(self, val):
        self.health = val

    def update_leaves(self, val):
        self.leaves = val
