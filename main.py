import pygame
import sys

# from checkpoint import Checkpoint
# from mario import Mario
# from mushroom import mushroom
# from princess import Princess
# from enemy import Enemy
# from python_snake import python_snake
# from carnivorous_plant import Carnivorous_plant
# from button import button
# from acorn import acorn
# from banana_peel import banana_peel

from enemy import Enemy
from level import Level
from config import *

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mario")
clock = pygame.time.Clock()


# c = Checkpoint((150, 100), pygame.Surface((10, 80)), 0)
# m = mushroom((110, 100), pygame.Surface((10, 10)), 0)
# ma = Mario((200, 100), pygame.Surface((10, 50)), 0)
# py = python_snake((160, 100), pygame.Surface((10, 5)), 0)
# ca = carnivorous_plant((170, 100), pygame.Surface((20, 80)), 0)
# b = button((180, 100), pygame.Surface((15, 15)), 0)
# a = acorn((190, 100), pygame.Surface((5, 5)), 0)
# ba = banana_peel((200, 100), pygame.Surface((5, 5)), 0)


#e = Enemy((120, 120), (50, 50), enemy_image, 0)
level = Level(level_map, screen)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(1)

        level.draw()
        level.update()

        # c.draw(screen)
        # m.draw(screen)
        # ma.draw(screen)
        # py.draw(screen)
        # ca.draw(screen)
        # b.draw(screen)
        # a.draw(screen)
        # ba.draw(screen)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()

