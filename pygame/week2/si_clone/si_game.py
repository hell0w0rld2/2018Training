import pygame
from pygame.sprite import Group

from ship import Ship
import settings

import sys

from bullet import Bullet


class Si_Game:
    def __init__(self, settings):
        # Initialize pygame, settings, and screen object.
        pygame.init()
        self.settings = settings
        self.screen = pygame.display.set_mode(
            (640, 640))
        pygame.display.set_caption("Raptor Invaders")
        
        self.ship = Ship(self);
    
    def run_game(self):
        #add animation clock
        
        # Start the main loop for the game.
        while True:
            pass
            #calculate elapsed time
            
            #check for events
            if self.check_events() == None:
                break;
            
            #update
            self.ship.update(17)
            #(17 is expected frame delay of 60Hz in ms.)
            
            
            #draw
            
            
            self.draw()
            
          
    def check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()
            
    def check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)
                
        return True
    
    def fire_bullet(self):
        """Fire a bullet, if limit not reached yet."""
        # Create a new bullet, add to bullets group.
        pass
    
    def draw(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen, each pass through the loop.
        self.screen.fill((224,112,24))
        
        #draw bullets
        
        #draw ship
        self.ship.draw();
    
        # Make the most recently drawn screen visible.
        pygame.display.flip()
        
    def update_bullets(self, elapsedMs):
        """Update position of bullets, and get rid of old bullets."""
        # Update bullet positions.
    
        # Get rid of bullets that have disappeared.

    def getSettings(self):
        return self.settings
    def getShip(self):
        return self.ship
    def getButtlets(self):
        pass
    def getScreen(self):
        return self.screen
    
    
    
if __name__ == "__main__":
    #create our settings. Incase we need to load diffrent values
    settings = settings.Settings()

    #create the game instance
    game = Si_Game(settings)

    #run the game. Does not return until exit.
    game.run_game()