import os, sys
import pygame
from pygame.locals import *

screen = pygame.display.set_mode((640,480))

PADDLE_WIDTH = 50
PADDLE_HEIGHT = 10
p1Paddle = pygame.Rect(10, 430, PADDLE_WIDTH, PADDLE_HEIGHT)
green = (0,0,0)
black = (1,1,1)

PADDLE_COLOR = pygame.color.Color(green)
SCREEN_COLOR = pygame.color.Color(black)
GO

puckSpeedX = 1
puckSpeedY = 1

PUCK_COLOR = pygame.color.Color(greenb)
puck = pygame.Rect(320,240,10,10)



while True:

    p1Paddle.left = pygame.mouse.get_pos()[0]

    puck.left = puck.left + puckSpeedX
    
    puck.top = puck.top + puckSpeedY
    
    screen.fill(SCREEN_COLOR)
    GO

screen.fill(PADDLE_COLOR, p1Paddle)

screen.fill(PUCK_COLOR, puck)

pygame.time.delay(10)    

if puck.colliderect(p1Paddle):

    puckSpeedY = puckSpeedY * -1


if puck.top &lt  or puck.bottom > 480

    puckSpeedY = puckSpeedY * -1



if puck.left &lt  or puck.right > 640

puckSpeedX = puckSpeedX * -1







