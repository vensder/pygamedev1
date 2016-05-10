#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

WIDTH = 800
HEIGHT = 600
DISPLAY_MODE = (WIDTH, HEIGHT)
KEY_WIDTH = (WIDTH // 160) * 10
KEY_HEIGHT = KEY_WIDTH
PADDING = WIDTH // 200
LINE_WIDTH = 1
FPS = 10
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
WHITE = (255, 255, 255)
ROW1 = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '\\', '<-']

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()
window = pygame.display.set_mode(DISPLAY_MODE)
pygame.display.set_caption("Keyboard")

FONT = pygame.font.SysFont("monospace", KEY_HEIGHT // 2, bold=True)
for i in range(0, 10):
    SURFASEFONT = FONT.render(str(i), True, BLACK, GRAY)
    SURFACER = SURFASEFONT.get_rect()
    SURFACER.center = (KEY_WIDTH * i, KEY_HEIGHT * 1)
window.fill(WHITE)


for i in range(1, 16):
    pygame.draw.rect(
        window,
        BLACK,
        (KEY_WIDTH * i - KEY_WIDTH // 2,
            HEIGHT - KEY_HEIGHT * 6,
            KEY_WIDTH - PADDING,
            KEY_HEIGHT - PADDING),
        LINE_WIDTH)
    symbol = FONT.render(ROW1[i - 1], True, BLACK, GRAY)
    symbol_rect = symbol.get_rect()
    symbol_rect.center = ((KEY_WIDTH * i - KEY_WIDTH // 2) + KEY_WIDTH // 2,
                          (HEIGHT - KEY_HEIGHT * 6) + KEY_HEIGHT // 2)
    window.blit(symbol, symbol_rect)


for i in range(1, 13):
    pygame.draw.rect(
        window,
        BLACK,
        (KEY_WIDTH * i + KEY_WIDTH,
            HEIGHT - KEY_HEIGHT * 5,
            KEY_WIDTH - PADDING,
            KEY_HEIGHT - PADDING),
        LINE_WIDTH)

for i in range(1, 12):
    pygame.draw.rect(
        window,
        BLACK,
        (KEY_WIDTH * i + KEY_WIDTH + KEY_WIDTH // 2,
            HEIGHT - KEY_HEIGHT * 4,
            KEY_WIDTH - PADDING,
            KEY_HEIGHT - PADDING),
        LINE_WIDTH)

for i in range(1, 11):
    pygame.draw.rect(
        window,
        BLACK,
        (KEY_WIDTH * i + KEY_WIDTH * 2,
            HEIGHT - KEY_HEIGHT * 3,
            KEY_WIDTH - PADDING,
            KEY_HEIGHT - PADDING),
        LINE_WIDTH)

pygame.draw.rect(
    window,
    BLACK,
    (KEY_WIDTH * 4 + KEY_WIDTH // 2,
        HEIGHT - KEY_HEIGHT * 2,
        KEY_WIDTH * 6 - PADDING,
        KEY_HEIGHT - PADDING),
    LINE_WIDTH)


window.blit(SURFASEFONT, SURFACER)
pygame.display.update()

gameLoop = True
while gameLoop:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            gameLoop = False

#    #clock.tick(FPS)
#    #window.blit(SURFASEFONT, SURFACER)
#    #pygame.display.flip()
#    #pygame.display.update()

pygame.quit()
