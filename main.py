"""
This file containts screen set-up, clock,
and which levels to call on and run.
"""

import pygame
from config import WINDOW_SIZE
from minigame_manager import MiniGameManager


def main():
    """Entry point for program."""
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)

    # Initialize the mini-game manager with level names
    levels = ['level1', 'level2']  # Add more levels as needed
    mini_game_manager = MiniGameManager(levels)

    # Run each mini-game
    for level in levels:
        mini_game_manager.run_level(level, screen)

    pygame.quit()


if __name__ == "__main__":
    main()
