#!/usr/bin/env python3
"""
Main AlienInvasion game module
By: NimaDaniels
2025/3/9
khodenimacollab@gmail.com
"""


import sys
import pygame


class AlienInvasion:
    def __init__(self) -> None:
        """Main class to manage game assets and behaviors."""

        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.background_color = (255, 255, 255)

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
