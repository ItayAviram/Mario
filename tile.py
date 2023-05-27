from character import Character
from config import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, image=None):
        super().__init__()
        self.pos = pos
        self.rect = pygame.Rect(*self.pos, size, size)
        if image:  # image
            self.image = pygame.transform.scale(image, (size, size))
        else:  # rectangle
            self.image = pygame.Surface((size, size))
            self.image.fill((255,255,255))  # outline
            self.image.fill((0, 0, 0), self.image.get_rect().inflate(-3, -3))

        self.collision_tolerance = 20

    def get_rect(self):
        return self.rect


    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, self.pos)

    def check_collision_horizontal(self, obj: Character):
        if self.rect.colliderect(obj.rect):
            # at this point there is a collision but we want to know where it occurs
            if abs(self.rect.right - obj.rect.left) <= self.collision_tolerance:
                obj.stop_x()
                obj.set_rect_left(self.rect.right)
                return "right"
            if abs(self.rect.left - obj.rect.right) <= self.collision_tolerance:
                obj.stop_x()
                obj.set_rect_right(self.rect.left)
                return "left"

    def check_collision_vertical(self, obj: Character):
        if self.rect.colliderect(obj.rect):
            # at this point there is a collision but we want to know where it occurs
            if abs(self.rect.top - obj.rect.bottom) <= self.collision_tolerance:
                obj.stop_y()
                obj.set_rect_bottom(self.rect.top)
                return "top"
            if abs(self.rect.bottom - obj.rect.top) <= self.collision_tolerance:
                obj.stop_y()
                obj.set_rect_top(self.rect.bottom)
                return "bottom"

    def move_x(self, relative_dest):
        self.pos = (self.pos[0] + relative_dest, self.pos[1])
        self.rect.left = self.pos[0]


tile_image = pygame.image.load(r"images\tile.png")
tile_image = pygame.transform.scale(tile_image, (tile_size, tile_size))



