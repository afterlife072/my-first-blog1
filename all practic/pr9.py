
import pygame
import sys

from pygame.color import THECOLORS

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Снеговик")


# Цвета
SKY_BLUE = (135, 206, 250)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (120, 120, 120)
ORANGE = (255, 69, 0)

# Основной цикл
def draw_snowman():
    screen.fill(SKY_BLUE)

    # Позиции центра
    center_x = WIDTH // 2
    base_y = HEIGHT - 100

    # Рисуем тело снеговика
    pygame.draw.circle(screen, WHITE, (center_x, base_y), 75)         # Нижний шар
    pygame.draw.circle(screen, WHITE, (center_x, base_y - 120), 55)   # Средний шар
    pygame.draw.circle(screen, WHITE, (center_x, base_y - 210), 35)   # Голова

    # Глаза
    pygame.draw.circle(screen, BLACK, (center_x - 10, base_y - 220), 4)
    pygame.draw.circle(screen, BLACK, (center_x + 10, base_y - 220), 4)

    # Нос
    pygame.draw.polygon(screen, ORANGE, [
        (center_x, base_y - 210),
        (center_x + 20, base_y - 195),
        (center_x, base_y - 200)
    ])
  # Ведро
    bucket_width = 55
    bucket_height = 60
    bucket_x = center_x - bucket_width // 2
    bucket_y = base_y - 290
    pygame.draw.rect(screen, GRAY, (bucket_x, bucket_y, bucket_width, bucket_height))

    # Руки
    pygame.draw.line(screen, BLACK, (center_x - 45, base_y - 120), (center_x - 90, base_y - 170), 3)
    pygame.draw.line(screen, BLACK, (center_x + 45, base_y - 120), (center_x + 90, base_y - 170), 3)

# Игровой цикл
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_snowman()
    pygame.display.flip()

pygame.quit()
sys.exit()
