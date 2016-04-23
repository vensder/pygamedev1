#!/usr/bin/env python2
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

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()
window = pygame.display.set_mode(DISPLAY_MODE)
pygame.display.set_caption("Keyboard")

FONT = pygame.font.SysFont("monospace", 40)
SURFASEFONT = FONT.render("Hello from PyGame!", True, BLACK, GRAY)
SURFACER = SURFASEFONT.get_rect()
SURFACER.center = (300, 200)
window.fill(WHITE)

gameLoop = True
while gameLoop:
    window.blit(SURFASEFONT, SURFACER)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            gameLoop = False

    #clock.tick(FPS)
    pygame.display.update()

pygame.quit()