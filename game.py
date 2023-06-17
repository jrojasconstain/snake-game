import pygame
import pickle
from config import ANCHO, ALTO, GRIDSIZE, up, down, left, right
from snake import Snake
from food import Food

class Game:
    def __init__(self):
        pygame.init() # init all omported pygame modules 
        
        self.window = pygame.display.set_mode((ANCHO, ALTO))
        
        self.snake = Snake()
        self.food = Food(self.snake)

        self.font = pygame.font.Font(None, 25)
        self.small_font = pygame.font.Font(None, 15)

        self.score_tracker = ScoreTracker()
    
    def get_fps(self):
        return 10 + (self.snake.length // 10) * 5
    
    def run(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.snake.direction != down:
                        self.snake.direction = up
                    elif event.key == pygame.K_DOWN and self.snake.direction != up:
                        self.snake.direction = down
                    elif event.key == pygame.K_LEFT and self.snake.direction != right:
                        self.snake.direction = left
                    elif event.key == pygame.K_RIGHT and self.snake.direction != left:
                        self.snake.direction = right

            self.snake.move()
            
            if self.snake.get_head_position() == self.food.position:
                if self.food.is_special:
                    self.snake.length += 3
                else:
                    self.snake.length += 1 # aumenta el largo de la culebra
                self.snake.food_counter += 1
                self.food.is_special = self.snake.food_counter % 5 == 0
                self.score_tracker.update_high_score(self.snake.length)
                self.food.randomize() # genera nueva comida

            self.window.fill((0, 0, 0)) # Área del juego
            # self.window.fill((50,50,50), (0, 0, ANCHO, 40)) # Área de la puntuación
            pygame.draw.rect(self.window, (50, 50, 50), pygame.Rect(0, 0, ANCHO, 40)) 

            self.food.draw(self.window)
            self.snake.draw(self.window)

            text_score = self.font.render(f"Score: {self.snake.length}", True, (255, 255, 255))
            
            text_high_score= self.font.render(f"High Score: {self.score_tracker.high_score}", True, (255, 255, 255))

            text_credits = self.small_font.render ("Creado por J.J. Rojas-Constaín", True, (200, 200, 200))

            self.window.blit(text_score, (20, 12))
            self.window.blit(text_high_score, (ANCHO - 135, 12))
            self.window.blit(text_credits, (140, 425))

            pygame.display.update()

            clock.tick(self.get_fps())

        pygame.quit()

class ScoreTracker:
    def __init__(self):
        self.high_score_file = "high_score.dat"
        self.high_score = 0

        try:
            with open(self.high_score_file, 'rb') as f:
                self.high_score = pickle.load(f)
        except (OSError, IOError) as e:
            self.high_score = 0

    def update_high_score(self, score):
        if score > self.high_score:
            self.high_score = score
            with open(self.high_score_file, 'wb') as f:
                pickle.dump(self.high_score, f)

if __name__ == "__main__":
    game = Game()
    game.run()
