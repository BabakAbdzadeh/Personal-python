import pygame

pygame.init()

# colors
background_color = [212, 139, 107]
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
HOUSE = (0, 55, 255)
RED = (255, 0, 0)
DOOR = (159, 140, 132)
GROUND = (92, 222, 90)
SKY = (103, 238, 242)
SUN = (255, 191, 0)
PI = 3.141592653

# screen size
size = [800, 800]
screen = pygame.display.set_mode(size)
pygame.display.set_caption(" animation Girl ")

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # drawing phase:
        # 1. Clear the screen and set the screen background
    # sky
    screen.fill(SKY)
    # 2. Drawing
    # pygame.draw.arc(screen, BLACK, [280, 50, 250, 250], 0.15%PI, 3%PI)
    # roof
    pygame.draw.polygon(screen, RED, [(180, 200), (400, 80), (600, 200)])
    # building body
    pygame.draw.rect(screen, HOUSE, [230, 200, 320, 400])
    # windows
    # left sides
    # 1.1
    pygame.draw.rect(screen, BLACK, [240, 220, 50, 50])
    pygame.draw.rect(screen, BLACK, [240, 280, 50, 50])
    pygame.draw.rect(screen, BLACK, [240, 340, 50, 50])
    pygame.draw.rect(screen, BLACK, [240, 400, 50, 50])
    pygame.draw.rect(screen, BLACK, [240, 460, 50, 50])
    pygame.draw.rect(screen, BLACK, [240, 520, 50, 50])
    # 1.2
    pygame.draw.rect(screen, BLACK, [310, 220, 50, 50])
    pygame.draw.rect(screen, BLACK, [310, 220, 50, 50])
    pygame.draw.rect(screen, BLACK, [310, 280, 50, 50])
    pygame.draw.rect(screen, BLACK, [310, 340, 50, 50])
    pygame.draw.rect(screen, BLACK, [310, 400, 50, 50])
    pygame.draw.rect(screen, BLACK, [310, 460, 50, 50])
    pygame.draw.rect(screen, BLACK, [310, 520, 50, 50])
    pygame.draw.rect(screen, BLACK, [310, 220, 50, 50])
    # mid side
    pygame.draw.rect(screen, BLACK, [380, 220, 20, 300])
    # Right sides
    # 1.1
    pygame.draw.rect(screen, BLACK, [420, 220, 50, 50])
    pygame.draw.rect(screen, BLACK, [420, 280, 50, 50])
    pygame.draw.rect(screen, BLACK, [420, 340, 50, 50])
    pygame.draw.rect(screen, BLACK, [420, 400, 50, 50])
    pygame.draw.rect(screen, BLACK, [420, 460, 50, 50])
    pygame.draw.rect(screen, BLACK, [420, 520, 50, 50])
    # 1.2
    pygame.draw.rect(screen, BLACK, [490, 220, 50, 50])
    pygame.draw.rect(screen, BLACK, [490, 220, 50, 50])
    pygame.draw.rect(screen, BLACK, [490, 280, 50, 50])
    pygame.draw.rect(screen, BLACK, [490, 340, 50, 50])
    pygame.draw.rect(screen, BLACK, [490, 400, 50, 50])
    pygame.draw.rect(screen, BLACK, [490, 460, 50, 50])
    pygame.draw.rect(screen, BLACK, [490, 520, 50, 50])
    pygame.draw.rect(screen, BLACK, [490, 220, 50, 50])
    # Door
    pygame.draw.rect(screen, DOOR, [370, 550, 40, 50])
    # Ground
    pygame.draw.rect(screen, GROUND, [0, 600, 800, 200])
    # sun
    pygame.draw.circle(screen, SUN, [700, 100], 50)
    # 3. its time for flipping the screen after drawing(updating the screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
