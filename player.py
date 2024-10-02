"""
This file containts important player information
including collisions and sprite functionalities.
"""

import pygame   # type: ignore
from config import TILE


class Player:
    """
    
    """
    def __init__(self, x: int, y: int, sprite_path: str):
        self.x = x
        self.y = y
        self.sprite = pygame.image.load(sprite_path).convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, (TILE, TILE))     # Ensure player sprite is size of 1 tile
        self.rect = self.sprite.get_rect(topleft=(x, y))                    # saves x,y as top left pixels for sprite

    def update(self, dx: int, dy: int, level_layout):
        """
        Calculate new positions for Player character.

        Parameters
            dx : next position x
            dy : next position y
            level_layout : map of level
        """
        new_x = self.x + dx
        new_y = self.y + dy

        # Check for collisions based on direction
        if dx != 0:  # Moving left or right
            if not self.check_collision(dx, 0, level_layout):   # Check horizontal
                self.x = new_x
        
        if dy != 0:  # Moving up or down
            if not self.check_collision(0, dy, level_layout):  # Check vertical
                self.y = new_y

        # Update the rectangle for drawing
        self.rect.topleft = (self.x, self.y)

    def check_collision(self, dx: int, dy: int, level_layout):
        """
        Checks collision between player and level.

        Parameters
            dx : next position x
            dy : next position y
            level_layout : map of level
        """
        # create new rect for where player wants to move
        new_rect = self.rect.move(dx, dy)

        # indices for each wall in layout
        walls = [[y, x] for y, row in enumerate(level_layout) for x, tile in enumerate(row) if tile=='#']
        
        # check each wall for collision with new player coords
        for y, x in walls:
            wall_rect = pygame.Rect(x * TILE, y * TILE, TILE, TILE)     # update wall rect with wall being checked
            
            if new_rect.colliderect(wall_rect):     # collision detected = true
                return True

        return False  # no collision = false

    def draw(self, screen):
        """
        Draws player.
        Parameters
            screen : pygame screen obj
        """
        screen.blit(self.sprite, (self.x, self.y))
