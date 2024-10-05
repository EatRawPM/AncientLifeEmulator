import pygame
from src.core.scene.core.scene import Scene
from src.core.tool.draw import draw_text
from src.core.scene.core.save_scene import get_scene

class MenuScene(Scene):
    def __init__(self):
        super().__init__()
        self.scene_manager = get_scene('manager')
        
    def on_enter(self): ...
    
    def on_update(self): ...
    
    def on_draw(self):
        draw_text('按下任意键切换')

    def on_input(self, event: pygame.event.EventType):
        if event.type == pygame.KEYDOWN:
            self.scene_manager.switch_scene('game')
    
    def on_exit(self): ...