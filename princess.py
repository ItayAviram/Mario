from character import Character
import pygame


gravity = 10


class Princess(Character):
    def __init__(self, pos, image, leaves, throws=3, health=3):
        self.x, self.y = pos[0], pos[1]  # (x, y)
        self.image = image  # type: pygame.Surface
        image.fill("white")
        self.rect = self.image.get_rect(topleft=pos)
        self.leaves = leaves
        self.throws = throws
        self.health = health
        # movement:
        #   constants:
        self.xvel = 8
        self.jump_height = 8
        self.gravity = 0.25
        #   changeables:
        self.direction = 0  # direction of x
        self.yvel = 0

    def move_x(self):
        self.x += self.direction * self.xvel

    def move_y(self):
        self.y += self.yvel

    def jump(self):
        self.yvel = self.jump_height * (-1)

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

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.direction = 1
        elif keys[pygame.K_a]:
            self.direction = -1
        else:
            self.direction = 0
        if keys[pygame.K_w]:
            self.jump()
        if keys[pygame.K_SPACE]:
            self.stop()

    def update(self):
        self.get_input()
        self.move_x()
        self.move_y()
        self.accelerate()

    def update_health(self, val):
        self.health = val

    def update_leaves(self, val):
        self.leaves = val
