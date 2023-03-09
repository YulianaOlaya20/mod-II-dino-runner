import pygame

from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

FONT_STYLE = 'freesansbold.ttf'
BLACK_COLOR = (0,0,0)

def get_score_element(points):
    font = pygame.font.Font(FONT_STYLE, 20)
    text = font.render(f"Point:{points}", True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (1000, 30)
    return text, text_rect


def get_centered_message(message, x_offset = 0, y_offset = 0, font_size = 30):
    font = pygame.font.Font(FONT_STYLE, font_size)
    text = font.render(message, True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = ((SCREEN_WIDTH // 2) + x_offset, (SCREEN_HEIGHT // 2) + y_offset)
    return text, text_rect


