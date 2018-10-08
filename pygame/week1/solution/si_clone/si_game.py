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
            (settings.screen_width, settings.screen_height))
        pygame.display.set_caption("Raptor Invaders")
        
        # Set the background color.
        self.bg_color = (230, 230, 230)
        
        # Make a ship.
        self.ship = Ship(self)
        # Make a group to store bullets in.
        self.bullets = Group()
    
    def run_game(self):
        #add animation clock
        fpsClock = pygame.time.Clock()
        
        # Start the main loop for the game.
        while True:
            elapsedTime = fpsClock.tick(self.settings.targetFps)
            self.check_events()
            self.ship.update(elapsedTime)
            self.update_bullets(elapsedTime)
            self.update_screen()
            
    
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
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)
                
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
        for self.bullet in self.bullets.sprites():
            self.bullet.draw_bullet()
        self.ship.blitme()
    
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

    def getSettings(self):
        return self.settings
    def getShip(self):
        return self.ship
    def getButtlets(self):
        return self.bullets
    def getScreen(self):
        return self.screen