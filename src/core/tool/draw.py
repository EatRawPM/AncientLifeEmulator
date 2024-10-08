import pygame
from src.data.assets import default_font

def draw_text(text, font: str=default_font, size: int=30, color: str | tuple[int, int, int] = 'white', x: int=0, y: int=0):
    pygame.init()
    surface_display = pygame.display.get_surface()
    Font = pygame.font.Font(font, size)
    surface = Font.render(str(text), True, color)
    rect = surface.get_rect(topleft = (x, y))
    surface_display.blit(surface, rect)