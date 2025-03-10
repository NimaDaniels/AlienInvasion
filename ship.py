"""
Module for the user Ship
object.
"""


import pygame


class Ship:
    """Class to manage player Ship"""

    def __init__(self, ai_game) -> None:
        """Intialize player Ship and set starting position"""

        self.game_screen = ai_game.screen
        self.game_screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("images/player_ship.bmp")
        self.rect = self.image.get_rect()
