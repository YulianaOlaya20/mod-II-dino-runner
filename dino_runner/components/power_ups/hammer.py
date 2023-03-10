from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import HAMMER_TYPE

class Hammer(PowerUp):

    def __init__(self, image):
        super().__init__(image)
        self.type = HAMMER_TYPE
