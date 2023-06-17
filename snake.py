import pygame
import random

from config import ANCHO, ALTO, GRIDSIZE
from config import up, down, left, right

# La clase Snake representa
class Snake:
    def __init__(self):
        self.length = 1 # La culebrita inicia con un largo de 1
        self.positions = [((ANCHO // 2), ((ALTO - 40) // 2))] # la culebrita inicia en la mitad de la pantalla
        self.direction = random.choice([up, down, left, right]) # la dirección inicial de la culebra es escogida aleatoriamente
        self.color = (100,255,50) # color verde
        self.food_counter = 0

    def get_head_position(self):
        return self.positions[0]
    
    def turn(self, point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else: 
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y= self.direction
        new = (((cur[0]+(x*GRIDSIZE))%ANCHO), ((cur[1]-40+(y*GRIDSIZE))%(ALTO-40))+40)
        if new[1] < 40: new = (new[0], 40)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((ANCHO // 2), (ALTO // 2))]
        self.direction = random.choice([up, down, left, right])
    
    def draw(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, self.color, (p[0], p[1], GRIDSIZE, GRIDSIZE))
        
