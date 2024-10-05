import pygame
from src.core.scene.core.scene import Scene
from src.core.tool.draw import draw_text
from src.core.scene.core.save_scene import get_scene

class GameScene(Scene):
    def __init__(self):
        super().__init__()
        self.scene_manager = get_scene('manager')

    def on_enter(self): ...

    def on_update(self): ...

    def on_draw(self):
        draw_text('游戏界面')

    def on_input(self, event: pygame.event.EventType): ...

    def on_exit(self): ...