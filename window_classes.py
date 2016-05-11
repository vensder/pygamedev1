#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

DISPLAY_MODE = (800, 600)
FPS = 50
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

x, y = 0, 0
moveX, moveY = 0, 0
step = 5

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode(DISPLAY_MODE)
pygame.display.set_caption("Class Sprite")


class Sprite:

    RIGHT = 1
    LEFT = 2
    STOP = 0
    RUN = 1

    def __init__(self, x, y):

        self.currentDirection = Sprite.RIGHT
        self.movement = Sprite.STOP

        self.x = x
        self.y = y
        self.width = 90
        self.height = 105
        self.image1_right = pygame.image.load('img/mario1_right.png').convert_alpha()
        self.image2_right = pygame.image.load('img/mario2_right.png').convert_alpha()
        self.image1_left = pygame.image.load('img/mario1_left.png').convert_alpha()
        self.image2_left = pygame.image.load('img/mario2_left.png').convert_alpha()
        self.timeTarget = 5
        self.timeNumber = 0
        self.currentImage = 1

    def update(self):

        self.timeNumber += 1

        if self.timeNumber == self.timeTarget:

            if self.currentImage == 1 and self.movement == Sprite.RUN:
                self.currentImage = 2  # += 1 (if we have more then 2 images
            elif self.currentImage == 2 and self.movement == Sprite.RUN:
                self.currentImage = 1

            self.timeNumber = 0

        self.render()

    def render(self):

        if self.currentImage == 1:
            if self.currentDirection == Sprite.RIGHT:
                window.blit(self.image1_right, (self.x, self.y))
            elif self.currentDirection == Sprite.LEFT:
                window.blit(self.image1_left, (self.x, self.y))
        else:
            if self.currentDirection == Sprite.RIGHT:
                window.blit(self.image2_right, (self.x, self.y))
            elif self.currentDirection == Sprite.LEFT:
                window.blit(self.image2_left, (self.x, self.y))

player1 = Sprite(0, 0)

gameLoop = True
while gameLoop:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            gameLoop = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player1.currentDirection = player1.LEFT
                player1.movement = player1.RUN
                moveX = -step
            if event.key == pygame.K_RIGHT:
                player1.currentDirection = player1.RIGHT
                player1.movement = player1.RUN
                moveX = step
            if event.key == pygame.K_UP:
                player1.movement = player1.RUN
                moveY = -step
            if event.key == pygame.K_DOWN:
                player1.movement = player1.RUN
                moveY = step

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moveX = 0
                player1.movement = player1.STOP
            if event.key == pygame.K_RIGHT:
                moveX = 0
                player1.movement = player1.STOP
            if event.key == pygame.K_UP:
                moveY = 0
                player1.movement = player1.STOP
            if event.key == pygame.K_DOWN:
                moveY = 0
                player1.movement = player1.STOP

    window.fill(WHITE)

    player1.x += moveX
    player1.y += moveY
    player1.update()

    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()
