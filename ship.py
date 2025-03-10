"""
Module for the user Ship
object.
"""


import pygame
from alien_invasion import AlienInvasion


class Ship:
    """Class to manage ship."""

    def __init__(self, ai_game: AlienInvasion) -> None:
        """Intialize ship and set starting position"""

        self.game_screen = ai_game.screen
        self.game_screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("images/player_ship.bmp")
        self.rect = self.image.get_rect()
