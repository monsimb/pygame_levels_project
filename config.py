"""
File contains constants for our levels project.
"""
import pygame # type: ignore
pygame.init()

# Display info
display_info = pygame.display.Info()

SCREEN_WIDTH = display_info.current_w
SCREEN_HEIGHT = display_info.current_h

WINDOW_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
FPS = 60

# Window size constants using 'tiles'
TILE = 50
MAZE_WIDTH = SCREEN_WIDTH//TILE
MAZE_HEIGHT = SCREEN_HEIGHT//TILE

# start and end coords
PLAYER_START = (50, SCREEN_HEIGHT-150)
END_RECT = pygame.Rect((MAZE_WIDTH)*TILE-3, 20*TILE-3, TILE+3, TILE+3)
