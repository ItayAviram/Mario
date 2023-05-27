import pygame
import random

width, height = (900, 600)
p_width = 40  # princess width and height
c_width, c_height = 20, 50  # checkpoint width and height
a_width, a_height = 20, 50  # carnivorous plant width and height
cone_width, cone_height = 20, 20

cone_x_vel = 10
cone_y_vel = -2


# generate level map: [["" for i in range(<width>)] for j in range(<height>)]
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

level_map = level_blocks[0]
tile_size = height / len(level_blocks[0])

block_width = len(level_blocks[0][0])
block_height = len(level_blocks[0])
block_pixel_width = block_width * tile_size  # in pixels
block_pixel_height = block_height * tile_size  # in pixels


def generate_random_level_map(l_width, l_height, chance_for_tile):
    m = []
    for i in range(l_height-1):
        row = ""
        for j in range(l_width):
            if random.randint(0,100) < chance_for_tile:
                row += "X"
            else:
                row += " "
        m.append(row)
    m.append("X" * l_width)
    print("[")
    for row in m:
        print("    \"" + row + "\",")
    print("]")
    return m


generate_random_level_map(30, 10, 20)

# images
background_image = pygame.image.load(r'images\bcimage.jpg')
background_image = pygame.transform.scale(background_image, (width, height))
enemy_image = pygame.image.load(r'images\enemies\enemy.png')  # type: pygame.Surface
tile_image = pygame.image.load(r"images\tile.png")
princess_image = pygame.image.load(r"images\princess.png")
p_height = p_width * (princess_image.get_height() / princess_image.get_width())  # keep the image width to height ratio
princess_image = pygame.transform.scale(princess_image, (p_width, p_height))
