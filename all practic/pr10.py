import pygame
import sys

pygame.init()


WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Сетка квадратов с номерами")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

square_size = 40
gap = 5

font_size = 16
font = pygame.font.SysFont(None, font_size)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)


    screen.fill(WHITE)

    num_cols = (WIDTH + gap) // (square_size + gap)
    num_rows = (HEIGHT + gap) // (square_size + gap)

    square_number = 1
    for row in range(num_rows):
        for col in range(num_cols):
            x = col * (square_size + gap)
            y = row * (square_size + gap)

            pygame.draw.rect(screen, BLUE, (x, y, square_size, square_size))

            text_surface = font.render(str(square_number), True, WHITE)
            text_rect = text_surface.get_rect(center=(x + square_size // 2, y + square_size // 2))
            screen.blit(text_surface, text_rect)

            square_number += 1

    pygame.display.flip()

pygame.quit()
sys.exit()
















































































