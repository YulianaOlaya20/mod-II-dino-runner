import random

from dino_runner.components.obstacles.cloud import Cloud
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.large_cactus import LargeCactus
from dino_runner.components.obstacles.small_catus import SmallCactus

from dino_runner.utils.constants import SMALL_CACTUS, CLOUD, LARGE_CACTUS, BIRD, SHIELD_TYPE, HAMMER_TYPE, DEAD, HEART_TYPE

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

        obstacle = obstacles_types[random.randint(0, 6)]
        obstacle.destroyed = False
        return obstacles_types[random.randint(0, 6)]
    
    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(self.generate_obstacle())

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.player.type == SHIELD_TYPE:
                print("Shield activated, no damage received")
                
            elif game.player.type == HAMMER_TYPE and game.player.dino_rect.colliderect(obstacle):
                self.obstacles = []
             
            elif game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                break


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def remove_obstacles(self):
        self.obstacles = []
