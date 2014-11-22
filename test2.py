import pygame, sys
from pygame.locals import *
import random

# Number of frames per second
# Change this value to speed up or slow down your game
FPS = 100

#Global Variables to be used through our program
WINDOWWIDTH = 400
WINDOWHEIGHT = 300
LINETHICKNESS = 10
PADDLESIZE = 50
PADDLEOFFSET = 20
score1 = 0
score2 = 0

# Set up the colours
BLACK     = (0  ,0  ,0  )
WHITE     = (255,255,255)

#Draws the arena the game will be played in. 
def drawArena():
    DISPLAYSURF.fill((0,0,0))
    #Draw outline of arena
    pygame.draw.rect(DISPLAYSURF, WHITE, ((0,0),(WINDOWWIDTH,WINDOWHEIGHT)), LINETHICKNESS*2)
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
    pygame.draw.rect(DISPLAYSURF, WHITE, paddle)

#draws the ball
def drawBall(ball):
    pygame.draw.rect(DISPLAYSURF, WHITE, ball)
    
#Random start direction, ensures that each time the game starts
#ball may go in either direction
def start():
    number = random.randint(1,10)
    if number >= 5:
        return 1
    if number < 5:
        return -1
    
#moves the ball returns new position
def moveBall(ball, ballDirX, ballDirY):
    ball.x += ballDirX
    ball.y += ballDirY
    return ball

#Checks for a collision with a wall or paddle, and 'bounces' ball off them.
#direction reverses
def checkCollision(ball, paddle1, paddle2, ballDirX, ballDirY):    #125          90  paddle2.top < ball.top is with respect to the screen When ball goes up  ball.top decreses
    condition1 = (ballDirX == 1 and ball.right == paddle2.left and paddle2.top < ball.top and paddle2.bottom > ball.bottom)
    condition2 = (ballDirX == -1 and ball.left == paddle1.right and paddle1.top < ball.top and paddle1.bottom > ball.bottom)
    
    if ball.top == (LINETHICKNESS) or ball.bottom == (WINDOWHEIGHT - LINETHICKNESS):
        ballDirY *= -1
    if ball.left == (LINETHICKNESS) or ball.right == (WINDOWWIDTH - LINETHICKNESS) or condition1 or condition2:
        ballDirX *= -1
    return ballDirX, ballDirY

#keeps track of the score
def score(ball, paddle1, paddle2,ballDirX):
    condition1 = (ballDirX == 1 and ball.right == paddle2.left and paddle2.top < ball.top and paddle2.bottom > ball.bottom)
    condition2 = (ballDirX == -1 and ball.left == paddle1.right and paddle1.top < ball.top and paddle1.bottom > ball.bottom)
    if condition1:
        score1 += 1
        return score1
    
    if condition2:
        score2 += 1
        return score2

#print the score
def printScore(score1, score2,DISPLAYSURF):
    font = pygame.font.SysFont("Comic Sans MS",30)
    score = font.render(score1 + " " + score2, 1, (255,255,0))
    DISPLAYSURF.blit(score, (0,50))
    
#end the game
def end():
    pygame.quit()
    sys.exit()


    
#Main function
def main():
    pygame.init()
    global DISPLAYSURF

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
            # arrow key movements player1:up and down player2: w and d
            elif event.type == KEYDOWN:
                   if event.key == K_UP:
                        paddle1.y += -50 
                   elif event.key == K_DOWN:
                        paddle1.y += 50
                   elif event.key == K_w:
                        paddle2.y += -50 
                   elif event.key == K_s:
                        paddle2.y += 50
                #close by pressing end    
                   elif event.key == K_END:
                        end()

        drawArena()
        drawPaddle(paddle1)
        drawPaddle(paddle2)
        drawBall(ball)
        #print paddle1.top
        #print ball.top
        ball = moveBall(ball, ballDirX, ballDirY)
        ballDirX, ballDirY = checkCollision(ball, paddle1, paddle2, ballDirX, ballDirY)
        #score1, score2 = score(ball, paddle1, paddle2,ballDirX)
        score1 = str(10)
        score2 = str(20)
        printScore(score1, score2,DISPLAYSURF)

        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__=='__main__':
    main()
