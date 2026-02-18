import pygame
import sys
import random as r
from Button import Button

class MarsGame:
    def __init__(self):
        pygame.init()

        #game window saved as class attribute
        self.window = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Mars Game")

        self.test_rect = pygame.Rect(0, 0, 1200, 100)

        self.clock = pygame.time.Clock()

    def run_game(self):
        while True:
            #get all user inputs (e.g. mouse, keyboard, ...), go through them
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close_window()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.get_clicked()
            
            #self.window.fill((r.randrange(0, 255), r.randrange(0, 255), r.randrange(0, 255)))
            self.window.fill((158, 255, 224))

            pygame.draw.rect(self.window, (255, 255, 255), self.test_rect)
            #self.test_rect.move_ip(0, 1)

            test_rect_2 = pygame.Rect(0, 100, 900, 700)
            pygame.draw.rect(self.window, (0, 0, 0), test_rect_2)

            test_button = Button(10, 10, 100, 100, "red")
            test_button.draw(self.window)

            test_button2 = Button(50, 100, 200, 50, "blue")
            test_button2.draw(self.window)

            pygame.display.flip()
            self.clock.tick(60)

    def close_window(self):
        sys.exit()