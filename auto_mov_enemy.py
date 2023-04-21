from movement import AutoMovEnemy
import math
import pygame


class Enemy(AutoMovEnemy):
    def __init__(self, pos, xvel, yvel, yacc=0):
        super().__init__(pos, xvel, yvel, yacc)
        self.image = pygame.Surface((50, 50))
        self.image.fill("red")
        self.rect = self.image.get_rect(topleft=pos)

    def move_towards(self, target_pos):
        # calculate distance and angle to target
        dx = target_pos[0] - self.rect.centerx
        dy = target_pos[1] - self.rect.centery
        distance = math.hypot(dx, dy)
        angle = math.atan2(dy, dx)

        # move towards target
        self.rect.x += math.cos(angle) * self.xvel
        self.rect.y += math.sin(angle) * self.yvel

    def move_x(self):
        # not needed for automatic movement
        pass

    def move_y(self):
        # not needed for automatic movement
        pass

    def jump(self):
        # not needed for automatic movement
        pass

    def stop(self):
        # not needed for automatic movement
        pass

    def accelerate(self):
        # not needed for automatic movement
        pass

    def update(self, target_pos):
        self.move_towards(target_pos)

    def draw(self, surface):
        surface.blit(self.image, self.rect)