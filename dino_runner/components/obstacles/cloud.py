import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import CLOUD


class Cloud(Obstacle):
    def __init__(self):
        super().__init__(CLOUD)
        self.rect.y = random.randint(100, 300)
        self.step = 0

    def update(self, game_speed, obstacles):
        self.image = CLOUD[0] if self.step <= 4 else CLOUD[1]
        super().update(game_speed, obstacles)
