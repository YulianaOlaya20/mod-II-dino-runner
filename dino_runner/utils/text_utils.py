import pygame

from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

FONT_STYLE = 'freesansbold.ttf'
BLACK_COLOR = (0,0,0)

def get_score_element(points):
    font = pygame.font.Font(FONT_STYLE, 20)
    text = font.render(f"Point:{points}", True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (1000, 35)
    return text, text_rect


def get_centered_message(message):
    font = pygame.font.Font(FONT_STYLE, 50)
    text = font.render(message, True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    return text, text_rect
