#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

DISPLAY_MODE = (800, 600)
FPS = 50
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
R, G, B = 0, 0, 0
changeR, changeG, changeB = 0, 0, 0
x, y = 0, 0
moveX, moveY = 0, 0
step = 5
stepR, stepG, stepB = 1, 1, 1

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode(DISPLAY_MODE)
pygame.display.set_caption("My Window :)")


class Sprite:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50

    def render(self):

        pygame.draw.rect(
            window,
            BLACK,
            (self.x,
                self.y,
                self.width,
                self.height))

player = Sprite(200, 200)

gameLoop = True

while gameLoop:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            gameLoop = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveX = -step
            if event.key == pygame.K_RIGHT:
                moveX = step
            if event.key == pygame.K_UP:
                moveY = -step
            if event.key == pygame.K_DOWN:
                moveY = step

            if event.key == pygame.K_r:
                changeR += stepR
            if event.key == pygame.K_g:
                changeG += stepG
            if event.key == pygame.K_b:
                changeB += stepB

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moveX = 0
            if event.key == pygame.K_RIGHT:
                moveX = 0
            if event.key == pygame.K_UP:
                moveY = 0
            if event.key == pygame.K_DOWN:
                moveY = 0

            if event.key == pygame.K_r:
                changeR = 0
            if event.key == pygame.K_g:
                changeG = 0
            if event.key == pygame.K_b:
                changeB = 0

    x += moveX
    y += moveY
    R += changeR
    G += changeG
    B += changeB

    if R > 255: stepR, R = -1, 255
    if G > 255: stepG, G = -1, 255
    if B > 255: stepB, B = -1, 255

    if R < 0: stepR, R = 1, 0
    if G < 0: stepG, G = 1, 0
    if B < 0: stepB, B = 1, 0

    window.fill((255-R, 255-G, 255-B))
    
    player.x += moveX
    player.y += moveY

    pygame.draw.rect(window, (R, G, B), (x, y, 50, 50))
    print (R, G, B)
    clock.tick(FPS)

    pygame.display.flip()

pygame.quit()
