import pygame
from config import *
from tile import Tile
from princess import Princess
from checkpoint import Checkpoint


class Level:
    def __init__(self, level_map, surface):
        self.level_map = level_map
        self.display_surface = surface
        self.tiles = pygame.sprite.Group()
        self.enemies = []
        self.checkpoints = []
        self.tile_shift = 0
        self.shift_offset = tile_size * 3

        self.setup_level()

    def setup_level(self):
        for y, row in enumerate(self.level_map):
            for x, col in enumerate(row):
                pos = (x * tile_size, y * tile_size)
                if col == "X":
                    self.tiles.add(Tile(pos, tile_size))
                if col == "C":
                    self.checkpoints.append(Checkpoint(pos,pygame.Surface((c_width, c_height)),self))
                if col == "P":
                    self.princess = Princess((pos[0] - p_width, pos[1]-p_height),
                                             pygame.Surface((p_width, p_height)), 0)

    def draw(self):
        self.display_surface.blit(background_image, (0, 0))
        self.tiles.draw(self.display_surface)
        for enemy in self.enemies:
            enemy.draw(self.display_surface)
        for checkpoint in self.checkpoints:
            checkpoint.draw(self.display_surface)
        self.princess.draw(self.display_surface)

    def update(self):
        self.princess.update(self.tiles)
        self.scroll_x()
        for checkpoint in self.checkpoints:
            checkpoint.update(self.tiles)

    def scroll_x(self):
        princess_rect = self.princess.get_rect()

        if princess_rect.right >= (width - self.shift_offset) and self.princess.direction == 1:
            self.tile_shift = self.princess.xvel * (-1)
            self.princess.x_speed_mul = 0
            self.princess.set_rect_right(width - self.shift_offset)
        elif princess_rect.left <= self.shift_offset and self.princess.direction == -1:
            self.tile_shift = self.princess.xvel
            self.princess.x_speed_mul = 0
            self.princess.set_rect_left(self.shift_offset)
        else:
            self.princess.x_speed_mul = self.princess.xvel
            self.tile_shift = 0
        self.scroll_tiles_x()

    def scroll_tiles_x(self):
        for tile in self.tiles:
            tile.move_x(self.tile_shift)
