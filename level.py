import pygame
from config import *
from tile import Tile
from princess import Princess
from checkpoint import Checkpoint
import random


from carnivorous_plant import Carnivorous_plant
from enemy import Enemy

class Level:
    def __init__(self, blocks, surface):
        self.blocks = blocks
        self.display_surface = surface
        self.tiles = pygame.sprite.Group()
        self.enemies = []
        self.checkpoints = []
        self.carnivorous_plants = []
        self.cones = []

        self.world_pos = 0
        self.tile_shift = 0
        self.shift_offset = tile_size * 3
        self.blocks_num = 0

        self.princess = None
        self.create_block()

    def create_block(self, xoffset=0, yoffset=0):
        for y, row in enumerate(random.choice(level_blocks)):
            for x, col in enumerate(row):
                xpos = x * tile_size + xoffset
                ypos = y * tile_size + yoffset
                pos = (xpos, ypos)
                if col == "X":
                    self.tiles.add(Tile(pos, tile_size))
                if col == "C":
                    self.checkpoints.append(Checkpoint(pos, pygame.Surface((c_width, c_height)), self))
                if col == "A":
                    self.carnivorous_plants.append(Carnivorous_plant(pos, pygame.Surface((a_width, a_height)), self))
                if col == "P" and not self.princess:
                    self.princess = Princess((pos[0] - p_width, pos[1]-p_height),
                                             pygame.Surface((p_width, p_height)), self)

    def draw(self):
        self.display_surface.blit(background_image, (0, 0))
        self.tiles.draw(self.display_surface)

        self.draw_list(self.enemies, self.display_surface)
        self.draw_list(self.checkpoints, self.display_surface)
        self.draw_list(self.cones, self.display_surface)
        self.draw_list(self.carnivorous_plants, self.display_surface)

        self.princess.draw(self.display_surface)

    def update(self):
        self.princess.update(self.tiles)

        self.scroll_x()
        self.world_pos -= self.tile_shift
        self.check_block()

        self.update_list(self.checkpoints, self.tiles)
        self.update_list(self.carnivorous_plants, self.tiles)
        self.update_list(self.cones, self.tiles)

        for enemy in self.enemies:
            enemy.update()

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

    def check_block(self):
        if self.world_pos + width >= (self.blocks_num + 1) * block_pixel_width:
            self.blocks_num += 1
            self.add_block()

    def add_block(self):
        self.create_block(abs(self.world_pos - self.blocks_num * block_pixel_width))



    @staticmethod
    def draw_list(lst, surface):
        for obj in lst:
            obj.draw(surface)

    @staticmethod
    def update_list(lst, *args):
        for obj in lst:
            obj.update(*args)

    def create_enemy(self, pos):
        enemy = Enemy(pos, enemy_size, enemy_image, enemy_speed)
        self.enemies.append(enemy)
