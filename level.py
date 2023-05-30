import pygame
from config import *
from tile import Tile
from princess import Princess
from checkpoint import Checkpoint
from banana_peel import BananaPeel
from mushroom import Mushroom
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
        self.projectiles = []

        self.world_pos = 0
        self.tile_shift = 0
        self.shift_offset = tile_size * 5
        self.blocks_num = 0

        self.princess = None
        self.create_block()

        self.dead = None

    def create_block(self, xoffset=0, yoffset=0):
        block = random.choice(level_blocks)
        enemy_num = self.blocks_num
        cols = []
        while enemy_num > 0:
            row = random.randint(0, len(block) - 1)
            col = random.randint(0, len(block[0]) - 1)
            # print(f"row {row}, col {col}, block[row][col] {repr(block[row][col])}")
            if block[row][col] == " " and col not in cols:
                cols.append(col)
                choice = random.choice(["M", "B"])
                xpos = col * tile_size + xoffset
                ypos = row * tile_size + yoffset
                pos = xpos, ypos
                print(f"{choice} at {pos}")
                if choice == "S":
                    pass
                    # self.enemies.append(Snake(pos, snake_image))
                if choice == "B":
                    self.enemies.append(BananaPeel(pos, banana_image))
                if choice == "M":
                    self.enemies.append(Mushroom(pos, mushroom_image, self))
                enemy_num -= 1
        for y, row in enumerate(block):
            for x, col in enumerate(row):
                xpos = x * tile_size + xoffset
                ypos = y * tile_size + yoffset
                pos = (xpos, ypos)
                if col == "X":
                    self.tiles.add(Tile(pos, tile_size, tile_image))
                if col == "C":
                    self.checkpoints.append(Checkpoint(pos, pygame.Surface((cone_width, cone_height)), self))
                if col == "A":
                    self.carnivorous_plants.append(Carnivorous_plant(pos, pygame.Surface((a_width, a_height)), self))
                if col == "P" and not self.princess:
                    self.princess = Princess((pos[0] - princess_width, pos[1] - p_height),
                                             princess_image, self)

    def draw(self):
        self.display_surface.fill((96, 150, 255))  # bg
        self.tiles.draw(self.display_surface)

        self.draw_list(self.enemies, self.display_surface)
        self.draw_list(self.checkpoints, self.display_surface)
        self.draw_list(self.projectiles, self.display_surface)
        self.draw_list(self.carnivorous_plants, self.display_surface)

        self.princess.draw(self.display_surface)
        if self.dead:
            x = width // 2 - death_message.get_width() // 2
            y = height // 2 - death_message.get_height() // 2
            self.display_surface.blit(death_message, (x, y))

    def update(self):
        if self.dead:
            return
        self.princess.update(self.tiles)

        self.scroll_x()
        self.world_pos -= self.tile_shift
        self.check_block()

        self.update_list(self.checkpoints, self.tiles)
        self.update_list(self.carnivorous_plants, self.tiles)
        self.update_list(self.projectiles, self.tiles, self.enemies, self.princess)

        for enemy in self.enemies:
            if enemy.get_rect().right < 0:
                self.enemies.remove(enemy)
        self.update_list(self.enemies, self.tiles, self.princess)

    def scroll_x(self):
        princess_rect = self.princess.get_rect()

        if princess_rect.right >= (width - self.shift_offset) and self.princess.direction == 1:  # check right
            self.tile_shift = self.princess.xvel * (-1)
            self.princess.x_speed_mul = 0
            self.princess.set_rect_right(width - self.shift_offset)
        elif self.world_pos == 0 and princess_rect.left <= 0 and self.princess.direction == -1:  # start position
            self.tile_shift = 0
            self.princess.x_speed_mul = 0
            self.princess.set_rect_left(0)
        elif princess_rect.left <= self.shift_offset and self.princess.direction == -1 and self.world_pos > 0:  # check left
            self.tile_shift = self.princess.xvel
            self.princess.x_speed_mul = 0
            self.princess.set_rect_left(self.shift_offset)
        else:
            self.princess.x_speed_mul = self.princess.xvel
            self.tile_shift = 0
        self.scroll_world()

    def scroll_world(self):
        for tile in self.tiles:
            tile.move_x(self.tile_shift)
        for enemy in self.enemies:
            enemy.set_x(enemy.x + self.tile_shift)

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

    def run(self):
        self.draw()
        self.update()
        if self.dead:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                self.__init__(self.blocks, self.display_surface)

    def die(self):
        self.dead = True

    def undie(self):
        self.dead = False
