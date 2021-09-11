"""
alian invator is space shooting game which is a single player game that
this is a university project 
game name : alian invator
name : amzad hossain 
e-mail: amzad.rafi@northsouth.edu
id : 1530530o42

"""
#import 

# import math as math     #for math calculation 
import sys, argparse    #argparse 
import pygame as pygame # main game module 
import random           #random module 
from pygame import mixer #mixer for music 
pygame.font.init()
pygame.mixer.init() 
pygame.init()
clock=pygame.time.Clock()

#class import 
from satting import Settings 
from ship import Ship
from bullets import Bullet 
from alian import Alien






class Game():
    def __init__(self):
        self.settings = Settings() #creat a instance of Settings class 
        self.screen = pygame.display.set_mode((self.settings.height,self.settings.width))
        pygame.display.set_caption("Alian invator")
        #allow to acces screen right lefe top and bollom etc
        self.ship= Ship(self)
        self.bullets= pygame.sprite.Group()
        self.alien= pygame.sprite.Group()
        self.create_fleet()
    def main(self):
        #main while loop
        
        while True: 
            #chack event 
            self._event()
            #ship movement 
            self.ship.ship_move()  
            # bullet create and remove 
            self.update_bullets()
            #update the display 
            self._update_display()
            #control the frame rate        
            clock.tick(60)

            
    #update the display 
    def _update_display(self):
        #fill the display 
        self.screen.fill(self.settings.black)
        #draw ship
        self.ship.blit_me()
        # display all the  bullet in sprites group 
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.alien.draw(self.screen)

           
        pygame.display.flip()

    #chak event
    def _event(self):
        #collect all the event in a list 
        for event in pygame.event.get():
            #chack if game is cross or not 
            if event.type == pygame.QUIT:
                sys.exit()
            #chack any event is keydonw or not 
            elif event.type == pygame.KEYDOWN :
                
               self.key_down(event)
               self.fire_bullets(event)
            

            elif event.type == pygame.KEYUP:
                self.key_up(event)

            
                
    def update_bullets(self) :

        self.bullets.update()  
        for Bullet in self.bullets.copy():
            if Bullet.rect.bottom < 0 :
                self.bullets.remove(Bullet)   
         

    def key_up(self,event):
        if event.key == pygame.K_a:
            self.ship.left=False

        elif event.key == pygame.K_d:
            self.ship.right=False




    def key_down(self,event) : 
        if event.key == pygame.K_a:
            self.ship.left=True

        elif event.key == pygame.K_d:
            self.ship.right=True

    def fire_bullets(self,event):
        if event.key== pygame.K_SPACE:
            if len(self.bullets) < self.settings.bullet_limit :
                new_bullets= Bullet(self)
                self.bullets.add(new_bullets)


    def create_fleet(self):
        alien= Alien(self)
        alien_width=alien.rect.width
        avilable_space_x= self.settings.width -(2*alien_width)
        number_of_alian= avilable_space_x//(2*alien_width)

        for alien in range(number_of_alian+4):
            new_alien= Alien(self)
            new_alien.rect.x= alien_width+2 *alien_width *alien
            self.alien.add(new_alien)
            print(new_alien)

if __name__ == '__main__':
    A= Game()
    A.main()
    



