import pygame, os
from sprite import Wall, Ball

pygame.init()

#creat window and setings

win = pygame.display.set_mode((800, 600))
pygame.display.set_caption('ping pong')

wall1 = Wall(win, 10)
wall2 = Wall(win, 770)

ball = Ball(win)
#FPS

fps = pygame.time.Clock()

#main while
while True:
    pygame.display.flip()
    win.fill((0, 20, 5))
    fps.tick(144)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    wall1.show()
    wall1.move()
    wall2.show()
    ball.show()