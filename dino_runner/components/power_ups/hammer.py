
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import HAMMER_TYPE

class Hammer(PowerUp):

    def __init__(self, image):
        super().__init__(image)
        self.type = HAMMER_TYPE

    
    def check_collision(self, rect):
        return self.image.get_rect().colliderect(rect)

    def activate(self, obstacle, game):
        game.obstacle_manager.remove(obstacle)
        self.kill()