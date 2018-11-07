import pygame

class Ship():

    def __init__(self, game):
        """Initialize the ship, and set its starting position."""
        self.game = game
        
        # Load the ship image, and get its rect.
        self.image = pygame.image.load('images/eagle.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.game.getScreen().get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        
        # Movement flags.
        self.moving_right = False
        self.moving_left = False
        
    def update(self, elapsedMs):
        """Update the ship's position, based on movement flags."""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += elapsedMs*self.game.getSettings().ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= elapsedMs*self.game.getSettings().ship_speed_factor
            
        # Update rect object from self.center.
        self.rect.centerx = self.center

    def draw(self):
        """Draw the ship at its current location."""
        self.game.getScreen().blit(self.image, self.rect)
