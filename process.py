#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import sys

def process(tux):
    # processes
    my_events = pygame.event.get() # list of events
    
    if my_events:
        print(my_events)

    for event in my_events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        tux.image = pygame.image.load("img/tuxflipped.png").convert_alpha()
        tux.velx = 5
    elif keys[pygame.K_a]:
        tux.image = pygame.image.load("img/tux.png").convert_alpha()
        tux.velx = -5
    else:
        tux.velx = 0

