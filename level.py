# level.py
import importlib.util
import pygame

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
        tile_size = 50  # Set tile size to 50x50 for sprites
        pygame.transform.scale(self.sprites, (50, 50))
        for y, row in enumerate(self.layout):
            for x, tile in enumerate(row):
                if tile in self.sprites:
                    # Load the sprite image and scale it to 50x50
                    sprite_image = pygame.image.load(self.sprites[tile]).convert_alpha()
                    sprite_image = pygame.transform.scale(sprite_image, (tile_size, tile_size))
                    screen.blit(sprite_image, (x * tile_size, y * tile_size))
                elif tile in self.color_mapping:
                    color = self.color_mapping[tile]
                    pygame.draw.rect(screen, color, (x * tile_size, y * tile_size, tile_size, tile_size))

    def get_player_start_position(self):
        for y, row in enumerate(self.layout):
            for x, tile in enumerate(row):
                if tile == '@':
                    return (x * 50, y * 50)  # Return the starting position of the player, adjusted for 50x50
        return None
