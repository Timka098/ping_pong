import pygame

class Wall:
    def __init__(self, window):
        self.win = window
        self.height = 100
        self.y = 250
        self.rect = pygame.Rect(10, self.y, 20, self.height)



    def show(self):
        pygame.draw.rect(self.win, '#20a50e', self.rect)