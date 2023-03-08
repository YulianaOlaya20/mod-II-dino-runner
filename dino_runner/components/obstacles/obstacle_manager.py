import random
import pygame
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.large_cactus import LargeCactus
from dino_runner.components.obstacles.small_catus import SmallCactus

from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

class ObstacleManager:

    def __init__(self):
        self.obstacles = []


    def generate_obstacle(self): 
        obstacles_types = {
            0: SmallCactus(SMALL_CACTUS[0]),
            1: SmallCactus(SMALL_CACTUS[1]),  
            2: SmallCactus(SMALL_CACTUS[2]),  
            3: LargeCactus(LARGE_CACTUS[0]),  
            4: LargeCactus(LARGE_CACTUS[1]),    
            5: LargeCactus(LARGE_CACTUS[2]),   
            6: Bird(BIRD[0]), 
        }

        return obstacles_types[random.randint(0, 6)]
    
    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(self.generate_obstacle())

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break
            

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def remove_obstacles(self):
        self.obstacles = []


    def check_collision(self, player):
        for obstacle in self.obstacles:
            if player.dino_rect.colliderect(obstacle.rect):
                return True
        return False
