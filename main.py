import pygame
from pygame import Color

from consts import *
from ball import Ball
from border import Border


def main():
    pygame.init()
    sc = pygame.display.set_mode(SIZE)

    Border(5, 5, W - 5, 0)
    Border(5, H - 5, W - 5, 0)
    Border(5, 5, 5, H - 5)
    Border(W - 5, 5, W - 5, H - 5)

    for i in range(10):
        Ball(20, 100, 100)

    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        sc.fill(Color('white'))

        all_sprites.draw(sc)
        all_sprites.update()

        clock.tick(FPS)
        pygame.display.flip()


if __name__ == '__main__':
    main()