# levels/level2.py
import pygame

layout = [
    "##########",
    "#        #",
    "#        #",
    "#        #",
    "#        #",
    "#        #",
    "#        #",
    "#        #",
    "#        #",
    "##########",
]

color_mapping = {
    '#': (0, 255, 0),  # Green for walls
    ' ': (0, 0, 0),    # Black for empty space
    '@': (0, 0, 0),    # Player's position; color won't be used as sprite will be drawn
    'E': (0, 0, 0),    # Enemy's position; color won't be used as sprite will be drawn
}

sprites = {
    '@': 'sprites/lvl1_player.png',  # Player sprite
    'E': 'sprites/lvl1_enemy.png',   # Enemy sprite
}



# Gameplay logic for the mini-game
def run_mini_game(screen):
    # Initialize player and enemy positions, scores, etc.
    player_pos = (100, 100)
    player = sprites['@']
    
    # Simple game loop for this mini-game
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Example: simple player movement
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx = -5
        if keys[pygame.K_RIGHT]:
            dx = 5
        if keys[pygame.K_UP]:
            dy = -5
        if keys[pygame.K_DOWN]:
            dy = 5

        player_pos = (player_pos[0] + dx, player_pos[1] + dy)

        # Drawing
        screen.fill((0, 0, 0))  # Clear screen
        draw_level(screen, layout, sprites, color_mapping)
        screen.blit(pygame.image.load(player), player_pos)
        pygame.display.flip()

        clock.tick(60)

def draw_level(screen, layout, sprites, color_mapping):
    tile_size = 50  # Set tile size
    for y, row in enumerate(layout):
        for x, tile in enumerate(row):
            if tile in sprites:
                sprite_image = pygame.image.load(sprites[tile]).convert_alpha()
                screen.blit(sprite_image, (x * tile_size, y * tile_size))
            elif tile in color_mapping:
                color = color_mapping[tile]
                pygame.draw.rect(screen, color, (x * tile_size, y * tile_size, tile_size, tile_size))
