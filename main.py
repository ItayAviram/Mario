import pygame
import sys

from princess import Princess

pygame.init()
width, height = (600, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mario")
clock = pygame.time.Clock()

p = Princess((100, 100), pygame.Surface((10, 50)), 0)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(1)

        screen.fill("black")
        p.draw(screen)
        p.update()

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
