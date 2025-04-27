import pygame
import sys

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 10
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE
SAND = 1
BLOCK = 2

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sand Falling Simulation")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

placing_mode = SAND
running = False
step_mode = False
mouse_held = False

def draw_grid():
    screen.fill(BLACK)
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if grid[y][x] == SAND:
                pygame.draw.rect(screen, YELLOW, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif grid[y][x] == BLOCK:
                pygame.draw.rect(screen, GRAY, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    draw_ui()
    pygame.display.flip()

def draw_ui():
    # Display placing mode
    placing_text = f"Placing: {'Sand' if placing_mode == SAND else 'Block'}"
    placing_label = font.render(placing_text, True, WHITE)
    screen.blit(placing_label, (10, 10))

    # Display simulation status
    status_text = f"Simulation: {'Running' if running else 'Paused'}"
    status_label = font.render(status_text, True, RED if running else WHITE)
    screen.blit(status_label, (10, 30))

def update_grid():
    for y in range(GRID_HEIGHT - 2, -1, -1):
        for x in range(GRID_WIDTH):
            if grid[y][x] == SAND:
                if grid[y + 1][x] == 0:
                    grid[y][x] = 0
                    grid[y + 1][x] = SAND
                elif x > 0 and grid[y + 1][x - 1] == 0:
                    grid[y][x] = 0
                    grid[y + 1][x - 1] = SAND
                elif x < GRID_WIDTH - 1 and grid[y + 1][x + 1] == 0:
                    grid[y][x] = 0
                    grid[y + 1][x + 1] = SAND

def handle_input():
    global placing_mode, running, step_mode, mouse_held
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                placing_mode = SAND
            elif event.key == pygame.K_2:
                placing_mode = BLOCK
            elif event.key == pygame.K_SPACE:
                running = not running
            elif event.key == pygame.K_s:
                step_mode = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_held = True
            place_cell()
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_held = False

def place_cell():
    x, y = pygame.mouse.get_pos()
    grid_y, grid_x = y // CELL_SIZE, x // CELL_SIZE
    if 0 <= grid_y < GRID_HEIGHT and 0 <= grid_x < GRID_WIDTH:
        grid[grid_y][grid_x] = placing_mode

def main():
    global step_mode
    while True:
        handle_input()
        if mouse_held:
            place_cell()
        if running or step_mode:
            update_grid()
            step_mode = False
        draw_grid()
        clock.tick(30)

if __name__ == "__main__":
    main()