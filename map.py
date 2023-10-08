import pygame
import sys
import math

# Ініціалізація Pygame
pygame.init()

# Розміри вікна
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Колір фону
BACKGROUND_COLOR = (255, 255, 255)

# Створення вікна
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Мапа із правильними шестикутниками в Pygame")

# Початковий масштаб карти
scale_factor = 1.0

# Кількість рядів та стовпців
rows = 25
columns = 25

# Функція для збільшення масштабу
def increase_scale():
    global scale_factor
    scale_factor += 0.1

# Функція для зменшення масштабу
def decrease_scale():
    global scale_factor
    scale_factor -= 0.1
    # Заборона надто маленького масштабу
    if scale_factor < 0.1:
        scale_factor = 0.1

# Функція для визначення номера шестикутника по позиції кліка
def get_hexagon_number(x, y):
    col = int(x // (hexagon_width * 1.5))
    row = int((y - (col % 2) * (hexagon_height // 2)) // hexagon_height)
    return row * columns + col + 1

# Основний цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                increase_scale()
            elif event.key == pygame.K_DOWN:
                decrease_scale()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Ліва кнопка миші
                x, y = event.pos
                hexagon_number = get_hexagon_number(x, y)
                print(f"Номер шестикутника: {hexagon_number}")

    # Очищення екрану
    screen.fill(BACKGROUND_COLOR)

    # Розмір шестикутника
    hexagon_width = 40 * scale_factor
    hexagon_height = 40 * scale_factor

    # Відображення правильних шестикутників на карті
    for row in range(rows):
        for col in range(columns):
            x = col * (hexagon_width * 1.5)
            y = row * (hexagon_height + (hexagon_height / 2 if col % 2 == 1 else 0))
            pygame.draw.polygon(screen, (0, 0, 0), [
                (x, y), (x + hexagon_width, y), (x + hexagon_width * 0.5, y + hexagon_height),
                (x - hexagon_width * 0.5, y + hexagon_height)
            ], 2)

    # Оновлення вікна
    pygame.display.flip()

# Завершення гри
pygame.quit()
sys.exit()
