import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import  HAMMER_TYPE, DEFAULT_TYPE, SHIELD_TYPE, RUNNING, DUCKING, JUMPING, RUNNING_SHIELD, JUMPING_SHIELD, DUCKING_SHIELD, RUNNING_HAMMER, JUMPING_HAMMER, DUCKING_HAMMER 


class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    JUMP_VEL = 20
    Y_POS_LIMIT = 100
    POWER_UP_TIME = 200 
    MAX_HAMMER_HITS = 3
 

    def __init__(self):
        self.image = RUNNING[0] 
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.type = DEFAULT_TYPE
        self.run_img = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER }
        self.jump_img = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE:JUMPING_HAMMER}
        self.duck_img = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE:DUCKING_HAMMER }
        self.power_up_time = 0
        self.hammer_hits = 0


    def process_event(self, user_input):
        if user_input[pygame.K_DOWN]:
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False
        elif user_input[pygame.K_UP]:
            self.dino_run = False
            self.dino_duck  = False
            self.dino_jump = True
        

    def update(self, user_input):
        self.process_event(user_input)
        if self.dino_duck:
            self.duck()
        elif self.dino_jump:
            self.jump()
        else:
            self.run()

        self.power_up_time -=1
        if self.power_up_time < 0:
            self.type = DEFAULT_TYPE

        self.step_index = self.step_index + 1
        if self.step_index == 10:
            self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
    
    def run(self):
        self.image  = self.run_img[self.type][0] if self.step_index < 5 else self.run_img[self.type][1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS

    def duck(self):
        self.image  = self.duck_img[self.type][0] if self.step_index < 5 else self.duck_img[self.type][1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS + 35
        self.dino_duck = False

    def jump(self):
            self.image = self.jump_img[self.type]
            self.dino_rect.x = self.X_POS
            self.dino_rect.y -= self.JUMP_VEL
            if self.dino_rect.y <= self.Y_POS_LIMIT:
                self.JUMP_VEL *= -1
            if self.dino_rect.y > self.Y_POS:
                self.JUMP_VEL *= -1
                self.dino_rect.y = self.Y_POS
                self.dino_jump = False

    def activate_power_up(self, power_up_type):
        if power_up_type == SHIELD_TYPE:
            self.type = SHIELD_TYPE
            self.power_up_time = self.POWER_UP_TIME

        elif power_up_type == HAMMER_TYPE:
            self.type = HAMMER_TYPE
            self.power_up_time = self.POWER_UP_TIME

            
