import pygame
import random

width, height = (1100, 600)

princess_width = 40  # princess width

cone_width = 40
cone_x_vel = 8
cone_y_vel = -4

stone_width = 40
stone_x_vel = -9
stone_y_vel = -4

gravity = 0.25

# **BLOCKS**
# X represents a tile
# O represents a coin
# P represents the princess
# M represents a mushroom
# C represents a checkpoint
# S represents a snake
# B represents a banana peal
# A represents a carnivorous plant


level_blocks = [
    [
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "                             X",
        "X                             ",
        "           XXX                ",
        "                              ",
        "        X    XX               ",
        "       XXX  X  X              ",
        "                   XXX        ",
        "   P                          ",
        "XXXXXXXXXXXXXXXXXXXXXXX   XXXX"
     ],
    [
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "                             X",
        "X         X                   ",
        "         XXX                  ",
        "          X                   ",
        "      XX                      ",
        "     XXXX                     ",
        "           XXXXX              ",
        "   P                          ",
        "XXXXXXXX   XXXXXXXXXXXXXXXXXXX"
     ],
    [
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "                             X",
        "X                             ",
        "                              ",
        "                              ",
        "      XX                      ",
        "     X                  X  X  ",
        "                       XX  XX ",
        "   P                  XXX  XXX",
        "XXXXXXXX   XXXXXXXXXXXXXX  XXX"
     ],
[
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "                             X",
        "X                             ",
        "                              ",
        "                   XX         ",
        "                  XXXX   XXX  ",
        "     XXXX                     ",
        "              X               ",
        "   P                          ",
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
     ],
[
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "                             X",
        "X                             ",
        "                    XXXXX     ",
        "                              ",
        "           XXX                ",
        "          XXXXX      X        ",
        "     XX             XXX       ",
        "   P                          ",
        "XXXXXXXXXXX XX XXXXXXXXXXXXXXX"
     ],
[
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        "                             X",
        "X                             ",
        "                              ",
        "                              ",
        "      XX                      ",
        "     XXXX                     ",
        "             XXXXX            ",
        "   P                          ",
        "XXXXXXXX   XXXXXXXXXXXXXXXXXXX"
     ],
]
# tiles
tile_size = height / len(level_blocks[0])

# enemies
b_width = tile_size * 0.8
m_width = tile_size * 0.8
snake_width = tile_size * 0.8

# block
block_width = len(level_blocks[0][0])  # in tiles
block_height = len(level_blocks[0])  # in tiles
block_pixel_width = block_width * tile_size  # in pixels
block_pixel_height = block_height * tile_size  # in pixels

# collision
collision_tolerance = 20

# images
tile_image = pygame.image.load(r"images\tile.png")

princess_image = pygame.image.load(r"images\princess.png")
p_height = princess_width * (princess_image.get_height() / princess_image.get_width())  # keep the image width to height ratio
princess_image = pygame.transform.scale(princess_image, (princess_width, p_height))

banana_image = pygame.image.load(r"images\enemies\banana_peel.png")
b_height = b_width * (banana_image.get_height() / banana_image.get_width())
banana_image = pygame.transform.scale(banana_image, (b_width, b_height))

mushroom_image = pygame.image.load(r"images\enemies\mushroom.png")
m_height = m_width * (mushroom_image.get_height() / mushroom_image.get_width())
mushroom_image = pygame.transform.scale(mushroom_image, (m_width, m_height))

snake_image = pygame.image.load(r"images\enemies\snake.png")
snake_height = snake_width * (snake_image.get_height() / snake_image.get_width())
snake_image = pygame.transform.scale(snake_image, (snake_width, snake_height))

cone_image = pygame.image.load(r"images\pinecone.png")
cone_height = cone_width * (cone_image.get_height() / cone_image.get_width())
cone_image = pygame.transform.scale(cone_image, (cone_width, cone_height))

stone_image = pygame.image.load(r"images\stone.png")
stone_height = stone_width * (stone_image.get_height() / stone_image.get_width())
stone_image = pygame.transform.scale(stone_image, (stone_width, stone_height))

# text
pygame.font.init()
font = pygame.font.SysFont("Arial", 72)
death_message = font.render("Game Over!", True, "white")
font = pygame.font.SysFont("Arial", 36)
play_again = font.render("Press 'r' to play again.", True, "white")


# def generate_random_level_map(l_width, l_height, chance_for_tile):
#     m = []
#     for i in range(l_height-1):
#         row = ""
#         for j in range(l_width):
#             if random.randint(0,100) < chance_for_tile:
#                 row += "X"
#             else:
#                 row += " "
#         m.append(row)
#     m.append("X" * l_width)
#     print("[")
#     for row in m:
#         print("    \"" + row + "\",")
#     print("]")
#     return m


# generate_random_level_map(30, 10, 20)