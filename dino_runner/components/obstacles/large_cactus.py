from dino_runner.components.obstacles.obstacle import Obstacle

class LargeCactus(Obstacle):

    def __init__(self, image):
        super().__init__(image)
        self.rect.y = 300