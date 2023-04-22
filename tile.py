import pygame
from character import Character
from config import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, image=None):
        super().__init__()
        self.pos = pos
        self.rect = pygame.Rect(*self.pos, size, size)
        if image:
            self.image = pygame.transform.scale(image, size)
        else:
            self.image = pygame.Surface((size, size))
            self.image.fill((160,82,45))

        self.collision_tolerance = 10

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
            if abs(self.rect.bottom - obj.rect.left) <= self.collision_tolerance:
                obj.stop_y()
                obj.set_rect_top(self.rect.bottom)
                return "bottom"


tile_image = pygame.image.load(r"images\tile.png")
tile_image = pygame.transform.scale(tile_image, (tile_size, tile_size))


tiles = pygame.sprite.Group()
for y, row in enumerate(level_map):
    for x, col in enumerate(row):
        if col == "X":
            tiles.add(Tile((x * tile_size, y * tile_size), tile_size))

