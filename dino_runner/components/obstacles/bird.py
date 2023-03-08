import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    def __init__(self, image):
        super().__init__(image)
        self.rect.y = random.randint(100, 300)
        self.step = 0

    def update(self, game_speed, obstacles):
        self.image = BIRD[0] if self.step <= 4 else BIRD[1]
        super().update(game_speed, obstacles)

        self.step += 1
        if self.step == 8:
            self.step = 0