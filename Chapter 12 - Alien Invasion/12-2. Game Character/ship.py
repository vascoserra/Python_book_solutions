import pygame


class Ship:

    """A class to manage the ship."""

    def __init__(self, bird):
        """Initialize the ship and set its starting position."""
        self.screen = bird.screen
        self.screen_rect = bird.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/bird.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
