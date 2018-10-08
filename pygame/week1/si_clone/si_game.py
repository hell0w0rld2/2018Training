import pygame
from pygame.sprite import Group

from ship import Ship

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
            for event in pygame.event.get():
                pass
            #update
            
            #(17 is expected frame delay of 60Hz in ms.)
            
            
            #draw
            
            
            self.draw()
            
    
    def check_keydown_events(self, event):
        """Respond to keypresses."""
        pass
            
    def check_keyup_events(self, event):
        """Respond to key releases."""
        pass
    
    def check_events(self):
        """Respond to keypresses and mouse events."""
        pass
                
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
        pass
    def getButtlets(self):
        pass
    def getScreen(self):
        return self.screen