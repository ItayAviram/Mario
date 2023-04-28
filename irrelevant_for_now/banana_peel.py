from character import Character
import pygame


class banana_peel(Character):
    # noinspection PyMissingConstructor
    def __init__(self, pos, image, leaves=None):
        self.x, self.y = pos[0], pos[1]  # (x, y)
        self.image = image  # type: pygame.Surface
        image.fill("white")
        self.rect = self.image.get_rect(topleft=pos)
#double new 
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

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def speak(self, what_to_say):
        pass

