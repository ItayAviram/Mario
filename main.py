import pygame
import sys

from checkpoint import checkpoint
from mario import Mario
from mushroom import mushroom
from princess import Princess
from enemy import Enemy
from python_snake import python_snake
from carnivorous_plant import carnivorous_plant
from button import button
from acorn import acorn
from banana_peel import banana_peel

from tile import tiles

pygame.init()
width, height = (900, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mario")
clock = pygame.time.Clock()

p = Princess((100, 100), pygame.Surface((10, 50)), 0)
# c = checkpoint((150, 100), pygame.Surface((10, 80)), 0)
# m = mushroom((110, 100), pygame.Surface((10, 10)), 0)
# ma = Mario((200, 100), pygame.Surface((10, 50)), 0)
# py = python_snake((160, 100), pygame.Surface((10, 5)), 0)
# ca = carnivorous_plant((170, 100), pygame.Surface((20, 80)), 0)
# b = button((180, 100), pygame.Surface((15, 15)), 0)
# a = acorn((190, 100), pygame.Surface((5, 5)), 0)
# ba = banana_peel((200, 100), pygame.Surface((5, 5)), 0)

enemyimage = pygame.image.load(r'images\enemy.png') # type: pygame.Surface

e = Enemy((120, 120), (50, 50), enemyimage, 0)


background_image = pygame.image.load(r'images\bcimage.jpg')
background_image = pygame.transform.scale(background_image, (width, height))


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(1)

        screen.blit(background_image, (0, 0))
        tiles.draw(screen)

        p.draw(screen)
        p.update()

        # c.draw(screen)
        # m.draw(screen)
        # ma.draw(screen)
        # py.draw(screen)
        # ca.draw(screen)
        # b.draw(screen)
        # a.draw(screen)
        # ba.draw(screen)

        e.draw(screen)
        e.update()

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()

