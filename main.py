import pygame
import sys
from level import Level
from config import *

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mario")
clock = pygame.time.Clock()

level = Level(level_blocks, screen)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(1)

        level.draw()
        level.update()

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()

