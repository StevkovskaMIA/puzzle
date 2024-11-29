import pygame

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 500, 600
GRID_SIZE = 5
TILE_SIZE = WINDOW_WIDTH // GRID_SIZE
PALETTE_HEIGHT = 50
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Color Fill Puzzle")

board = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

selected_color = None

def is_valid_color(row, col, color):
    neighbors = [
        (-1, 0), (1, 0), (0, -1), (0, 1)
    ]
    for dr, dc in neighbors:
        nr, nc = row + dr, col + dc
        if 0 <= nr < GRID_SIZE and 0 <= nc < GRID_SIZE:
            if board[nr][nc] == color:
                return False
    return True


def check_win():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if board[i][j] is None:
                return False
            neighbors = [
                (-1, 0), (1, 0), (0, -1), (0, 1)
            ]
            for dr, dc in neighbors:
                nr, nc = i + dr, j + dc
                if 0 <= nr < GRID_SIZE and 0 <= nc < GRID_SIZE:
                    if board[i][j] == board[nr][nc]:
                        return False
    return True

def draw_board():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            color = board[i][j] if board[i][j] else WHITE
            pygame.draw.rect(screen, color, (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, (0, 0, 0), (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

def draw_palette():
    for i, color in enumerate(COLORS):
        pygame.draw.rect(screen, color, (i * TILE_SIZE, WINDOW_HEIGHT - PALETTE_HEIGHT, TILE_SIZE, PALETTE_HEIGHT))
        pygame.draw.rect(screen, (0, 0, 0), (i * TILE_SIZE, WINDOW_HEIGHT - PALETTE_HEIGHT, TILE_SIZE, PALETTE_HEIGHT), 1)

def handle_click(x, y):
    global selected_color
    if y < WINDOW_HEIGHT - PALETTE_HEIGHT:
        row, col = y // TILE_SIZE, x // TILE_SIZE
        if selected_color:
            if is_valid_color(row, col, selected_color):
                board[row][col] = selected_color
                print(f"Успешно ја променивте бојата на квадратот ({row}, {col}) на {selected_color}.")
            else:
                print(f"Не можете да ја промените бојата на квадратот ({row}, {col}) на {selected_color}.")
                print("Причина: Еден од соседите веќе ја има истата боја.")
        else:
            print("Не е избрана боја! Изберете боја од палетата.")
    else:
        palette_index = x // TILE_SIZE
        if 0 <= palette_index < len(COLORS):
            selected_color = COLORS[palette_index]
            print(f"Избравте боја: {selected_color}")

def display_congratulations():
    font = pygame.font.SysFont(None, 50)
    text = font.render("Congratulations!", True, (0, 0, 0))
    screen.blit(text, (WINDOW_WIDTH // 4, WINDOW_HEIGHT // 2))

def main():
    global selected_color
    running = True
    while running:
        screen.fill(WHITE)
        draw_board()
        draw_palette()

        if check_win():
            display_congratulations()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                handle_click(x, y)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
