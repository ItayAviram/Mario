import pygame
import sys

from princess import Princess
from enemy import Enemy

pygame.init()
width, height = (900, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mario")
clock = pygame.time.Clock()

p = Princess((100, 100), pygame.Surface((10, 50)), 0)

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
        pygame.display.update()

        p.draw(screen)
        p.update()

        e.draw(screen)
        e.update()

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()

