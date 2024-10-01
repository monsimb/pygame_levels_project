# main.py
import pygame
from config import WINDOW_SIZE, FPS
from minigame_manager import MiniGameManager

def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    clock = pygame.time.Clock()

    # Initialize the mini-game manager with level names
    levels = ['level1', 'level2']  # Add more levels as needed
    mini_game_manager = MiniGameManager(levels)

    # Run each mini-game
    for level in levels:
        mini_game_manager.run_level(level, screen)

    pygame.quit()

if __name__ == "__main__":
    main()
