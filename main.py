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

class recyclable(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()

item_list = pygame.sprite.Group()
plastic_list = pygame.sprite.Group()
allsprites = pygame.sprite.Group()

bin = Bin()
allsprites.add(bin)

images = ["item1.png", "item2.png", "item3.png"]

for i in range(20):
    plastic = non_recyclable()
    plastic.rect.x = random.randrange(WIDTH)
    plastic.rect.y = random.randrange(HEIGHT)
    plastic_list.add(plastic)
    allsprites.add(plastic)

for i in range(50):
    item = recyclable(random.choice(images))
    item.rect.x = random.randrange(WIDTH)
    item.rect.y = random.randrange(HEIGHT)
    item_list.add(item)
    allsprites.add(item)

WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)
GREEN = (0,255,0)

playing = True
score = 0