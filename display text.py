# a simple pygame text example
# vegaseat
import pygame as pg
pg.init()
# use a (r, g, b) tuple for color
yellow = (255, 255, 0)
# create the basic window/screen and a title/caption
# default is a black background
screen = pg.display.set_mode((640, 280))
pg.display.set_caption("Text adventures with Pygame")
# pick a font you have and set its size
myfont = pg.font.SysFont("Comic Sans MS", 30)
# apply it to text on a label
hello="hello world"
label = myfont.render("Python and Pygame are Fun!"+hello,1, yellow)
# put the label object on the screen at point x=100, y=100
screen.blit(label, (0, 100))
# show the whole thing
pg.display.flip()
# event loop
while True:
    for event in pg.event.get():
        # exit conditions --> windows titlebar x click
        if event.type == pg.QUIT:
            pg.quit()
            
