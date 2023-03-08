from dino_runner.components.obstacles.obstacle import Obstacle

class SmallCactus(Obstacle):

    def __init__(self, image):
        super().__init__(image)
        self.rect.y = 325