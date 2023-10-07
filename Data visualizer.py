import pygame
import pickle

pygame.init()

WIDTH = 488
HEIGHT = 488

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Nasa Space App Challenge')

clock = pygame.time.Clock()
FPS = 60

colors = pickle.load(open("colors_exoplanet", "rb"))

run = True

while run:
    clock.tick(FPS)

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False 
            pygame.quit() 
            quit()
    col = 0
    row = 0
    for r in range(len(colors)):

        pygame.draw.rect(screen, colors[(r)], pygame.Rect(row*(WIDTH//round(len(colors) ** 0.5)), col*(WIDTH//round(len(colors) ** 0.5)), WIDTH//round(len(colors) ** 0.5), WIDTH//round(len(colors) ** 0.5)))
        row += 1
        if row > round(len(colors) ** 0.5) - 1:
            col += 1
            row = 0

    pygame.display.flip()

