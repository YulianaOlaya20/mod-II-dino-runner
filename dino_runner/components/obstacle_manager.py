import random
import pygame
from dino_runner.components.catus import Cactus

from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS

class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            obstacle_image = random.choice(SMALL_CACTUS + LARGE_CACTUS)
            self.obstacles.append(Cactus(obstacle_image))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)