import pygame, sys
from pygame.locals import *
import sys, os, traceback
import random

#sounds
pygame.mixer.init(buffer=0)
sounds = {
    "ping" : pygame.mixer.Sound("data/ping.wav"),
    "click" : pygame.mixer.Sound("data/click.wav"),
    "da-ding" : pygame.mixer.Sound("data/da-ding.wav")
}
sounds["ping"].set_volume(0.05)
sounds["click"].set_volume(0.5)
sounds["da-ding"].set_volume(0.5)

# Number of frames per second
# Change this value to speed up or slow down your game
FPS = 100

#Global Variables to be used through our program
WINDOWWIDTH = 400
WINDOWHEIGHT = 300
LINETHICKNESS = 10
PADDLESIZE = 50
PADDLEOFFSET = 10
score1 = 0
score2 = 0

# Set up the colours
BLACK     = (0  ,0  ,0  )
WHITE     = (255,255,255)
PINK      = (255,0, 255)
YELLOW    = (255,255,0)

#Draws the arena the game will be played in. 
def drawArena():
    DISPLAYSURF.fill((0,0,0))
       
    #Draw centre line
    pygame.draw.line(DISPLAYSURF, WHITE, ((WINDOWWIDTH/2),0),((WINDOWWIDTH/2),WINDOWHEIGHT), (LINETHICKNESS/4))

#Draws the paddle
def drawPaddle(paddle):
    #Stops paddle moving too low
    if paddle.bottom > WINDOWHEIGHT - LINETHICKNESS:
        paddle.bottom = WINDOWHEIGHT - LINETHICKNESS
    #Stops paddle moving too high
    elif paddle.top < LINETHICKNESS:
        paddle.top = LINETHICKNESS
    #Draws paddle
    pygame.draw.rect(DISPLAYSURF, PINK, paddle)

#draws the ball
def drawBall(ball):
    pygame.draw.rect(DISPLAYSURF, WHITE, ball)
    
#Random start direction, ensures that each time the game starts
#ball may go in either direction
def start():
    number = random.randint(1,5000)
    if number >= 25:
        return 1
    if number < 25:
        return -1
    
#moves the ball returns new position
def moveBall(ball, ballDirX, ballDirY):
    ball.x += ballDirX
    ball.y += ballDirY
    return ball

#Checks for a collision with a wall or paddle, and 'bounces' ball off them.
#direction reverses
def checkCollision(ball, paddle1, paddle2, ballDirX, ballDirY):    #125          90  paddle2.top < ball.top is with respect to the screen When ball goes up  ball.top decreses
    condition1 = (ballDirX == 1 and ball.right == paddle2.left and paddle2.top < ball.top and paddle2.bottom > ball.bottom)#collide with paddle2
    condition2 = (ballDirX == -1 and ball.left == paddle1.right and paddle1.top < ball.top and paddle1.bottom > ball.bottom)#collide with paddle1
    
    if ball.top == 0 or ball.bottom == WINDOWHEIGHT:
        ballDirY *= -1
    if condition1 or condition2:
        ballDirX *= -1
        sounds["ping"].play()
    return ballDirX, ballDirY

#keeps track of the score
def score(ball, paddle1, paddle2, ballDirX):
    global score1, score2 #for inbound local reference error

    if ball.left == 0: #ball has exited the screen on the left
        score2 += 1
        sounds["click"].play()
    if ball.right == WINDOWWIDTH: #ball has exited the screen on the right
        score1 += 1
        sounds["click"].play()
        
    return score1, score2

#print the score
def printScore(scor1, scor2,DISPLAYSURF):
    font = pygame.font.SysFont("Times New Roman",30)
    scr1 = str(scor1)
    scr2 = str(scor2)
    score = font.render(scr1 + "                      " + scr2, 1, YELLOW)
    DISPLAYSURF.blit(score, (90,50))
    
#end the game
def end():
    pygame.quit()
    sys.exit()

#Main function
def main():
    pygame.init()
    global DISPLAYSURF

    sounds["ping"].play()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT)) 
    pygame.display.set_caption('Pong')

    #Initiate variable and set starting positions
    #any future changes made within rectangles
    ballX = WINDOWWIDTH/2 - LINETHICKNESS/2
    ballY = WINDOWHEIGHT/2 - LINETHICKNESS/2
    playerOnePosition = (WINDOWHEIGHT - PADDLESIZE) /2
    playerTwoPosition = (WINDOWHEIGHT - PADDLESIZE) /2

    #tells the ball where to start moving
    ballDirX = start() 
    ballDirY = start() 

    #Creates Rectangles for ball and paddles.
    paddle1 = pygame.Rect(PADDLEOFFSET,playerOnePosition, LINETHICKNESS,PADDLESIZE)
    paddle2 = pygame.Rect(WINDOWWIDTH - PADDLEOFFSET - LINETHICKNESS, playerTwoPosition, LINETHICKNESS,PADDLESIZE)
    ball = pygame.Rect(ballX, ballY, LINETHICKNESS, LINETHICKNESS)

    #starting score
    score1 = 0
    score2 = 0
    
    #Draws the starting position of the Arena
    drawArena()
    drawPaddle(paddle1)
    drawPaddle(paddle2)
    drawBall(ball)

    pygame.mouse.set_visible(0) # make cursor invisible

    while True: #main game loop
        for event in pygame.event.get():
            #close by mouse
            if event.type == QUIT:
                end()
            # arrow key movements player2:up and down player1: w and d
            elif event.type == KEYDOWN:
                   if event.key == K_UP:
                        paddle2.y += -50 
                   elif event.key == K_DOWN:
                        paddle2.y += 50
                   elif event.key == K_w:
                        paddle1.y += -50 
                   elif event.key == K_s:
                        paddle1.y += 50
                #close by pressing end    
                   elif event.key == K_END:
                        end()

        drawArena()
        drawPaddle(paddle1)
        drawPaddle(paddle2)
        drawBall(ball)
        
        if ball.left <= 0 or ball.right >= WINDOWWIDTH:
            sounds["ping"].play()
            ballDirX = start() 
            ballDirY = start()
            ball = pygame.Rect(ballX, ballY, LINETHICKNESS, LINETHICKNESS)
        
        ball = moveBall(ball, ballDirX, ballDirY)
        ballDirX, ballDirY = checkCollision(ball, paddle1, paddle2, ballDirX, ballDirY)

        score1, score2 = score(ball, paddle1, paddle2, ballDirX)

        printScore(score1, score2,DISPLAYSURF)

        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__=='__main__':
    main()
