import pygame

class Wall:
    def __init__(self, window, x):
        self.win = window
        self.height = 100
        self.y = 250
        self.x = x
        self.rect = pygame.Rect(self.x, self.y, 20, self.height)
        


    def show(self):
        pygame.draw.rect(self.win, '#20a50e', self.rect)
    
    def move(self):
        self.key = pygame.key.get_pressed()
        if self.key[pygame.K_DOWN] and self.y < 490:
            self.y += 2
            self.rect.y = self.y
        
        if self.key[pygame.K_UP] and self.y > 10:
            self.y -= 2
            self.rect.y = self.y

class Ball:
    def __init__(self, win):
        self.win = win
        self.x = 100
        self.y = 100
        #self.rect = pygame.Rect(self.x, self.y, self.win)
        
    def show(self):
        pygame.draw.circle(self.win, (255, 255, 255), (self.x, self.y), 30, 5)