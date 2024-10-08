from src.core.scene.run_scene import RunScene
from src.core.scene.menu_scene import MenuScene
from src.core.scene.game_scene import GameScene
from src.core.scene.core.scene_manager import SceneManager
from src.core.scene.core.save_scene import *
import pygame
import sys

save_init()

class App:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((1280, 720))
        pygame.display.set_caption('AncientLifeEmulator')
        
        set_scene('manager', SceneManager())
        set_scene('menu', MenuScene())
        set_scene('run', RunScene())
        set_scene('game', GameScene())
        
        self.surface_display = pygame.display.get_surface()
        
        self.clock = pygame.time.Clock()
        
        self.scene_manager = get_scene('manager')
        self.run_scene = get_scene('run')
        self.menu_scene = get_scene('menu')
        self.game_scene = get_scene('game')
        
    def update(self):
        self.clock.tick(60)
        self.scene_manager.on_update()
        self.surface_display.fill('black')
        self.scene_manager.on_draw()
        pygame.display.update()
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.scene_manager.on_input(event)
        
    def run(self):
        self.scene_manager.set_current_scene(get_scene('run'))
        self.scene_manager.on_enter()
        while True:
            self.handle_events()
            self.update()