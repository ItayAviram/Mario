import pygame
from character import Character


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, image=None):
        super().__init__()
        self.pos = pos
        self.rect = pygame.Rect(*self.pos, size, size)
        if image:
            self.image = pygame.transform.scale(image, size)
        else:
            self.image = pygame.Surface(self.pos, size)
            self.image.fill((160,82,45))

        print("image", self.image)
        print("rect", self.rect)
        # self.image.fill("white")

    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, self.pos)

    def check_collision(self, obj: Character):
        collision_tolerance = 5
        obj_rect = obj.get_rect()
        if abs(self.rect.right - obj_rect.left) <= collision_tolerance:
            return "right"
        if abs(self.rect.left - obj_rect.right) <= collision_tolerance:
            return "left"
        if abs(self.rect.top - obj_rect.bottom) <= collision_tolerance:
            return "top"
        if abs(self.rect.bottom - obj_rect.left) <= collision_tolerance:
            return "bottom"


tile_size = 10
tile_image = pygame.image.load(r"images\tile.png")
pygame.transform.scale(tile_image, (tile_size, tile_size))

level_map = [['', '', '', '', '', '', '', '', '', ''],
             ['', 'X', '', '', '', '', '', '', '', ''],
             ['', '', 'X', '', '', '', '', '', '', ''],
             ['', '', '', 'X', '', '', '', '', '', ''],
             ['', '', '', '', 'X', '', '', '', '', ''],
             ['', '', '', '', '', 'X', '', '', '', ''],
             ['', '', '', '', '', '', 'X', '', '', ''],
             ['', '', '', '', '', '', '', 'X', '', ''],
             ['', '', '', '', '', '', '', '', '', ''],
             ['', '', '', '', '', '', '', '', '', '']
             ]

tiles = pygame.sprite.Group()
for x, row in enumerate(level_map):
    for y, col in enumerate(row):
        if col == "X":
            tiles.add(Tile((x * tile_size, y * tile_size), tile_size))

