import pygame
import random
from dino_runner.utils.constants import CLOUD
from dino_runner.utils.constants import ICON 
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager

from dino_runner.utils.constants import BG, ICON, INITIAL_GAME_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.utils.text_utils import get_centered_message, get_score_element, get_score_deaths


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = INITIAL_GAME_SPEED
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.points = 0
        self.deaths = 0


    def show_score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1
        score, score_rect = get_score_element(self.points)
        self.screen.blit(score, score_rect)

    def show_deaths(self):

        if self.playing == False:
            self.deaths += 1

    def show_menu(self):
        self.screen.fill((255,255,255))

        wallpaper_rect = ICON.get_rect()
        wallpaper_rect.topleft = (510, 170) 
        self.screen.blit(ICON, wallpaper_rect)

        text, text_rect = get_centered_message('START!')
        death, death_rect = get_score_deaths(self.deaths)
        self.screen.blit(death, death_rect)
        self.screen.blit(text, text_rect)
        pygame.display.update()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                print("Game Over")
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.time.delay(1000)
        self.obstacle_manager.remove_obstacles()
        self.power_up_manager.remove_power_ups()
        self.game_speed = INITIAL_GAME_SPEED
        self.points = 0

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.show_score()
        self.show_deaths()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_cloud(self):
        image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.x_pos_cl, self.y_pos_cl))
        self.x_pos_cl -= self.game_speed
        if self.x_pos_bg <= -image_width:
            self.x_pos_cl = SCREEN_WIDTH + 1000
            self.y_pos_cl = random.randint(50, 100)
            self.screen.blit (CLOUD, (self.x_pos_cl, self.y_pos_cl))
          