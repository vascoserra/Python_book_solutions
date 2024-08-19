import sys
import pygame

from settings import Settings
from ship import Ship


class Bird:
    """Class to manage game assets and behavior"""

    def __init__(self):
        """Start game and resources"""
        pygame.init()
        self.settings = Settings()

        # Set the background color
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Poo Revenge")
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Make the most recently drawn screen visible.
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    game = Bird()
    game.run_game()
