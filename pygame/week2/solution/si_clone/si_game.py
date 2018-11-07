import pygame
from pygame.sprite import Group

from ship import Ship

import sys

from bullet import Bullet
import settings

from alien import Alien

class Si_Game:
    def __init__(self, settings):
        # Initialize pygame, settings, and screen object.
        pygame.init()
        self.settings = settings
        self.screen = pygame.display.set_mode(
            (settings.screen_width, settings.screen_height))
        pygame.display.set_caption("Raptor Invaders")
        
        # Set the background color.
        self.bg_color = (230, 230, 230)
        
        # Make a ship.
        self.ship = Ship(self)
        # Make a group to store bullets in.
        self.bullets = Group()
        self.aliens = Group()
        new_alien = Alien(self)
        self.aliens.add(new_alien)
        
    
    def run_game(self):
        #add animation clock
        fpsClock = pygame.time.Clock()
        
        # Start the main loop for the game.
        while True:
            elapsedTime = fpsClock.tick(self.settings.targetFps)
            if(self.check_events() == None):
                break
            self.ship.update(elapsedTime)
            self.update_bullets(elapsedTime)
            self.update_aliens(elapsedTime)
            self.update_screen()

        pygame.quit()            
    
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
                return None
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)
                
        return True
                
    def fire_bullet(self):
        """Fire a bullet, if limit not reached yet."""
        # Create a new bullet, add to bullets group.
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen, each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        
        # Redraw all bullets, behind ship and aliens.
        for bullet in self.bullets.sprites():
            bullet.draw()
        
        for alien in self.aliens.sprites():
            alien.draw()
        self.ship.draw()
    
    
        
    
        # Make the most recently drawn screen visible.
        pygame.display.flip()
        
    def update_bullets(self, elapsedMs):
        """Update position of bullets, and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()
    
        # Get rid of bullets that have disappeared.
        for self.bullet in self.bullets.copy():
            if self.bullet.rect.bottom <= 0:
                self.bullets.remove(self.bullet)

    def update_aliens(self, elapsedMs):
        """Update position of bullets, and get rid of old bullets."""
        # Update bullet positions.
        self.aliens.update(elapsedMs)
        for alien in self.aliens:
            if alien.check_edges():
                self.settings.fleet_direction *= -1
                break



    def getSettings(self):
        return self.settings
    def getShip(self):
        return self.ship
    def getButtlets(self):
        return self.bullets
    def getScreen(self):
        return self.screen
    
    
if __name__ == "__main__":
    #create our settings. Incase we need to load diffrent values
    settings = settings.Settings()
    
    #create the game instance
    game = Si_Game(settings)
    
    #run the game. Does not return until exit.
    game.run_game()