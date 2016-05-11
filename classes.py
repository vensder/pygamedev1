#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

class BaseClass(pygame.sprite.Sprite):
    
    allsprites = pygame.sprite.Group()
    
    def __init__(self, x, y, width, height, image_string):
        
        pygame.sprite.Sprite.__init__(self)
        BaseClass.allsprites.add(self)
        
        self.image = pygame.image.load(image_string).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.width = width
        self.height = height
        

class Tux(BaseClass):
    
    List = pygame.sprite.Group()
    
    def __init__(self, x, y, width, height, image_string):
        
        BaseClass.__init__(self, x, y, width, height, image_string)
        Tux.List.add(self)
        self.velx = 0
        
    def motion(self):
        
        self.rect.x += self.velx

class Pump(BaseClass):
    
    List = pygame.sprite.Group()
    
    def __init__(self, x, y, width, height, image_string):
        
        BaseClass.__init__(self, x, y, width, height, image_string)
        Tux.List.add(self)
        self.velx = -3
        
    def motion(self):
        
        self.rect.x += self.velx
