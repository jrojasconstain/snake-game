import pygame
import random

from config import ANCHO, ALTO, GRIDSIZE
from snake import Snake

class Food:
    def __init__(self, snake):
        self.snake = snake
        self.position = (0,0)
        self.color = (255, 50, 49)
        self.apple_img = pygame.image.load('assets/images/apple.png')
        self.apple_img = pygame.transform.scale(self.apple_img, (GRIDSIZE, GRIDSIZE))
        self.mouse_img = pygame.image.load('assets/images/mouse.png')
        self.mouse_img = pygame.transform.scale(self.mouse_img, (GRIDSIZE + 3, GRIDSIZE + 3))
        self.is_special = False
        self.randomize()

    def randomize(self):
        all_positions = [(x*GRIDSIZE, y*GRIDSIZE) for x in range(0, ANCHO//GRIDSIZE) for y in range(4, (ALTO - 40)//GRIDSIZE)]
        free_positions = list(set(all_positions) - set(self.snake.positions))
        self.position = random.choice(free_positions)

    def draw(self, surface):
        if self.is_special:
            surface.blit(self.mouse_img, (self.position[0], self.position[1]))
        else: 
             surface.blit(self.apple_img, (self.position[0], self.position[1]))

