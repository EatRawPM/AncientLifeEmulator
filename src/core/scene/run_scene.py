import pygame
from src.core.scene.core.scene import Scene
from src.core.scene.core.save_scene import get_scene
from src.core.tool.draw import draw_text
from src.timer import *

class RunScene(Scene):
    def __init__(self):
        super().__init__()
        self.scene_manager = get_scene('manager')
        
        self.timer = CountdownTimer(3)
        
    def on_enter(self):
        self.timer.start()
    
    def on_update(self):
        if self.timer.is_done():
            self.scene_manager.switch_scene('menu')
    
    def on_draw(self):
        draw_text(f'{self.timer.remaining_time()}')

    def on_input(self, event: pygame.event.EventType): ...
    
    def on_exit(self): ...