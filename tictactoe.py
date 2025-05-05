import pygame

pygame.init()

WIDTH, HEIGHT = 600, 600  # Reduced size for better visibility
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BOARD = [["" for _ in range(3)] for _ in range(3)]

FONT = pygame.font.SysFont("Arial", WIDTH // 6)  # Scalable font


def draw_board():
    SCREEN.fill(WHITE)  # Clear screen before redrawing

    cell_size = WIDTH // 3  # Dynamic size based on WIDTH
    for i in range(1, 3):
        pygame.draw.line(SCREEN, BLACK, (i * cell_size, 0), (i * cell_size, HEIGHT), 5)
        pygame.draw.line(SCREEN, BLACK, (0, i * cell_size), (WIDTH, i * cell_size), 5)

    for row in range(3):
        for col in range(3):
            if BOARD[row][col]:
                text = FONT.render(BOARD[row][col], True, BLACK)
                text_rect = text.get_rect(center=((col + 0.5) * cell_size, (row + 0.5) * cell_size))
                SCREEN.blit(text, text_rect)


def check_winner():
    for i in range(3):
        if BOARD[i][0] == BOARD[i][1] == BOARD[i][2] != "":
            return BOARD[i][0]
        if BOARD[0][i] == BOARD[1][i] == BOARD[2][i] != "":
            return BOARD[0][i]

    if BOARD[0][0] == BOARD[1][1] == BOARD[2][2] != "":
        return BOARD[0][0]
    if BOARD[0][2] == BOARD[1][1] == BOARD[2][0] != "":
        return BOARD[0][2]

    return None


def reset_game():
    global BOARD, turn, running
    BOARD = [["" for _ in range(3)] for _ in range(3)]
    turn = "X"
    running = True


running = True
turn = "X"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            col, row = x // (WIDTH // 3), y // (HEIGHT // 3)  # Corrected index calculation

            if BOARD[row][col] == "":
                BOARD[row][col] = turn
                winner = check_winner()
                if winner:
                    print(f"¡{winner} gana!")
                    pygame.time.delay(1000)  # Pause before resetting
                    reset_game()

                turn = "O" if turn == "X" else "X"

    draw_board()
    pygame.display.flip()

pygame.quit()
