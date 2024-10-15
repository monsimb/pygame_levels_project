"""
File contains constants for our levels project.
"""
import pygame # type: ignore
pygame.init()

# Display info
display_info = pygame.display.Info()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 760
TILE = 40
MAZE_WIDTH = SCREEN_WIDTH // TILE
MAZE_HEIGHT = SCREEN_HEIGHT // TILE

WINDOW_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
FPS = 60

# start and end coords
PLAYER_START = (TILE, TILE)
END_RECT = pygame.Rect(960, 680, TILE, TILE)
