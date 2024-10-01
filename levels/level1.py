# levels/level1.py
from player import Player
import pygame
from config import MAZE_WIDTH,TILE, PLAYER_START, END_RECT

'''
as you make your layout, keep in mind that the window will be sized to whatever screen it detects! that's why we use the MAZE_WIDTH constant below
'''

layout = [      # ' ' = empty, '#' = wall, '@' = player, 'E' = enemy
    "#"*(MAZE_WIDTH+1),
    "#"+" "*(MAZE_WIDTH-1)+"#",
    "#"+" "*(MAZE_WIDTH-1)+"#",
    "# ###"+" "*(MAZE_WIDTH-5)+"#",
    "#"+" "*(MAZE_WIDTH-1)+"#",
    "#"+" "*(MAZE_WIDTH-1)+"#",
    "#"+" "*(MAZE_WIDTH-1)+"#",
    "#"+" "*(MAZE_WIDTH-1)+"#",
    "#"+" "*(MAZE_WIDTH-1)+"#",
    "#"+" "*(MAZE_WIDTH-1)+"#",
    "#"+" "*(MAZE_WIDTH-1)+"#",
    "# "+" "*(MAZE_WIDTH-7)+"######",
    "#"+" "*(MAZE_WIDTH-1)+"#",
    "#"+" "*(MAZE_WIDTH-1)+"#",
    "#"+" "*(MAZE_WIDTH-1)+"#",
    "#"+" "*(MAZE_WIDTH-1)+"#",
    "#"+" "*(MAZE_WIDTH-1)+"#",
    "#"+" "*(MAZE_WIDTH-1)+"#",
    "#"+" "*(MAZE_WIDTH-1)+"#",
    "#"+" "*(MAZE_WIDTH-1)+"#",
    "#"+" "*(MAZE_WIDTH-1)+"#",
    "#"*(MAZE_WIDTH)+"#",
]

''' 
This is where you store your colors! You can change these or add new colors to them if you're adding new obstacles
'''
color_mapping = {
    '#': (0, 250, 0),  # Green for walls
    ' ': (0, 0, 0),    # Black for empty space
    '@': (0, 0, 0),    # Player's position; color won't be used as sprite will be drawn
    'E': (0, 0, 250),    # Enemy's position; color won't be used as sprite will be drawn
}

'''
This is where sprite image paths are stored. If you want to add or changes images for objects (like the walls, end goal, and anything else you add),
upload them to the sprites folder and make sure you have the right path listed next to the element identifier.

Before you add images for objects that don't currently have them, keep in mind that this will change what your draw_maze function looks like!
'''
sprites = {
    '@': 'sprites/lvl1_player.png',  # Player sprite
    # 'E': 'sprites/lvl1_enemy.png',   # Enemy sprite
}

# Gameplay logic for the mini-game
def run_mini_game(screen):
    player = Player(PLAYER_START[0], PLAYER_START[1], sprites['@'])

    clock = pygame.time.Clock()
    running = True
    while running:
        # Check if player has won
        if player.rect.colliderect(END_RECT):
            running = False

        # Check if player wants to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Player movement
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

        # Update player position with collision detection
        player.update(dx, dy, layout)

        # Drawing
        screen.fill((0, 0, 0))  # Clear screen
        draw_level(screen, layout, sprites, color_mapping)
        player.draw(screen)
        pygame.display.flip()

        clock.tick(60)

def draw_level(screen, layout, sprites, color_mapping):
    for y, row in enumerate(layout):        # y = index, row contains contents of each row
        for x, tile in enumerate(row):      # x = index, tile = character at index (' ', '#', or '@')
            if tile in sprites:     # check if tile is player first
                sprite_image = pygame.image.load(sprites[tile]).convert_alpha()
                sprite_image = pygame.transform.scale(sprite_image, (TILE, TILE))
                screen.blit(sprite_image, (x * TILE, y * TILE))
            elif tile in color_mapping:     # if not player, apply appropriate color mapping
                color = color_mapping[tile]
                pygame.draw.rect(screen, color, (x * TILE, y * TILE, TILE, TILE))
    
    pygame.draw.rect(screen, color_mapping['E'], END_RECT)      # DO NOT REMOVE OR CHANGE THIS