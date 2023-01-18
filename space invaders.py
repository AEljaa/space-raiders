import os
import pygame
from pygame.locals import *
import time
import random

background_colour=(0,0,0)
size=40
d = pygame.display.set_mode((1920, 1080))

class Alien():
    def __init__(self,parent_screen):
        self.parent_screen= parent_screen
        self.alien=pygame.image.load("resources/alien.jpg").convert()
     
        self.y=100

     


    def alien_movement(self):
        self.x =+ 40
        if self.x >1780:
            self.x -= 40
        
        if self.x <200:
            self.x += 40
        
        pygame.display.update()

    def draw(self):
        self.x=random.randint(0,48)*size
        self.parent_screen.blit(self.alien,(self.x,self.y))
        pygame.display.update()
       

class ship():
    def __init__(self,parent_screen):

        self.parent_screen= parent_screen
        self.ship=pygame.image.load("resources/ship.jpg").convert()
        self.x=random.randint(0,48)*size
        self.y=1000
        self.direction=''
    


    def move_left(self):
        self.x -= 2
    def move_right(self):
        self.x += 2

    def draw(self):
        self.parent_screen.fill(background_colour)
        self.parent_screen.blit(self.ship,(self.x,self.y))
        pygame.display.update()
    
    def bound_correction(self):
        
        if self.x <=40:
            self.x=40
        if self.x>=1840:
            self.x=1840
        pygame.display.update()

class Player:
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.speed = 4

    def draw(self):
        pygame.draw.rect(d, (0, 0, 0), (self.x, self.y, self.width, self.height))

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

    def bound_correction(self):
        
        if self.x <=0:
            self.x=0
        if self.x>=1900:
            self.x=1892
        pygame.display.update()


p = Player(600, 1000, 50, 30) 

class Bullet:
    
    def __init__(self, x, y):
        self.radius = 10
        self.speed = 10
        self.x = x
        self.y = y

    def update(self):
        self.y -= self.speed
    
    def draw(self):
        pygame.draw.circle(d, (255, 0, 0), (self.x, self.y), self.radius)
        print(self.x,"",self.y)

bullets = []


class Game:
    def __init__(self):
        pygame.init()
        self.surface=pygame.display.set_mode((1920,1080))
       
        self.alien=Alien(self.surface)     
       
        p.draw()


    def play(self):

        self.alien.draw()  
       
        
        p.bound_correction()
        
        pygame.display.update() 
    


    def run(self):
        running=True
        pause=False
       
      
        while running:
            pygame.time.Clock().tick(100)
            # handel events
            for event in pygame.event.get():
                
                if event.type ==  KEYDOWN:
                    if event.key==K_ESCAPE:
                            running=False
                            
                    if not pause:
                        
                        if event.key == K_SPACE:
                           bullets.append(Bullet(p.x+p.width//2, p.y))
                
               
            
            # update objects
            keys = pygame.key.get_pressed() 
        
            if keys[pygame.K_LEFT]:
                p.move_left()
            if keys[pygame.K_RIGHT]:
                p.move_right()
            for b in bullets:
                b.update()
       

            d.fill((98, 98, 98))

            # draw scene
            for b in bullets:
                b.draw()
            p.draw()
            p.bound_correction()
            pygame.display.update()

if __name__=="__main__":
    game=Game()
    game.run()
    
    