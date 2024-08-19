import sys
import pygame

from settings import Settings


class Key:
    """Class to manage everything"""

    def __init__(self):
        "Start game resources"
        pygame.init()
        self.settings = Settings()
        pygame.display.set_caption("Keys!")

        # set background
        self.screen = pygame.display.set_mode(
            (self.settings.screen_witdh, self.settings.screen_height))

    def run_game(self):
        """Start main loop for the game"""
        while True:
            self._check_events()
            self._update_screen()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()

    def _check_events(self):
        # Respond to keypresses
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # If key is pressed create motion
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_key(event)

    def _check_keydown_key(self, event):

        print(event.key)
        if event.key == pygame.K_q:
            sys.exit()


if __name__ == '__main__':
    game = Key()
    game.run_game()
