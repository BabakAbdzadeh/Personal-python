import pygame
import math
import time

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (0xFF, 0xFF, 0xFF)
PI = 3.141592653

size = [400, 400]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Professor Craven's Cool Game")

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # drawing phase:
    # 1. Clear the screen and set the screen background
    screen.fill(WHITE)
    # 2. Drawing
    # pygame.draw.rect(screen, RED, [0, 350, 20, 20])
    # pygame.draw.polygon(screen, RED, [(10, 10), (50, 90), (110, 30)])
    # y_offset = 0
    # while y_offset < 100:
    #     pygame.draw.line(screen, RED, [0, 10 + y_offset], [100, 110 + y_offset], 5)
    #     y_offset = y_offset + 10
    offset = 0
    while offset < 100:
        pygame.draw.line(screen, RED, [50 + offset, 20], [50 + offset, 60], 5)
        offset = offset + 10
    # pygame.draw.ellipse(screen, BLACK, [20, 20, 250, 100], 2)
    # pygame.draw.arc(screen, GREEN, [100, 100, 250, 200], PI / 2, PI, 2)
    # pygame.draw.arc(screen, BLACK, [100, 100, 250, 200], 0, PI / 2, 2)
    # pygame.draw.arc(screen, RED, [100, 100, 250, 200], 3 * PI / 2, 2 * PI, 2)
    # pygame.draw.arc(screen, BLUE, [100, 100, 250, 200], PI, 3 * PI / 2, 2)
    # 3. its time for flipping the screen after drawing(updating the screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
