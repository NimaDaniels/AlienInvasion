#!/usr/bin/env python3
"""
Main AlienInvasion game module
By: NimaDaniels
2025/3/9
khodenimacollab@gmail.com
"""


import sys
import pygame

from settings import Settings


class AlienInvasion:
    def __init__(self) -> None:
        """Main class to manage game assets and behaviors."""

        self.settings = Settings()
        pygame.init()

        self.screen = pygame.display.set_mode(
        (
            self.settings.screen_width,
            self.settings.screen_height)
        )
        self.background_color = (self.settings.background_color)

        pygame.display.set_caption("Alien: Invasion ( By NimaDaniels )")

    def run_game(self) -> None:
        """Start main game loop"""

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.background_color)
            pygame.display.flip()


if __name__ == "__main__":
    alien_game = AlienInvasion()
    alien_game.run_game()
