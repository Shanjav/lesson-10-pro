import pygame
import time
import random
pygame.init()

WIDTH = 900
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH,HEIGHT))

def change_bg():
    bg = pygame.image.load("bground.png")
    bg = pygame.transform.scale(bg,(WIDTH,HEIGHT))
    screen.blit(bg,(0,0))

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("bin.png")
        self.image = pygame.transform.scale(self.image,(40,60))
        self.rect = self.image.get_rect()

class non_recyclable(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("plastic.png")
        self.image = pygame.transform.scale(self.image,(40,40))
        self.rect = self.image.get_rect()
        