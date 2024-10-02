
"""
Contains functions for loading levels, starting sprites, and getting player's starting pos.
"""
import importlib.util
import pygame

from config import TILE, END_RECT

class Level:
    def __init__(self, level_file):
        self.layout, self.color_mapping, self.sprites = self.load_level(level_file)

    def load_level(self, level_file):
        # Load the Python file as a module
        spec = importlib.util.spec_from_file_location("level_module", level_file)
        level_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(level_module)
        
        # Get the layout, color mapping, and sprites from the module
        return level_module.layout, level_module.color_mapping, level_module.sprites

    def draw(self, screen):
        pygame.transform.scale(self.sprites, (TILE, TILE))
        for y, row in enumerate(self.layout):
            for x, tile in enumerate(row):
                if tile in self.sprites:
                    # Load the sprite image and scale it to 50x50
                    sprite_image = pygame.image.load(self.sprites[tile]).convert_alpha()
                    sprite_image = pygame.transform.scale(sprite_image, (TILE, TILE))
                    screen.blit(sprite_image, (x * TILE, y * TILE))
                elif tile in self.color_mapping:
                    color = self.color_mapping[tile]
                    pygame.draw.rect(screen, color, (x * tile_size, y * tile_size, tile_size, tile_size))
                    
        pygame.draw.rect(screen, self.color_mapping['E'], END_RECT)      # DO NOT REMOVE OR CHANGE THIS

    def get_player_start_position(self):
        for y, row in enumerate(self.layout):
            for x, tile in enumerate(row):
                if tile == '@':
                    return (x * 50, y * 50)  # Return the starting position of the player, adjusted for 50x50
        return None
