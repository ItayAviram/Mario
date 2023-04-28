import pygame
import random

width, height = (900, 600)
p_width, p_height = 20, 50  # princess width and height
c_width, c_height = 20, 50  # checkpoint width and height

# generate level map: [["" for i in range(<width>)] for j in range(<height>)]
# X represents a tile
# O represents a coin
# P represents the princess
# M represents a mushroom
# C represents a checkpoint
# S represents a snake
# B represents a banana peal

level_map = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    "X    X      X          X   X  ",
    "X    X    X X    XX X      X  ",
    "    X  XX   X  X              ",
    "   X                 X   X    ",
    " X  X  C   XX     X     X X    ",
    " XX  X      XXX XXX           ",
    "                X      X X   X",
    " X     X     X  X    X    X   ",
    "   P   X X X   X        X   X ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
]


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

tile_size = height / len(level_map)

# images
background_image = pygame.image.load(r'images\bcimage.jpg')
background_image = pygame.transform.scale(background_image, (width, height))
enemy_image = pygame.image.load(r'images\enemy.png') # type: pygame.Surface