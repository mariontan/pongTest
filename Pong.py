import pygame
from pygame.locals import*
img = pygame.image.load('Family.jpg')

white = (255, 64, 64)
w = 640
h = 480
screen = pygame.display.set_mode((w, h))
screen.fill((white))
running = input("enter a number");

while (running != 1):
    screen.fill((white))
    screen.blit(img,(0,0))
    pygame.display.flip()