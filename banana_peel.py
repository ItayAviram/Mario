from character import Character
import pygame


class BananaPeel(Character):
    # noinspection PyMissingConstructor
    def __init__(self, pos, image, leaves=None):
        self.x, self.y = pos[0], pos[1]  # (x, y)
        self.image = image  # type: pygame.Surface
        image.fill("white")
        self.rect = self.image.get_rect(topleft=pos)

    def move_x(self):
        pass

    def move_y(self):
        pass

    def jump(self):
        pass

    def stop(self):
        self.stop_x()
        self.stop_y()

    def stop_x(self):
        pass

    def stop_y(self):
        pass

    def accelerate(self):
        pass

    def die(self):
        pass

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def speak(self, what_to_say):
        pass

    def set_rect_bottom(self, val):
        self.rect.bottom = val

    def set_rect_left(self, val):
        self.rect.left = val

    def set_rect_right(self, val):
        self.rect.right = val

    def set_rect_top(self, val):
        self.rect.top = val

