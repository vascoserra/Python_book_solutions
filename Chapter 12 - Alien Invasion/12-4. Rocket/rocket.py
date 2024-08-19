import sys
import pygame

from settings import Settings
from ship import Ship


class Rocket:
    """Class to manage everything"""

    def __init__(self):
        "Start game resources"
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Rocket Beach!")

        # set background
        self.screen = pygame.display.set_mode(
            (self.settings.screen_witdh, self.settings.screen_height))
        # Create ship
        self.ship = Ship(self)

    def run_game(self):
        """Start main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()

    def _check_events(self):
        # Respond to keypresses
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # If key is pressed create motion
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            # If key is not pressed stop motion
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        # If stop pressing right
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        # If stop pressing left
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        # If stop pressing up
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        # If stop pressing up
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_keydown_events(self, event):
        """Respond to key presses"""
        if event.key == pygame.K_RIGHT:
            # Move ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move ship to the left
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        # If stop pressing up
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True


if __name__ == '__main__':
    game = Rocket()
    game.run_game()
