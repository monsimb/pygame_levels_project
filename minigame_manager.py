# minigame_manager.py
import pygame

class MiniGameManager:
    def __init__(self, levels):
        self.levels = levels

    def run_level(self, level_name, screen):
        # Dynamically import the level module
        level_module = __import__(f'levels.{level_name}', fromlist=[''])
        level_module.run_mini_game(screen)
