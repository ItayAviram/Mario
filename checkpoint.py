from character import Character
import pygame


class Checkpoint(Character):
    # noinspection PyMissingConstructor
    def __init__(self, pos, image,level):
        self.x, self.y = pos[0], pos[1]  # (x, y)
        self.image = image  # type: pygame.Surface
        image.fill("white")
        self.rect = self.image.get_rect(topleft=pos)
        self.level=level

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

    def get_rect(self):
        pass

    def set_rect_left(self):
        pass

    def stop_x(self):
        pass

    def stop_y(self):
        pass

    def set_rect_right(self):
        pass

    def set_rect_top(self):
        pass

    def set_rect_bottom(self):
        pass

    def update(self, tiles):
        self.x+=self.level.tile_shift
