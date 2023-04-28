from movement import Movement
import pygame


class Cone(Movement):
    # noinspection PyMissingConstructor
    def __init__(self, pos, image, level, xvel, yvel):
        self.x, self.y = pos[0], pos[1]  # (x, y)
        self.xvel, self.yvel = xvel, yvel
        self.gravity = 0.25
        self.level = level
        self.image = image  # type: pygame.Surface
        image.fill("white")
        self.rect = self.image.get_rect(topleft=pos)

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
        self.yvel += self.gravity

    def stop_x(self):
        self.xvel = 0

    def stop_y(self):
        self.yvel = 0

    def stop(self):
        pass

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def get_rect(self):
        return self.rect

    def update(self, tiles):
        self.move_x()
        self.move_y()
        self.accelerate()
        for tile in tiles:
            if tile.get_rect().colliderect(self.get_rect()):
                self.die()
                break

    def die(self):
        self.level.cones.remove(self)

