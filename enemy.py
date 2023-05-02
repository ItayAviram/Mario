from character import Character
import pygame
import pygame


class Enemy(pygame.sprite.Sprite):

    def __init__(self, pos, size, image, speed):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed
        self.direction = 1
        self.gravity = 0.5
        self.velocity = pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, self.gravity)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def get_rect(self):
        return self.rect

    def set_rect_top(self, value):
        self.rect.top = value

    def set_rect_bottom(self, value):
        self.rect.bottom = value

    def set_rect_left(self, value):
        self.rect.left = value

    def set_rect_right(self, value):
        self.rect.right = value

    def move_x(self):
        self.rect.x += self.speed * self.direction

    def move_y(self):
        self.velocity += self.acceleration
        self.rect.y += self.velocity.y

    def jump(self):
        self.velocity.y = -10

    def stop_x(self):
        self.speed = 0

    def stop_y(self):
        self.velocity.y = 0

    def stop(self):
        self.stop_x()
        self.stop_y()

    def accelerate(self, value):
        self.acceleration.x += value

    def die(self):
        self.kill()

    def speak(self):
        print("Hello, I am an enemy.")

    def update(self):
        if abs(self.rect.centerx - player.rect.centerx) > 200:
            self.move_x = 2  # set movement speed
            self.rect.x += self.move_x
            self.check_platform_collision()  # check for collisions with the platform
        else:
            self.move_x = 0  # stop moving