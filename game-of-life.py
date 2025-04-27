import pygame
import sys

# Constants
WIDTH, HEIGHT = 500, 500
CELL_SIZE = 10
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

def draw_grid():
    screen.fill(WHITE)
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if grid[y][x] == 1:
                pygame.draw.rect(screen, RED, rect)
            pygame.draw.rect(screen, GRAY, rect, 1)

def draw_ui(paused):
    # Display simulation status
    status_text = f"Simulation: {'Paused' if paused else 'Running'}"
    status_color = GREEN if not paused else RED
    status_label = font.render(status_text, True, status_color)
    screen.blit(status_label, (10, 10))

def get_neighbors(x, y):
    neighbors = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < GRID_WIDTH and 0 <= ny < GRID_HEIGHT:
                neighbors += grid[ny][nx]
    return neighbors

def update_grid():
    new_grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            neighbors = get_neighbors(x, y)
            if grid[y][x] == 1 and (neighbors == 2 or neighbors == 3):
                new_grid[y][x] = 1
            elif grid[y][x] == 0 and neighbors == 3:
                new_grid[y][x] = 1
    return new_grid

def main():
    running = True
    paused = True
    mouse_held = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_held = True
                x, y = event.pos
                grid[y // CELL_SIZE][x // CELL_SIZE] = 1 - grid[y // CELL_SIZE][x // CELL_SIZE]
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_held = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                elif event.key == pygame.K_s and paused:
                    grid[:] = update_grid()

        if mouse_held:
            x, y = pygame.mouse.get_pos()
            grid[y // CELL_SIZE][x // CELL_SIZE] = 1

        if not paused:
            grid[:] = update_grid()

        draw_grid()
        draw_ui(paused)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()