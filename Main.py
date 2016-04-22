#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import pygame
from classes import *
from process import process

# print sys.version

SCREENWIDTH, SCREENHEIGHT = 640, 480

pygame.init()
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), 0, 32)

img_python = pygame.image.load("img/python.png").convert_alpha() # .convert_alpha()
img_tux = pygame.image.load("img/tux.png").convert_alpha() # .convert_alpha()

green = (31, 147, 40)
blue = (70, 88, 169)
red = (225, 21, 57)
brown = (100, 0, 0)

clock = pygame.time.Clock()
FPS = 48
#fivesecondinterval = FPS * 5
totalframes = 0

tux = Tux(0, 0, 128, 128, "img/tux.png")
tux2 = Tux(0, SCREENHEIGHT // 2, 128, 128, "img/tux.png")
pump = Pump(SCREENWIDTH - 256, SCREENHEIGHT - 256, 256, 256, "img/pumpkin.png")

# ----------------- Main Program Loop -----------------
while True:
    process(tux)
    # logic
    
    #totalframes += 1
    #if totalframes % fivesecondinterval == 0:
    #    print("5 sec passed")

    tux.motion()
    tux2.motion()
    pump.motion()
    # logic
    # draw
    screen.fill(brown)    
    BaseClass.allsprites.draw(screen)
    
    if totalframes > FPS * 1:
        pygame.draw.line(screen, blue, (0, 0), (SCREENWIDTH, SCREENHEIGHT), 1)
    if totalframes > FPS * 2:
        pygame.draw.line(screen, blue, (SCREENWIDTH, 0), (0, SCREENHEIGHT), 1)
    if totalframes > FPS * 3:
        pygame.draw.rect(screen, green, (SCREENWIDTH / 3.0, SCREENHEIGHT / 3.0, SCREENWIDTH / 3.0, SCREENHEIGHT / 3.0))
    if totalframes > FPS * 4:
        pygame.draw.rect(screen, blue, (SCREENWIDTH * 0.375, SCREENHEIGHT * 0.375, SCREENWIDTH / 4.0, SCREENHEIGHT // 4))
    if totalframes > FPS * 5:
        pygame.draw.rect(screen, green, (SCREENWIDTH * 0.4, SCREENHEIGHT * 0.4, SCREENWIDTH // 5, SCREENHEIGHT // 5))
    if totalframes > FPS * 6:
        pygame.draw.rect(screen, blue, (SCREENWIDTH * (1 / 2.0 - 1 / 12.0), SCREENHEIGHT * (1 / 2.0 - 1 / 12.0), SCREENWIDTH // 6, SCREENHEIGHT // 6))
    if totalframes > FPS * 7:
        screen.blit(img_python, (SCREENWIDTH // 2 - 128, SCREENHEIGHT // 2 - 128))
    if totalframes > FPS * 8:
        pygame.draw.circle(screen, green, (SCREENWIDTH / 2, SCREENHEIGHT / 2), SCREENHEIGHT // 6, 2)
    if totalframes > FPS * 9:
        screen.blit(img_tux, (SCREENWIDTH // 2 - 64, SCREENHEIGHT // 2 - 64))
        #screen.fill(green)
    if totalframes > FPS * 10:
        totalframes = 0

    pygame.display.flip()
    totalframes += 1
    clock.tick(FPS)
#draw

